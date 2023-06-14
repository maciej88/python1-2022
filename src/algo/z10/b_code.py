
def decode(word: str) -> str:
    x = [*word]
    output = ''
    i = 0
    while i < len(x):
        output += x[i]
        i += 5
    return output

if __name__ == '__main__':
    word = 'kyqbkabtlaxhldxefrbelhssl'
    print(decode(word))