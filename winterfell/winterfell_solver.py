from pwn import *
import json

# https://research.nccgroup.com/2021/11/08/technical-advisory-arbitrary-signature-forgery-in-stark-bank-ecdsa-libraries/

conn = remote("20.127.67.127", 1236)

conn.recvuntil("> ")
conn.sendline("2")
conn.sendline("Winterfell")
signature = '{"s": "0x0", "r": "0x0"}'
conn.sendline(signature)
print(conn.recvline())