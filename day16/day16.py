import math

# Probably not the cleanest version of this problem :(


def decode_packet_type4(encoded_str):
    last_group, nb, len_decoded = False, '', 0

    while not last_group:
        last_group = True if encoded_str[0] == '0' else False
        nb += encoded_str[1:5]
        encoded_str = encoded_str[5:]
        len_decoded += 5
    return encoded_str, int(nb, 2), len_decoded


def decode_value(type_packet, list_values):
    if type_packet == 0:
        return sum(list_values)
    elif type_packet == 1:
        return math.prod(list_values)
    elif type_packet == 2:
        return min(list_values)
    elif type_packet == 3:
        return max(list_values)
    elif type_packet == 5:
        assert len(list_values) == 2
        return 1 if list_values[0] > list_values[1] else 0
    elif type_packet == 6:
        assert len(list_values) == 2
        return 1 if list_values[0] < list_values[1] else 0
    else:
        assert type_packet == 7
        assert len(list_values) == 2
        return 1 if list_values[0] == list_values[1] else 0


def decode_packet(encoded_str, total_version):
    version = int(encoded_str[:3], 2)
    type_id = int(encoded_str[3:6], 2)
    len_decoded = 6
    total_version += version

    if type_id == 4:
        encoded_str, value, length = decode_packet_type4(encoded_str[6:])
        len_decoded += length

    else:
        length_type_id = int(encoded_str[6])
        len_decoded += 1
        l_value = []
        if length_type_id == 0:
            length = int(encoded_str[7:22], 2)
            len_decoded += 15 + length
            encoded_str = encoded_str[22:]
            cur_len_decoded = 0
            while cur_len_decoded != length:
                encoded_str, tmp, total_version, value = decode_packet(encoded_str, total_version)
                cur_len_decoded += tmp
                l_value.append(value)
        else:
            nb_packets = int(encoded_str[7:18], 2)
            encoded_str = encoded_str[18:]
            len_decoded += 11
            for i in range(nb_packets):
                encoded_str, tmp, total_version, value = decode_packet(encoded_str, total_version)
                len_decoded += tmp
                l_value.append(value)

        value = decode_value(type_id, l_value)

    return encoded_str, len_decoded, total_version, value


def main(filename):
    with open('decoder.txt', 'r') as file:
        lines = [line.rstrip() for line in file.read().split('\n')]
        dict_hex_bin = {line.split(' = ')[0]: line.split(' = ')[1] for line in lines}

    with open(filename, 'r') as file:
        packet = file.readline().rstrip()

    encoded_str = "".join([dict_hex_bin[c] for c in packet])
    _, _, total_version, final_value = decode_packet(encoded_str, 0)

    print("Sum versions %s" % total_version)
    print("Value %s" % final_value)


if __name__ == "__main__":
    main('day16_input.txt')
