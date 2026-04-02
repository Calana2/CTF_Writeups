# Reverse 5

```
=== Virtual Machine Challenge ===
A custom VM protects the flag.
Reverse the bytecode to find the key.

VM Instructions: LOAD(0x01) XOR(0x02) CMP(0x03) JNE(0x04) SUCCESS(0x05) INPUT(0x06) HALT(0xFF)

Bytecode (290 bytes):
06 00 02 00 aa 01 01 e2 03 00 01 04 06 00 02 00
aa 01 01 9e 03 00 01 04 06 00 02 00 aa 01 01 ff
03 00 01 04 06 00 02 00 aa 01 01 d1 03 00 01 04
06 00 02 00 aa 01 01 dc 03 00 01 04 06 00 02 00
aa 01 01 c7 03 00 01 04 06 00 02 00 aa 01 01 f5
03 00 01 04 06 00 02 00 aa 01 01 d8 03 00 01 04
06 00 02 00 aa 01 01 99 03 00 01 04 06 00 02 00
aa 01 01 dc 03 00 01 04 06 00 02 00 aa 01 01 99
03 00 01 04 06 00 02 00 aa 01 01 d8 03 00 01 04
06 00 02 00 aa 01 01 d9 03 00 01 04 06 00 02 00
aa 01 01 99 03 00 01 04 06 00 02 00 aa 01 01 f5
03 00 01 04 06 00 02 00 aa 01 01 99 03 00 01 04
06 00 02 00 aa 01 01 c4 03 00 01 04 06 00 02 00
aa 01 01 cd 03 00 01 04 06 00 02 00 aa 01 01 9b
03 00 01 04 06 00 02 00 aa 01 01 c4 03 00 01 04
06 00 02 00 aa 01 01 99 03 00 01 04 06 00 02 00
aa 01 01 99 03 00 01 04 06 00 02 00 aa 01 01 d8
03 00 01 04 06 00 02 00 aa 01 01 d7 03 00 01 04
05 ff

Enter the key (24 chars):
```

La VM carga la entrada, aplica XOR con un byte fijo y compara la salida con un resultado esperado, si extraemos key ^ correct_byte para cada byte entonces obtenemos la clave correcta:
```
import string


bytecode = "06 00 02 00 aa 01 01 e2 03 00 01 04 06 00 02 00 aa 01 01 9e 03 00 01 04 06 00 02 00 aa 01 01 ff 03 00 01 04 06 00 02 00 aa 01 01 d1 03 00 01 04 06 00 02 00 aa 01 01 dc 03 00 01 04 06 00 02 00 aa 01 01 c7 03 00 01 04 06 00 02 00 aa 01 01 f5 03 00 01 04 06 00 02 00 aa 01 01 d8 03 00 01 04 06 00 02 00 aa 01 01 99 03 00 01 04 06 00 02 00 aa 01 01 dc 03 00 01 04 06 00 02 00 aa 01 01 99 03 00 01 04 06 00 02 00 aa 01 01 d8 03 00 01 04 06 00 02 00 aa 01 01 d9 03 00 01 04 06 00 02 00 aa 01 01 99 03 00 01 04 06 00 02 00 aa 01 01 f5 03 00 01 04 06 00 02 00 aa 01 01 99 03 00 01 04 06 00 02 00 aa 01 01 c4 03 00 01 04 06 00 02 00 aa 01 01 cd 03 00 01 04 06 00 02 00 aa 01 01 9b 03 00 01 04 06 00 02 00 aa 01 01 c4 03 00 01 04 06 00 02 00 aa 01 01 99 03 00 01 04 06 00 02 00 aa 01 01 99 03 00 01 04 06 00 02 00 aa 01 01 d8 03 00 01 04 06 00 02 00 aa 01 01 d7 03 00 01 04 05 ff"

stack = []

def vm_machine(bytecode,input):
    bc = bytes.fromhex(bytecode)
    pc = 0
    idx = 0
    reg = [0] * 12
    flag = 1
    input_idx = 0
    key = []

    while pc < len(bc):
        op = bc[pc]

        if op > 6:
            if op == 0xff:
                return flag
            return 0
        
        if op == 0:
            return 0

        idx = pc + 1

        if op == 0x01:      # LOAD
            reg[bc[idx]]  = bc[pc + 2]
            pc += 3

        elif op == 0x02:    # XOR
            reg[bc[idx]] = reg[bc[idx]] ^ bc[pc + 2]
            key.append(reg[bc[idx]])
            pc += 3

        elif op == 0x03:    # CMP
            reg_idx1 = bc[idx]
            reg_idx2 = bc[pc + 2]
            if reg[reg_idx1] != reg[reg_idx2]:
                # NEXT
                return chr(reg[reg_idx2] ^ 0xaa)
            flag = flag and (reg[reg_idx1] == reg[reg_idx2])
            pc += 3

        elif op == 0x04:    # JNE
            pc = idx;
            if flag == 0:
                return 0

        elif op == 0x05:    # SUCCESS
            return 1

        elif op == 0x06:    # INPUT
            op = bc[idx]
            val = 0
            if input_idx < len(input):
                val = ord(input[input_idx])
                input_idx += 1
            reg[op] = val
            pc += 2

    return 0


if __name__ == "__main__":
    msg = "H4U{"
    for _ in range(20):
        r = vm_machine(bytecode,msg)
        msg += r
    print(msg)
```

`H4U{vm_r3v3rs3_3ng1n33r}`
