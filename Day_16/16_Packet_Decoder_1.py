import fileinput

sum_versions = 0


def decodePacket(bits: str, pos=0) -> int:
    global sum_versions

    if len(bits) - pos < 6:
        return -1

    p_ver = int(bits[pos : pos + 3], 2)
    pos += 3

    sum_versions += p_ver
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
        return pos
    else:
        p_len_type_id = bits[pos : pos + 1]
        pos += 1
        if p_len_type_id == "0":
            p_len = int(bits[pos : pos + 15], 2)
            pos += 15
            limit = pos + p_len
            while pos < limit:
                pos = decodePacket(bits, pos)
            return pos
        elif p_len_type_id == "1":
            p_len = int(bits[pos : pos + 11], 2)
            pos += 11
            for i in range(p_len):
                pos = decodePacket(bits, pos)
            return pos


def main() -> None:
    for line in fileinput.input():
        bits = bin(int(line.strip(), 16))[2:].zfill((len(line) - 1) * 4)

        decodePacket(bits, 0)

        print(sum_versions)


if __name__ == "__main__":
    main()
