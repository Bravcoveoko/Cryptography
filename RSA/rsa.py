def egcd(a, b):
    if a == 0:
        return 0, 1
    else:
        x, y = egcd(b % a, a)
        return y - (b // a) * x, x

def nsd(e, fim):
    div = fim // e
    rest = fim - (div * e)

    u = fim
    v = e
    print('REA({0}, {1}):'.format(e, fim))
    while rest != 1:
        print('{0} = {1} * {2} + {3}'.format(u, div, v, rest))

        tmp2 = rest
        div = v // rest
        rest = v - (div * rest)

        tmp = v
        v = tmp2
        u = tmp

    print('{0} = {1} * {2} + {3}'.format(u, div, v, rest))

def get_ord_letter(text):
    arr = []
    for c in text:
        ord_num = str(ord(c))
        print('{0} => {1}'.format(c, ord_num))
        arr.append(ord_num)
    return arr



if __name__ == "__main__":
    while True:
        p = int(input("Zadaj 'p' prvocislo: "))
        q = int(input("Zadaj 'q' prvocislo: "))

        m = p * q
        Fim = (p - 1) * (q - 1)

        print('m = {0}'.format(m))
        print("----------------")
        print('Fi(m) = {0}'.format(Fim))
        print("----------------")

        e = int(input("Zadaj 'e': "))
        text = input("Zadaj text: ")


        nsd(e, Fim)

        print("----------------")

        x, d = egcd(Fim, e)

        print('1 = {0} * {1} + ({2}) * {3}'.format(d, e, x, Fim))

        
        print('d = {0}'.format(d))
        print("----------------")

        letter_arr = get_ord_letter(text)
        print("----------------")

        m_length = len(str(m))

        for i in range(len(letter_arr)):
            if len(letter_arr[i]) != 3:
                letter_arr[i] = ('0' * (3 - len(letter_arr[i]))) + letter_arr[i]


        joined_text = ''.join(letter_arr)

        print("Upraveny text, ktory sa bude sifrovat:", joined_text)
        print("----------------")

        new_arr = [joined_text[i : i + (m_length - 1)] for i in range(0, len(joined_text), m_length - 1)]

        if len(new_arr[-1]) != m_length - 1:
            new_arr[-1] = new_arr[-1] + ((m_length - 1 - len(new_arr[-1])) * '0')

        arr_mod = []

        for n in new_arr:
            num = int(n)
            new_modulo = (num**e) % m
            add_zero = len(str(m)) - len(str(new_modulo))
            result = ('0' * add_zero) + str(new_modulo)

            print('{0}^{1} % {2} = {3}'.format(num, e, m, result))

            arr_mod.append(result)

        print('Zasifrovany text:', ''.join(arr_mod))
        print("----------------")
