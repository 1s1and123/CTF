import mydebug
from pwn import *

def pwn():
    p = process("./ret2text")
    a = mydebug.debug()
    a.dbg(p,0x5af)
    p.recvline()
    p.send('jjhh')
    #print payload
    #p.sendline(payload)
    p.interactive()
   

if __name__ == '__main__':
   pwn()
