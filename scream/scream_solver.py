from Crypto.Util.number import long_to_bytes
from Crypto.Cipher import AES
from pwn import *

conn = remote("20.127.67.127", 1238)

key = 0
for _ in range(1500):
	print(_)
	conn.recvuntil("> ")
	conn.sendline("2")
	hint = int(conn.recvline().decode().strip().split(" ")[-1])
	key |= hint

key = long_to_bytes(key)

conn.recvuntil("> ")
conn.sendline("1")
enc_flag = bytes.fromhex(conn.recvline().decode().strip().split(" ")[-1])
iv = enc_flag[:16]
enc = enc_flag[16:]
aes = AES.new(key, AES.MODE_CBC, iv)
print(aes.decrypt(enc))