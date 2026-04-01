# Reverse 1

```
$ ltrace ./crackme
puts("=== CrackMe v1.0 ==="=== CrackMe v1.0 ===
)                 = 21
printf("Enter the password: ")               = 20
fgets(Enter the password: givemeflag
"givemeflag\n", 256, 0x7fc54fa278e0)   = 0x7ffdbd129300
strcspn("givemeflag\n", "\n")                = 10
strlen("H4U{cr4ck_m3_1f_y0u_c4n}")           = 24
strncpy(0x7ffdbd129270, "cr4ck_m3_1f_y0u_c4n", 19) = 0x7ffdbd129270
strcmp("givemeflag", "cr4ck_m3_1f_y0u_c4n")  = 4
puts("Wrong password. Try harder!"Wrong password. Try harder!
)          = 28
+++ exited (status 0) +++
```

`H4U{cr4ck_m3_1f_y0u_c4n}`
