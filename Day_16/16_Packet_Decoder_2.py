import fileinput
import math


def decodePacket(bits: str, pos=0) -> tuple[int, int]:
    if len(bits) - pos < 6:
        return -1, -1

    p_ver = int(bits[pos : pos + 3], 2)
    pos += 3

    p_type_id = int(bits[pos : pos + 3], 2)
    pos += 3

    if p_type_id == 4:
        p_val = 0
        more = True
        while more:
            more = bits[pos : pos + 1] == "1"
            pos += 1
            group = int(bits[pos : pos + 4], 2)
            pos += 4
            p_val <<= 4
            p_val += group
        return pos, p_val
    else:
        p_len_type_id = bits[pos : pos + 1]
        pos += 1
        vals = []
        if p_len_type_id == "0":
            p_len = int(bits[pos : pos + 15], 2)
            pos += 15
            limit = pos + p_len
            while pos < limit:
                d = decodePacket(bits, pos)
                pos = d[0]
                vals.append(d[1])
        elif p_len_type_id == "1":
            p_len = int(bits[pos : pos + 11], 2)
            pos += 11
            for i in range(p_len):
                d = decodePacket(bits, pos)
                pos = d[0]
                vals.append(d[1])
        if p_type_id == 0:
            return pos, sum(vals)
        elif p_type_id == 1:
            return pos, math.prod(vals)
        elif p_type_id == 2:
            return pos, min(vals)
        elif p_type_id == 3:
            return pos, max(vals)
        elif p_type_id == 5:
            return pos, 1 if vals[0] > vals[1] else 0
        elif p_type_id == 6:
            return pos, 1 if vals[0] < vals[1] else 0
        elif p_type_id == 7:
            return pos, 1 if vals[0] == vals[1] else 0
        else:
            assert False


def main() -> None:
    for line in fileinput.input():
        bits = bin(int(line.strip(), 16))[2:].zfill((len(line) - 1) * 4)

        print(decodePacket(bits, 0)[1])


if __name__ == "__main__":
    main()
