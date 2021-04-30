import struct
ss=198076
header=struct.pack('i',ss)
print(header)

last=struct.unpack('i',header)[0]
print(last)