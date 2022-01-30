#!/usr/bin/env python3
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import sys, os

welcome = """
  ┌────────────────────┐
  | ┌──(ncsc@ctf)-[~]  |
  | └─$ ./crash-ba$h   |
  |                    |
  |      By Aptx       |
  └────────────────────┘
"""
print(welcome)

key = os.urandom(16)
iv = os.urandom(16)
root_proof = os.urandom(16).hex()

def execute_cmd(sig):
    try:
        aes = AES.new(key, AES.MODE_CBC, iv)
        exec_cmd = unpad(aes.decrypt(sig), 16)

        exec_cmd = exec_cmd.split(b' : ')
        cmd = exec_cmd[1].decode()
        proof = exec_cmd[2].decode()

        if proof == root_proof:
            os.system(cmd)

    except Exception:
        print("Invalid signature.\n")

def sign_cmd(cmd):
        msg = os.urandom(16) + b" : " + cmd.encode() + b" : " + root_proof.encode()
        aes = AES.new(key, AES.MODE_CBC, iv)
        sig = aes.encrypt(pad(msg, 16))
        return sig

def available_cmds():
    cmds = ['ls -l', 'pwd']
    for cmd in cmds:
        print(f"{cmd} : {sign_cmd(cmd).hex()}")


def main():
    while True:
        print("1 - Show available commands")
        print("2 - Execute command")
        print("3 - Exit")
        c = str(input("> "))

        if c == '1':
            available_cmds()
            print()

        elif c == '2':
            try:      
                sig = bytes.fromhex(input("Insert your command : "))
            except Exception:
                print("Invalid input.\n")

            execute_cmd(sig)
            print()

        elif c == '3':
            print("Bye!")
            sys.exit()

        else:
            print("Invalid choice.\n")

if __name__ == "__main__" :
    main()