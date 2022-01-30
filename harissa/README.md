#### Challenge script :
```python
#!/usr/bin/env python3
from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes, inverse, GCD
import sys

welcome = """
  ┌────────────────────┐
  | ┌──(ncsc@ctf)-[~]  |
  | └─$ ./haRiSsA      |
  |                    |
  |      By Aptx       |
  └────────────────────┘
"""
print(welcome)

FLAG = "Securinets{REDACTED}"

while True:
        p, q = getPrime(512), getPrime(512)
        n = p*q
        phi = (p-1)*(q-1)
        e = 65537
        if GCD(e, phi) == 1:
                d = inverse(e, phi)
                break


def main():
        while True:
                print("1 - Sign")
                print("2 - Vote")
                print("3 - Exit")
                c = str(input("> "))

                if c == '1':
                        try:
                                msg = bytes.fromhex(input("Insert your msg : "))
                                if b"I vote for Cha3b Harissa" in msg:
                                        print("Sorry, I can't sign this message for you.")
                                        sys.exit()

                                m = bytes_to_long(msg)
                                assert 1 < m < 2**128

                                s = pow(m, d, n)
                                print(f"Vote : {hex(s)}\n")

                        except Exception:
                                print("Invalid input.\n")

                elif c == '2':
                        try:
                                vote = int(input("Insert your vote : "), 16) % n
                                verified = long_to_bytes(pow(vote, e, n))

                                if verified == b"I vote for Cha3b Harissa":
                                        print(f"Vote is done. Here is your flag {FLAG}\n")
                                else:
                                        print("You should vote for Cha3b Harissa!\n")

                        except Exception:
                                print("Invalid input.\n")

                elif c == '3':
                        print("Bye!")
                        sys.exit()

                else:
                        print("Invalid choice.\n")

if __name__ == "__main__":
        main()
```
