from Crypto.Util.number import long_to_bytes
from pwn import *

# factors of "I vote for Cha3b Harissa"
factors = [3, 11, 19, 251, 503, 474060765215282981, 47780705009814237402688533849691]

conn = remote("20.127.67.127", 1234)

msg = 1
for factor in factors:
	conn.recvuntil("> ")
	conn.sendline("1")
	conn.sendline(long_to_bytes(factor).hex())
	vote = int(conn.recvline().decode().strip().split(" ")[-1], 16)
	msg *= vote

conn.recvuntil("> ")
conn.sendline("2")
conn.sendline(hex(msg))
print(conn.recvline())