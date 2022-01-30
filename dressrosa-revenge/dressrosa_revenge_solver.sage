from pwn import *

# Solve discrete log problem using Pohlig Hellman

conn = remote("20.127.67.127", 1237)
p = 12278213144366362996470965945939514337273613121169089825041207199059753601704347066047438407223753796160579827236053352219599
g = 2
l_haki = int(conn.recvline().decode().strip().split(" ")[-1])
inv_l_haki = inverse_mod(l_haki, p)

g = Mod(g, p)
inv_l_haki = Mod(inv_l_haki, p)
d_commit = discrete_log(inv_l_haki, g)

conn.sendline(str(d_commit))
print(conn.recvline())