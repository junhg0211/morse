table = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ' ': ' ',
    ',': '..-..',
    '.': '.-.-.-',
    '?': '..--..',
    '!': '-.-.--',
    ';': '-.-.-',
    ':': '---...',
    '/': '-..-.',
    '+': '.-.-.',
    '-': '-....-',
    '=': '-...-'
}


def generate(string: str):
    string = string.lower()
    result = ''
    for letter in string:
        result += table[letter]
        result += ' '
    return result


if __name__ == '__main__':
    print(generate('hello, world!'))

