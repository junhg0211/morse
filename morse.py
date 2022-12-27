import numpy as np
from pyaudio import PyAudio, paFloat32

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
    ' ': '/',
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
    overline = False

    for letter in string:
        if letter == '`':
            if overline:
                overline = False
                result += ' '
            else:
                overline = True
            continue

        result += table[letter]

        if not overline:
            result += ' '
    return result


SAMPLING_RATE = 44100
FREQUENCY = 660
VOLUME = 0.5
WPM = 90


def generate_sin(
        duration: float,
        frequency: float = FREQUENCY,
        volume: float = VOLUME,
        sampling_rate: int = SAMPLING_RATE
):
    samples = np.sin(2 * np.pi * np.arange(sampling_rate * duration) * frequency / sampling_rate)\
        .astype(np.float32)

    return (volume * samples).tobytes()


def generate_silence(duration: float, sampling_rate: int = SAMPLING_RATE):
    samples = np.zeros(int(sampling_rate * duration)).astype(np.float32)
    return samples.tobytes()


def write_audio(stream, string: str, unit: float, function=None):
    if function is None:
        function = stream.write

    for letter in generate(string):
        if letter == '.':
            function(generate_sin(unit))
        elif letter == '-':
            function(generate_sin(3 * unit))
        elif letter == ' ':
            function(generate_silence(2 * unit))
        elif letter == '/':
            function(generate_silence(unit))
        function(generate_silence(unit))


WORD_LENGTH = 48


def play_morse(string: str, wpm: int = WPM):
    p = PyAudio()

    stream = p.open(format=paFloat32,
                    channels=1,
                    rate=SAMPLING_RATE,
                    output=True)

    unit = 1 / (WORD_LENGTH/60 * wpm)
    write_audio(stream, string, unit)

    stream.stop_stream()
    stream.close()

    p.terminate()


if __name__ == '__main__':
    message = '`bt`'
    print(generate(message))
    play_morse(message, 20)
