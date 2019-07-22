import string, random

ALPHABET = string.ascii_uppercase + string.digits


def gen_key(parts=4, chars_per_part=8):
    join = ''.join
    keylist = []
    add = keylist.append
    while len(keylist) < parts:
        part_key = join(random.choices(ALPHABET, k=chars_per_part))
        add(part_key)
    return '-'.join(i for i in keylist)