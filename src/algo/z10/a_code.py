import string, random
from random import choice

code_val = 1
def encode(word: str) -> str:
    x = [*word]
    output = ''
    i = 0
    while i < len(x):
        z = ''.join(choice(string.ascii_lowercase) for _ in range(3))
        res = f'{x[i]}{z}{x[i]}'
        i += code_val
        output += res
    return output


if __name__ == '__main__':
    words = 'kaxel'
    print(encode(words))
