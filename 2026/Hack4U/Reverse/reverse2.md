# Reverse 2

```
$ ltrace ./obfuscated
signal(SIGTRAP, 0x562508da82a0)                  = 0
ptrace(0, 0, 0, 0)                               = -1
puts("Nice try, debugger detected!"Nice try, debugger detected!
)             = 29
+++ exited (status 1) +++
```

El programa tiene dos tecnicas anti-debugging: Un signal handler para SIGTRAP (0x000010d5) y un checker para PTRACE_TRACEME (0x000010dc)
```
[0x000010c0]> pdf
            ;-- section..text:
            ; DATA XREF from entry0 @ 0x11b4(r)
/ 218: int main (int argc, char **argv, char **envp);
|           0x000010c0      55             push rbp                    ; [14] -r-x section size 1286 named .text
|           0x000010c1      488d35d801..   lea rsi, [0x000012a0]       ; void *func
|           0x000010c8      bf05000000     mov edi, 5                  ; int sig
|           0x000010cd      53             push rbx
|           0x000010ce      4881ec0801..   sub rsp, 0x108
|           0x000010d5      e8a6ffffff     call sym.imp.signal         ; void signal(int sig, void *func)
|           0x000010da      31c0           xor eax, eax
|           0x000010dc      e8cf010000     call fcn.000012b0
...
[0x000010c0]> pdf @fcn.000012b0
            ; CALL XREF from main @ 0x10dc(x)
/ 34: fcn.000012b0 ();
|           0x000012b0      4883ec08       sub rsp, 8
|           0x000012b4      31c9           xor ecx, ecx                ; void*data
|           0x000012b6      31d2           xor edx, edx                ; void*addr
|           0x000012b8      31f6           xor esi, esi                ; pid_t pid
|           0x000012ba      31ff           xor edi, edi                ; __ptrace_request request
|           0x000012bc      31c0           xor eax, eax
|           0x000012be      e8cdfdffff     call sym.imp.ptrace         ; long ptrace(__ptrace_request request, pid_t pid, void*addr, void*data)
|           0x000012c3      4883f8ff       cmp rax, 0xffffffffffffffff
|           0x000012c7      0f94c0         sete al
|           0x000012ca      4883c408       add rsp, 8
|           0x000012ce      0fb6c0         movzx eax, al
\           0x000012d1      c3             ret
```

Si patcheamos el binario, omitiendo estas llamadas podemos depurarlo:
```
[0x000010c0]> s 0x000010d5
[0x000010d5]> wx 9090909090
[0x000010d5]> s 0x000010dc
[0x000010dc]> wx 9090909090
[0x000010c0]> s main
[0x000010c0]> pd 20
            ;-- section..text:
            ;-- main:
            0x000010c0      55             push rbp                    ; [14] -r-x section size 1286 named .text
            0x000010c1      488d35d801..   lea rsi, [0x000012a0]
            0x000010c8      bf05000000     mov edi, 5
            0x000010cd      53             push rbx
            0x000010ce      4881ec0801..   sub rsp, 0x108
            0x000010d5      90             nop
            0x000010d6      90             nop
            0x000010d7      90             nop
            0x000010d8      90             nop
            0x000010d9      90             nop
            0x000010da      31c0           xor eax, eax
            0x000010dc      90             nop
            0x000010dd      90             nop
            0x000010de      90             nop
            0x000010df      90             nop
            0x000010e0      90             nop
            0x000010e1      85c0           test eax, eax
```

Con un breakpoint en la posicion donde se comparan las cadenas se puede recuperar la flag:
```
[0x55fbd66a1596]> px 32@  0x7ffc3d49fd20
- offset -      2021 2223 2425 2627 2829 2A2B 2C2D 2E2F  0123456789ABCDEF
0x7ffc3d49fd20  4834 557b 3062 6675 7363 3474 3364 5f34  H4U{0bfusc4t3d_4
0x7ffc3d49fd30  6e64 5f70 7230 7433 6374 3364 7d00 0000  nd_pr0t3ct3d}...
[0x55fbd66a1596]>
```

`H4U{0bfusc4t3d_4nd_pr0t3ct3d}`
