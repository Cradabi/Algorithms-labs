def crc(values, poly):
    values = ''.join([f'{ord(j):08b}' for j in [i for i in values]]) + '0' * 32
    ptype = '0' + str(32) + 'b'
    poly = '1' + f'{int(poly, 16):{ptype}}'
    i = 0
    while i < len(values) - 32:
        if values[i] == '1':
            tmp = int(values[i:i + 33], 2) ^ int(poly, 2)
            values = values[:i] + f'{tmp:{ptype}}' + values[i + 33:]
            i = 0
            continue
        i += 1
    return hex(int(values, 2))


poly = '0x04C11DB7'
n = input()
print(crc(n, poly))