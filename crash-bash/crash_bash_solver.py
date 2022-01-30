from pwn import *

# AES Bit Flip Attack

conn = remote("20.127.67.127", 1235)

conn.recvuntil("> ")
conn.sendline("1")
ls_cmd_sign = bytes.fromhex(conn.recvline().decode().strip().split(" ")[-1])

block_1 = list(ls_cmd_sign[:16])
block_1[3] = block_1[3] ^ ord("l") ^ ord("c")
block_1[4] = block_1[4] ^ ord("s") ^ ord("a")
block_1[5] = block_1[5] ^ ord(" ") ^ ord("t")
block_1[6] = block_1[6] ^ ord("-") ^ ord(" ")
block_1[7] = block_1[7] ^ ord("l") ^ ord("*")

new_block_1 = ''.join(map(chr, block_1)).encode('latin-1')

cat_cmd_sign = new_block_1 + ls_cmd_sign[16:]
conn.recvuntil("> ")
conn.sendline("2")
conn.sendline(cat_cmd_sign.hex())
conn.interactive()