decode_map = {
    '❌': 'A', '@': 'B', '✋🏻': 'C', '⭐': 'D', '💲': 'E', '🧨': 'F', '🌪️': 'G', '💣': 'H',
    '⚡': 'I', '🦴': 'J', '⚓': 'K', '*': 'L', '🌒': 'M', '💀': 'N', '❓': 'O', '🌲': 'P',
    '⚛️': 'Q', '&': 'R', '#': 'S', '⛵': 'T', '🗡️': 'U', '%': 'V', '👓': 'W', '🪐': 'X',
    '❗': 'Y', '🌀': 'Z'
}

encode_map = {v: k for k, v in decode_map.items()}


def translate(encoded_text):
    return ''.join(decode_map.get(char, char) for char in encoded_text)


def encrypt(text):
    return ''.join(encode_map.get(char.upper(), char) for char in text)


if __name__ == "__main__":
    mode = input("Введіть 0 для розшифрування або 1 для шифрування: ")
    text = input("Введіть текст: ")

    if mode == "0":
        print("Розшифрований текст:", translate(text))
    elif mode == "1":
        print("Зашифрований текст:", encrypt(text))
