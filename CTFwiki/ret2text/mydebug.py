from pwn import *

class debug:

    # # debug mode or real environment mode
    # # debug mode: the breakpoint addr will translate to the real addr by add the base
    # # real environment mode: if PIE is not enable, the addr you see in IDA is the real addr
    # DEBUG = True

    wordSz = 4
    hwordSz = 2
    bits = 32
    PIE = 0
    mypid=0
    
    # ''' 
    # set debug mode or not
    # Arg: 
    #     value:
    #          True for debug mode
    #          False for real environment mode 
    # '''
    # def set_debug(self, value):
    #     DEBUG = value

    def leak(self, address, size):
        with open('/proc/%s/mem' % mypid) as mem:
            mem.seek(address)
            return mem.read(size)

    def findModuleBase(self, pid, mem):
        name = os.readlink('/proc/%s/exe' % pid)
        with open('/proc/%s/maps' % pid) as maps:
            for line in maps:
                if name in line:
                    addr = int(line.split('-')[0], 16)
                    mem.seek(addr)
                    if mem.read(4) == "\x7fELF":
                        bitFormat = u8(self.leak(addr + 4, 1))
                        if bitFormat == 2:
                            global wordSz
                            global hwordSz
                            global bits
                            wordSz = 8
                            hwordSz = 4
                            bits = 64
                        return addr
        log.failure("Module's base address not found.")
        sys.exit(1)

    '''
    if ASLR is open, this function can set the breakpoint on the real addr by searching the program base in the /proc/***/maps file
    Args:
        p: the handler
        addr: the addr you want to set a breakpoint
    '''
    def dbg(self, p, addr): 
        global mypid
        mypid = proc.pidof(p)[0]
        with open('/proc/%s/mem' % mypid) as mem:
            moduleBase = self.findModuleBase(mypid, mem)
            print "program_base",hex(moduleBase)
            gdb.attach(p, "set follow-fork-mode parent\nb *" + hex(moduleBase+addr))

