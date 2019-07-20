def get_index_different_char(chars):
    alpha_num = []
    characters = []
    chars = [str(char) for char in chars]
    for char in chars:
        if char.isdigit() or char.isalpha():
            alpha_num.append(char)
        else:
            characters.append(char)
    if len(alpha_num) > len(characters):
        return chars.index(characters[0])
    else:
        return chars.index(alpha_num[0])
