#!/usr/bin/env python3
from ecdsa.ecdsa import generator_256
from hashlib import sha1
import random, json, sys

welcome = """
  ┌────────────────────┐
  | ┌──(ncsc@ctf)-[~]  |
  | └─$ ./winterfell   |
  |                    |
  |      By Aptx       |
  └────────────────────┘
"""
print(welcome)

FLAG = "Securinets{REDACTED}"

G = generator_256
q = G.order()
d = random.randint(1, q-1)
P = d*G

def inverse(a, b):
        try:
                return pow(a, -1, b)
        except Exception:
                return 0

def ecdsa_sign(msg):
    h = int(sha1(msg.encode()).hexdigest(), 16)
    k = random.randint(1, q-1)
    r = int((k*G).x())
    s = (h + d*r)*inverse(k, q) % q
    return {"s": hex(s), "r": hex(r)}

def ecdsa_verify(msg, s, r):
    h = int(sha1(msg.encode()).hexdigest(), 16)
    u1 = h*inverse(s, q) % q
    u2 = r*inverse(s, q) % q
    T = u1*G + u2*P
    x = int(T.x() or 0)
    if x == r:
        return True
    return False


def main():
        while True:
                print("1 - Sign")
                print("2 - Verify")
                print("3 - Exit")
                c = str(input("> "))

                if c == '1':
                        msg = str(input("Insert your msg : "))
                        if "Winterfell" in msg:
                                print("Sorry, I can't sign this message for you.")
                                sys.exit()

                        sig = ecdsa_sign(msg)
                        print(f"Signature : {json.dumps(sig)}\n")

                elif c == '2':
                        try:
                                msg = str(input("Insert your msg : "))
                                sig = json.loads(input("Insert your signature : "))
                                s = int(sig["s"], 16) % q
                                r = int(sig["r"], 16) % q

                                if ecdsa_verify(msg, s, r):
                                        if msg == "Winterfell":
                                                print(f"Welcome, Sir. Here is your flag {FLAG}\n")
                                        else:
                                                print("Nothing for you!\n")
                                else:
                                        print("Invalid signature.\n")

                        except Exception:
                                print("Invalid input.\n")

                elif c == '3':
                        print("Bye!")
                        sys.exit()

                else:
                        print("Invalid choice.\n")

if __name__ == "__main__":
        main()
