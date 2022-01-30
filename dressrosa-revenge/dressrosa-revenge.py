#!/usr/bin/env python3
from Crypto.Util.number import long_to_bytes
import hashlib, random, sys

welcome = """
  ┌──────────────────────┐
  | ┌──(ncsc@ctf)-[~]    |
  | └─$ ./dressrosa_rev  |
  |                      |
  |        By Aptx       |
  └──────────────────────┘
"""
print(welcome)

FLAG = "Securinets{REDACTED}"

def H(m):
        return hashlib.sha256(long_to_bytes(m)).hexdigest()


def main():
        try:
                p = 12278213144366362996470965945939514337273613121169089825041207199059753601704347066047438407223753796160579827236053352219599
                g = 2

                l_commit = random.randint(2, p-1)
                l_haki = pow(g, l_commit, p)
                Luffy = H(l_haki)
                print(f"Luffy's haki : {l_haki}")

                d_commit = int(input("Doffy's commit : "))
                assert 1 < d_commit < p-1

                d_haki = (pow(g, d_commit, p)*l_haki**2) % p
                Doffy = H(d_haki)

                if Doffy == Luffy:
                        print(f"Supreme King Haki colliding again? {FLAG}")
                else:
                        print("No way! Don Quichotte Doflamingo has been defeated.")

        except Exception:
                print("Error occured.")
                sys.exit()

if __name__ == "__main__":
        main()