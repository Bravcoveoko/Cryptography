import re
import math

# DONE
def caesar_cipher(decrypt, text, key):
    result = ""
    if decrypt:
        for index in range(len(text)):
            result += chr(((ord(text[index]) - int(key)) % 65 ) + 65)
    else:
        for index in range(len(text)):
            result += chr(((ord(text[index]) + int(key)) % 65 ) + 65)

    print(result)

# DONE
def albam_cipher(text):
    text = text.upper()
    result = ""
    for index in range(len(text)):
        character = text[index]

        if character == ' ':
            continue

        result += chr(ord(character) + 13) if ord(character) + 13 <= 90 else chr(ord(character) - 13)
    print(result)

# DONE
def atbash_cipher(text):
    text = text.upper()
    result = ""
    for index in range(len(text)):
        character = text[index]

        if character == ' ':
            continue

        diff = (ord(character) + 25) - 90
        result += chr(90 - diff)
    print(result)

def _remove_duplicate(text):
    seen = set()
    result = ''.join([x for x in text if not (x in seen or seen.add(x))])
    return result

def _add_alphabet_letters(text, w):
    result = text
    result += "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if w else "ABCDEFGHIJKLMNOPQRSTUVXYZ"
    return result

def _create_dict(modified_key, decrypt):
    d = dict()

    if decrypt:
        for pos in range(26):
            d.update({modified_key[pos] : "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[pos]})
    else:
        for pos in range(26):
            d.update({"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[pos] : modified_key[pos]})

    return d


# DONE
def substitution_cipher(decrypt, text, key):
    modified_key = _remove_duplicate(_add_alphabet_letters(key, True))

    dic = _create_dict(modified_key, decrypt)
    result = ""

    for char in text:
        result += dic[char]


    print(result)

def _create_vigener_table():
    matrix = []
    alphabet = [chr(x) for x in range(65, 91)]

    for index in range(0, 26):
        newAlp = ''.join(alphabet)
        matrix.append(newAlp)

        c = alphabet.pop(0)
        alphabet.append(c)

    return matrix

def _create_extended_text(text, key):
    
    decimal = len(text) // len(key)
    modulo = len(text) % len(key)

    buffered_text = ""

    for i in range(decimal):
        buffered_text += key

    buffered_text += key[:modulo] if modulo > 0 else ""

    return buffered_text


# DONE
def napoleon_cipher(text, key):
    napoleon_table = {
        'A' : "ABCDEFGHIJKLM",
        'B' : "NOPQRSTUVWXYZ",
        'C' : "ABCDEFGHIJKLM",
        'D' : "OPQRSTUVWXYZN",
        'E' : "ABCDEFGHIJKLM",
        'F' : "PQRSTUVWXYZNO",
        'G' : "ABCDEFGHIJKLM",
        'H' : "QRSTUVWXYZNOP",
        'I' : "ABCDEFGHIJKLM",
        'J' : "RSTUVWXYZNOPQ",
        'K' : "ABCDEFGHIJKLM",
        'L' : "STUVWXYZNOPQR",
        'M' : "ABCDEFGHIJKLM",
        'N' : "TUVWXYZNOPQRS",
        'O' : "ABCDEFGHIJKLM",
        'P' : "UVWXYZNOPQRST",
        'Q' : "ABCDEFGHIJKLM",
        'R' : "VWXYZNOPQRSTU",
        'S' : "ABCDEFGHIJKLM",
        'T' : "WXYZNOPQRSTUV",
        'U' : "ABCDEFGHIJKLM",
        'V' : "XYZNOPQRSTUVW",
        'W' : "ABCDEFGHIJKLM",
        'X' : "YZNOPQRSTUVWX",
        'Y' : "ABCDEFGHIJKLM",
        'Z' : "ZNOPQRSTUVWXY"
    }

    

    buffered_text = _create_extended_text(text, key)
    length = len(buffered_text)

    result = ""

    for index in range(length):
        c1 = text[index] #G
        c2 = buffered_text[index] #P

        position = napoleon_table[c2].find(c1)
        is_even = ord(c2) % 2 == 0

        if position == -1:
            if is_even:
                tup = (napoleon_table[chr(ord(c2) - 1)].find(c1), chr(ord(c2)))
            else:
                tup = (napoleon_table[chr(ord(c2) + 1)].find(c1), chr(ord(c2)))
        else:
            if is_even:
                tup = (napoleon_table[c2].find(c1), chr(ord(c2) - 1))
            else:
                tup = (napoleon_table[c2].find(c1), chr(ord(c2) + 1))

        result += napoleon_table[tup[1]][tup[0]]

    print(result)

# DONE
def vigener_cipher(decrypt, text, key):
    vigener_table = _create_vigener_table()
    buffered_text = _create_extended_text(text, key)

    length = len(text)
    result = ""

    if decrypt:
        for index in range(length):
            letterText = text[index]
            letterKey = buffered_text[index]

            new_index = ord(letterKey) % 65

            for sentance in vigener_table:
                if sentance[new_index] == letterText:
                    result += sentance[0]
    else:
        for index in range(length):
            letterText = text[index]
            letterKey = buffered_text[index]

            new_index = ord(letterKey) % 65

            sentance = vigener_table[ord(letterText) % 65]

            result += sentance[new_index]


    print(result)


def _create_square(key):
    matrix = []

    buffered_text = _remove_duplicate(_add_alphabet_letters(key, False))

    for _ in range(5):
        matrix.append(buffered_text[:5])
        buffered_text = buffered_text[5:]

    for line in matrix:
        print(line)

    return matrix

# DONE
def polybius_cipher(decrypt, text, key):
    polybius_square = _create_square(key)

    result = ""

    if decrypt:

        tuples = [(ord(text[i : i + 1]) - 48, ord(text[i + 1 : i + 2]) - 48) for i in range(0, len(text), 2)]

        for tup in tuples:
            row, column = tup

            result += polybius_square[row - 1][column - 1]
    else:

        for character in text:
            for row in range(len(polybius_square)):
                column = polybius_square[row].find(character)
                if column != -1:
                    result += str(row + 1) + str(column + 1)
                    break

    print(result)


def _modify_text(text):
    match =  re.search(r"(.)\1", text)

    while ( match != None ):
        start, end = match.span()

        text = text.replace(text[start : end], (text[start] + 'X' + text[end - 1]))
        match =  re.search(r"(.)\1", text)

    if len(text) % 2 == 1:  text += 'X'

    return text

# DONE
def playfair_cipher(decrypt, text, key):
    playfair_square = _create_square(key)

    count = len(playfair_square)

    modified_text = _modify_text(text)

    tuples = [(text[i : i + 1], text[i + 1 : i + 2]) for i in range(0, len(text), 2)]
    result = ""

    for tup in tuples:
        letter1, letter2 = tup

        # Find x,y positions
        for index in range(count):
            sentance = playfair_square[index]

            if sentance.find(letter1) != -1:
                pos1 = (index, sentance.find(letter1))

            if sentance.find(letter2) != -1:
                pos2 = (index, sentance.find(letter2))

        # Rules

        if decrypt:

            if pos1[0] == pos2[0]:
                result += playfair_square[pos1[0]][pos1[1] - 1]
                result += playfair_square[pos2[0]][pos2[1] - 1]

            elif pos1[1] == pos2[1]:
                result += playfair_square[pos1[0] - 1][pos1[1]]
                result += playfair_square[pos2[0] - 1][pos2[1]]

            else:
                result += playfair_square[pos1[0]][pos2[1]]
                result += playfair_square[pos2[0]][pos1[1]]

        else:
            if pos1[0] == pos2[0]:
                result += playfair_square[pos1[0]][(pos1[1] + 1) % 5]
                result += playfair_square[pos2[0]][(pos2[1] + 1) % 5]

            elif pos1[1] == pos2[1]:
                result += playfair_square[(pos1[0] + 1) % 5][pos1[1]]
                result += playfair_square[(pos2[0] + 1) % 5][pos2[1]]

            else:
                result += playfair_square[pos1[0]][pos2[1]]
                result += playfair_square[pos2[0]][pos1[1]]


    print(result)

# DONE
def one_time_pad(text, key):

    result = [ chr( ((ord(a) + ord(b) - 130) % 26) + 65) for (a, b) in tuple(zip(text, key)) ]

    result = ''.join(result)

    print(result)


def _split_text(text, length):
    matrix = []
    mod = len(text) % length
    count = (len(text) // length) + (1 if mod != 0 else 0)

    for _ in range(count):
        matrix.append(text[:length])

        text = text[length:]

    matrix[count - 1] = matrix[count - 1] + (' ' * (length - mod))

    return matrix

def _mark_letters(key):

    ordinals = list(map(lambda x : ord(x), [*key]))

    length = len(ordinals)
    arr = [None for _ in range(length)]

    mark = 1
    for _ in range(length):
        mIndex =  ordinals.index(min(ordinals))
        arr[mIndex] = mark
        mark += 1

        ordinals[mIndex] = math.inf

    return arr


def _make_groups(tuples, index):
    length = len(index)

    arr = [["", 0, 0] for _ in range(length)]

    ind = 0
    for i in index:
        ind += 1
        for (c, v) in tuples:
            if v == i:
                arr[i - 1][0] += c
                arr[i - 1][1] = ind
                arr[i - 1][2] = i

    return arr

def richelieu_cipher(decrypt, text, key):
    length_key = len(key)

    marked = _mark_letters(key)

    split_text = _split_text(text, length_key)

    if decrypt:
        tuples = []
        index = 0
        for word in split_text:
            tuples += [*zip(word, marked)]

        groups = _make_groups(tuples, marked)

        groups.sort(key=lambda x: x[1])

        res = [None for _ in range(length_key)]

        for i in range(length_key):
            n = groups[i][2] - 1

            for g in range(length_key):
                if i == groups[g][2] - 1:
                    res[groups[g][1] - 1] = groups[i]


        result = ""

        div = (len(text) // len(key)) + (1 if len(text) % len(key) != 0 else 0)

        for i in range(div):
            for word in res:
                result += word[0][i]
    else:
        tuples = []
        index = 0
        for word in split_text:
            tuples += [*zip(word, marked)]

        groups = _make_groups(tuples, marked)

        groups.sort(key = lambda x: x[2])

        result = ""

        div = (len(text) // len(key)) + (1 if len(text) % len(key) != 0 else 0)

        for i in range(div):
            for word in groups:
                result += word[0][i]


    print(result.replace(" ", ""))

if __name__ == "__main__":
    while True:
        arrFunc = [(caesar_cipher, "Cezarova sifra", 1),
        (albam_cipher, "Albam sifra", 2), 
        (atbash_cipher, "Atbas sifra", 3),
        (substitution_cipher, "Substitucna sifra", 4),
        (napoleon_cipher, "Napoleonova sifra", 5),
        (vigener_cipher, "Vigenerova sifra", 6),
        (polybius_cipher, "Polybiova sifra", 7),
        (playfair_cipher, "Playfairova sifra", 8),
        (one_time_pad, "Vernamova sifra", 9),
        (richelieu_cipher, "Richelieuva sifra", 10)]

        for i in range(len(arrFunc)):
            print(arrFunc[i][1] + " (" + str(arrFunc[i][2]) + ")")

        inp = int(input("Zadaj cislo sifry:"))
        text = input("Zadaj text:")
        text = text.upper()

        if inp in [1, 4, 6, 7, 8, 10]:
            key = input("Zadaj kluc:")
            key = key.upper()
            de = input("Zadaj 's' pre sifrovanie alebo zadaj 'd' pre desifrovanie:")
            de = True if de == "d" else False

            arrFunc[inp - 1][0](de, text, key)

        elif inp in [5, 9]:
            key = input("Zadaj kluc:")
            key = key.upper()
            arrFunc[inp - 1][0](text, key)
        else:
            arrFunc[inp - 1][0](text)

        print("********************************\n********************************")









