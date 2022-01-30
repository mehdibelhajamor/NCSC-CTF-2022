#!/usr/bin/env python3
from Crypto.Util.number import long_to_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import sys, os

welcome = """
  ┌────────────────────┐
  | ┌──(ncsc@ctf)-[~]  |
  | └─$ ./scream       |
  |                    |
  |      By Aptx       |
  └────────────────────┘
"""
print(welcome)

FLAG = "Securinets{REDACTED}"

key = os.urandom(16)
iv = os.urandom(16)

def encrypt(msg):
        msg = pad(msg.encode(), 16)
        aes = AES.new(key, AES.MODE_CBC, iv)
        enc = aes.encrypt(msg)
        return iv + enc

def hint(key):
        taps = [int(os.urandom(16).hex(), 16) for _ in range(8)]
        h = int(key.hex(), 16)
        for tap in taps:
                h &= tap
        return h


def main():
    while True:
        print("1 - Get encrypted flag")
        print("2 - Get hint")
        print("3 - Exit")
        c = str(input("> "))

        if c == '1':
            print(f"Encrypted flag : {encrypt(FLAG).hex()}\n")

        elif c == '2':
            print(f"Hint : {hint(key)}\n")

        elif c == '3':
            print("Bye!")
            sys.exit()

        else:
            print("Invalid choice.\n")

if __name__ == "__main__" :
    main()