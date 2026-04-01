# Reverse 6

```
$ file crackme.pyc
crackme.pyc: Byte-compiled Python module for CPython 3.12 or newer, timestamp-based, .py timestamp: Tue Mar 24 20:55:00 2026 UTC, .py size: 572 bytes
```

Lo subimos a https://pylingual.io/ para recuperar el codigo Python:
```py
def scramble(s):
    out = []
    for i, c in enumerate(s):
        out.append(ord(c) ^ i + 19)
    return out
def check(user_input):
    expected = [99, 109, 97, 126, 39, 118, 70, 120, 98, 104, 46, 125, 47, 68, 18, 125, 81, 23, 83]
    s = scramble(user_input)
    return s == expected and len(user_input) == len(expected)
if __name__ == '__main__':
    print('=== Python CrackMe ===')
    user_key = input('Enter the key: ')
    if check(user_key):
        flag = 'H4U{' + user_key + '}'
        print('Correct! Flag:', flag)
    else:
        print('Wrong key.')
```

Hacemos las operaciones inversas a `scramble`:
```py
def scramble(s):
    out = []
    for i, c in enumerate(s):
        out.append(ord(c) ^ i + 19)
    return out
def check(user_input):
    expected = [99, 109, 97, 126, 39, 118, 70, 120, 98, 104, 46, 125, 47, 68, 18, 125, 81, 23, 83]
    s = scramble(user_input)
    return s == expected and len(user_input) == len(expected)

def unscramble(scrambled_list):
    out = []
    for i, val in enumerate(scrambled_list):
        # Reverse: val = ord(c) ^ (i + 19)
        # So ord(c) = val ^ (i + 19)
        original_char = chr(val ^ (i + 19))
        out.append(original_char)
    return ''.join(out)

if __name__ == '__main__':
    u=unscramble([99, 109, 97, 126, 39, 118, 70, 120, 98, 104, 46, 125, 47, 68, 18, 125, 81, 23, 83])
    print(u)
```

`H4U{pyth0n_byt3c0d3_r3v}
