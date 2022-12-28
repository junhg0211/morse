from random import choice
from time import sleep

from morse import generate, play_morse

WORDS = [
    'the', 'of', 'and', 'a', 'to', 'in', 'is', 'you', 'that', 'it', 'he', 'was',
    'for', 'on', 'are', 'as', 'with', 'his', 'they', 'i', 'at', 'be', 'this', 'have',
    'from', 'or', 'one', 'had', 'by', 'word', 'but', 'not', 'what', 'all', 'were',
    'we', 'when', 'your', 'can', 'said', 'there', 'use', 'an', 'each', 'which', 'she',
    'do', 'how', 'their', 'if', 'will', 'up', 'other', 'about', 'out', 'many', 'then',
    'them', 'these', 'so', 'some'
]


def main():
    word = choice(WORDS)
    morse_code = generate(word)

    play_morse(morse_code, 30)
    sleep(5)

    play_morse(morse_code, 15)
    sleep(2)

    print(morse_code)
    sleep(3)

    print(word)


if __name__ == '__main__':
    main()
