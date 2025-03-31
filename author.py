decode_map = {
    'Ǝ': 'A', '⧖': 'B', '☍': 'C', '⫘': 'D', '▽': 'E', '⨒': 'F', '⨕': 'G', 'φ': 'H',
    '⍽': 'I', '⏚': 'J', '≷': 'K', '⍋': 'L', '𖦹': 'M', '◇': 'N', '山': 'O', '☂': 'P',
    '⍾': 'Q', '⋑': 'R', 'И': 'S', '⊡': 'T', '☊': 'U', '꩜': 'V', '⌶': 'W', '⋈': 'X',
    '∪': 'Y', 'ż': 'Z'
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
