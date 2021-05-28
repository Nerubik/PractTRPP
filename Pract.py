def move(s):
    return s[len(s)-1] + s[:len(s)-1]


def bwt_coding(s):
    lst = []
    temp = ''
    s1 = s
    for i in range(len(s)):
        lst.append(s)
        s = move(s)
    lst.sort()
    for i in range(len(lst)):
        if s1 == lst[i]:
            index = i
    for item in lst:
        temp += item[len(item)-1]
    return temp, index


def bwt_decoding(s, index):
    lst = list(s)
    for i in range(len(s) - 1):
        lst.sort()
        for j in range(len(lst)):
            lst[j] = s[j] + lst[j]
    lst.sort()
    return lst[index]

print(bwt_decoding('311',2))
print(bwt_coding('311'))


import  random

names = ['Святослав', 'Доброжир', 'Тихомир', 'Ратибор', 'Ярополк', 'Гостомысл', 'Велимудр', 'Всеволод', 'Богдан',
         'Доброгнева', 'Любомила', 'Миролюб', 'Светозар', 'Милонег']
g = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
s = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'х', 'ц', 'ч', 'ш', 'щ']


def name_generator():
    f_name = names[random.randint(0, len(names) - 1)]
    l_name = s[random.randint(0, len(s) - 1)].upper()
    i = random.randint(4, 10)
    while i != 0:
        if i % 2 == 0:
            l_name += g[random.randint(0, len(g) - 1)]
        else:
            l_name += s[random.randint(0, len(s) - 1)]
        i -= 1
    return f_name + ' ' + l_name


print(name_generator())
print(name_generator())
print(name_generator())
