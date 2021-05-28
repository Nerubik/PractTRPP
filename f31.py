import struct

A_SIZE = 00
B_SIZE = 00
C_SIZE = 00
D_SIZE = 6 + 8*3 + 8 + 8
E_SIZE = 1 + 2 + 4 + 4 + 4

def parse_e(offset, bytes):
    e_bytes = bytes[offset:offset + E_SIZE]
    e_parced = struct.unpack('BhIII', e_bytes)
    e3_bytes = bytes[e_parced[3]:e_parced[3] + e_parced[2]]
    e3_parced = struct.unpack('q' * e_parced[2], e3_bytes)
    return {'E1': e_parced[0],
            'E2': e_parced[1],
            'E3': list(e3_parced),
            'E4': e_parced[4]}
def parce_d(offset, bytes):
    d_bytes = bytes[offset:offset + D_SIZE]
    d_parced = struct.unpack()