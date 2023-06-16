from a_code import code_val

def decode(word: str) -> str:
    x = [*word]
    output = ''
    i = 0
    while i < len(x):
        output += x[i]
        i += code_val
    return output

if __name__ == '__main__':
    word = 'kyqbkabtlaxhldxefrbelhssl'
    print(decode(word))