# Reverse 4

```C
void FUN_001012ae(long param_1)

{
  int local_c;
  
  for (local_c = 0; local_c < 0x17; local_c = local_c + 1) {
    *(byte *)(param_1 + local_c) = (&DAT_001040c0)[lo cal_c] ^ DAT_001040d7;
  }
  *(undefined *)(param_1 + 0x17) = 0;
  return;
}
```

No hay que adivinar, solo recuperar la flag:
```py
encrypted = [
    0xed, 0x91, 0xf0, 0xde, 0xd3, 0x91, 0xd0, 0xc9,
    0xd1, 0xfa, 0xc6, 0xd7, 0x91, 0xc6, 0xce, 0x96,
    0xc1, 0xfa, 0xc2, 0x95, 0x95, 0xc1, 0xd8
]
key = 0xa5
flag_bytes = [b ^ key for b in encrypted]
flag = ''.join(chr(b) for b in flag_bytes)

print(f"Flag: {flag}")
```

`H4U{v4ult_cr4ck3d_g00d}`
