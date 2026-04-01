# Reverse 3

```C
void FUN_001012a4(void)

{
  byte local_48 [16];
  undefined local_38;
  byte local_28 [28];
  int local_c;
  
  local_28[0] = 0xcb;
  local_28[1] = 0xb7;
  local_28[2] = 0xd6;
  local_28[3] = 0xf8;
  local_28[4] = 0xee;
  local_28[5] = 0xb7;
  local_28[6] = 0xf9;
  local_28[7] = 0xb0;
  local_28[8] = 0xdc;
  local_28[9] = 0xf1;
  local_28[10] = 0xf6;
  local_28[0xb] = 0xed;
  local_28[0xc] = 0xed;
  local_28[0xd] = 0xb0;
  local_28[0xe] = 0xf1;
  local_28[0xf] = 0xfe;
  for (local_c = 0; local_c < 0x10; local_c = local_c + 1) {
    local_48[local_c] = local_28[local_c] ^ 0x83;
  }
  local_38 = 0;
  printf("You escaped the maze! Flag: %s\n",local_48);
  return;
}
```

No hay que resolver la mazmorra, solo hay que recuperar la flag
```py
encrypted = [
    0xcb, 0xb7, 0xd6, 0xf8, 0xee, 0xb7, 0xf9, 0xb0,
    0xdc, 0xf1, 0xf6, 0xed, 0xed, 0xb0, 0xf1, 0xfe
]

flag_bytes = [b ^ 0x83 for b in encrypted]
flag = ''.join(chr(b) for b in flag_bytes)
```

`H4U{m4z3_runn3r}`
