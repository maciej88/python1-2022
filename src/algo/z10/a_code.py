import string, random
from random import choice

code_val = 4
def encode(word: str) -> str:
    x = [*word]
    output = ''
    i = 0
    while i < len(x):
        z = ''.join(choice(string.ascii_lowercase) for _ in range(code_val))
        res = f'{x[i]}{z}{x[i]}'
        i += 1
        output += res
    return output


if __name__ == '__main__':
    words = 'kaxel'
    print(encode(words))
