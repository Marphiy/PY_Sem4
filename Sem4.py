import math
import random
import os


def string_fill(*params):
    res: str = ""
    for item in params:
        res += item
    return res

def evklid(a, b):
    while a !=0 and b !=0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def zadacha_27():  # 27. Задайте строку из набора чисел. Напишите программу, которая покажет
    # большее и меньшее число. В качестве символа-разделителя используйте пробел.
    my_str = '31 8 17 0 44 11 21 56 6'
    print(f'Имеем строку: {my_str}')
    my_str = my_str.split(' ')
    my_list = ([int(elem) for elem in my_str])
    print(
        f'Минимальноре число списка = {min(my_list)}, максимальное = {max(my_list)}')


# 28. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
def zadacha_28():
    # 1. с помощью математических формул нахождения корней квадратного уравнения
    # 2. с помощью дополнительных библиотек Python

    A = float(input('Введите А: '))
    B = float(input('Введите B: '))
    C = float(input('Введите C: '))
    # D = B ** 2 - 4 * A * C
    # if D == 0:
    #     x = -B / (2 * A)
    #     print(f'Корень = {x}')
    # elif D > 0:
    #     x1 = (-B + D ** 0.5) / (2 * A)
    #     x = (-B - D ** 0.5) / (2 * A)
    #     print(f'Корни = {x} и {x1}')
    # else: print('Нет корней!')
    
    D = pow(B, 2) - 4 * A * C
    if D == 0:
        x = -B / (2 * A)
        print(f'Корень = {x}')
    elif D > 0:
        x1 = (-B + math.sqrt(D)) / (2 * A)
        x = (-B - math.sqrt(D)) / (2 * A)
        print(f'Корни = {x} и {x1}')
    else: print('Нет корней!')
    
def zadacha_29(): # 29. Задайте два числа. Напишите программу, которая найдёт НОК 
        # (наименьшее общее кратное) этих двух чисел.
    A = int(input('Введите А: '))
    B = int(input('Введите B: '))  
    print(int(A * B / evklid(A, B)))
    

def zadacha_30():  # 30. Вычислить число Пи c заданной точностью d
    print(math.pi)
    d = float(input('Введите точность, с которой требуется определить число Пи: '))
    print(int(math.pi / d) * d)


def zadacha_31():  # 31. Задайте натуральное число N. Напишите программу, которая
    # составит список простых множителей числа N.
    numb = int(input('Задайте натуральное число N:\n'))
    my_list = []
    TWO = 2
    THREE = 3
    FIVE = 5
    SEVEN = 7
    NINE = 9
    while True:
        if numb <= 0:
            break
        elif numb == 1:
            break
        elif numb % TWO == 0:
            my_list.append(TWO)
            numb //= TWO
        elif numb % THREE == 0:
            my_list.append(THREE)
            numb //= THREE
        elif numb % FIVE == 0:
            my_list.append(FIVE)
            numb //= FIVE
        elif numb % SEVEN == 0:
            my_list.append(SEVEN)
            numb //= SEVEN
        elif math.sqrt(numb) == int(math.sqrt(numb)):
            my_list.append(int(math.sqrt(numb)))
            numb //= int(math.sqrt(numb))
        elif numb % numb == 0:
            my_list.append(numb)
            numb //= NINE
            break
    if len(my_list) == 1:
        my_list.append(1)
    print(
        f'Число {numb} раскладывается на следующие простые множители: {my_list}')
    
def zadacha_32(): # 32. Задайте последовательность чисел. Напишите программу, которая выведет 
    # список неповторяющихся элементов исходной последовательности.
    my_list = ([random.randint(0,10) for i in range(10)])
    print(f'Имеем случайную последовательность чисел: {my_list}')
    count = 0
    new_list = []
    for elem in my_list:
        count = 0
        for i in range(len(my_list)):
            if elem == my_list[i]: count += 1
        if count == 1: new_list.append(elem)
    new_list.sort()
    print(f'Список неповторяющихся элементов исходной последовательности: {new_list}')
    
def mnogochlen():
    nat_step = random.randint(1, 10)
    k1 = random.randint(1, 10)
    k2 = random.randint(0, 10)
    k3 = random.randint(0, 10)
    print(f'Натуральная степень = {nat_step}\nk1 = {k1}\nk2 = {k2}\nk3 = {k3}')
    my_str: str = ''
    chlen1: str = ''
    chlen2: str = ''
    chlen3: str = ''
    if nat_step > 1:
        if k1 == 1: chlen1 = chlen1 + 'x^' + str(nat_step)
        else: chlen1 = chlen1 + str(k1) + 'x^' + str(nat_step)
    else: 
        if k1 == 1: chlen1 = chlen1 + 'x'
        else: chlen1 = chlen1 + str(k1) + 'x'
    my_str = my_str + chlen1
    if k2 != 0:
        if k2 == 1: 
            chlen2 = 'x'    
        else: chlen2 = chlen2 + str(k2) + 'x'
        my_str = my_str + ' + ' + chlen2
    if k3 != 0: 
        chlen3 = chlen3 + str(k3)
        my_str = my_str + ' + ' + chlen3
    my_str = my_str + ' = 0' 
    return my_str
    
def zadacha_33(): # 33. Задана натуральная степень k. Сформировать случайным образом список 
    # коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k и 
    # приравняйте его к нулю. 1. k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x²  = 0
    os.system('cls' if os == 'nt' else 'clear')
    print('Имеем 1й произвольный многочлен: ')
    my_str1 = mnogochlen()
    f1_name = input('Введите имя файла для сохранения 1го многочлена (1.txt): ')
    print(f'Записываем полученный многочлен {my_str1} в файл {f1_name}')
    with open(f1_name, 'w') as file1:
        file1.write(my_str1)
    print()
    print('Имеем 2й произвольный многочлен: ')
    my_str2 = mnogochlen()
    f2_name = input('Введите имя файла для сохранения 2го многочлена (2.txt): ')
    print(f'Записываем полученный многочлен {my_str2} в файл {f2_name}')
    with open(f2_name, 'w') as file1:
        file1.write(my_str2)
    f_names = [f1_name, f2_name]
    return f_names
        
def zadacha_34(): # 34. Даны два файла, в каждом из которых находится запись многочлена, 
    # приравненного к нулю. Задача - сформировать файл, содержащий сумму многочленов 
    # (суммируем подобные слагаемые).   
    os.system('cls' if os == 'nt' else 'clear')
    f_names = zadacha_33()
    print()
    with open(f_names[0]) as file1:
        m_chlen1 = file1.readline()
    with open(f_names[1]) as file2:
        m_chlen2 = file2.readline()
    print(f'Производим считывание многочленов из файлов {f_names[0]} и {f_names[1]}:\n{m_chlen1}\n{m_chlen2}')  
    m1_k1: str = ''
    new_m_chlen: str = ''
    for i in range(m_chlen1.find('x')):
        m1_k1 = m1_k1 + m_chlen1[i]
    m2_k1: str = ''
    m1_k3: str = ''
    m2_k3: str = ''
    for i in range(m_chlen2.find('x')):
        m2_k1 = m2_k1 + m_chlen2[i]
    if m1_k1 == '': m1_k1 = '0'
    if m2_k1 == '': m2_k1 = '0'
    k1_sum = int(m1_k1) + int(m2_k1)
    if m_chlen1.find('^') != -1: nat_step1 = int(m_chlen1[m_chlen1.find('x') + 2: m_chlen1.find('+')])
    else: nat_step1 = 0
    if m_chlen2.find('^') != -1: nat_step2 = int(m_chlen2[m_chlen2.find('x') + 2: m_chlen2.find('+')])
    else: nat_step2 = 0
    nat_step_sum = nat_step1 + nat_step2
    new_chlen1: str = ''
    if k1_sum != 0: 
        if nat_step_sum != 0: new_chlen1 = new_chlen1 + str(k1_sum) + 'x^' + str(nat_step_sum)
        else: new_chlen1 = new_chlen1 + str(k1_sum) + 'x'
    else:
        if nat_step_sum != 0: new_chlen1 = new_chlen1 + 'x^' + str(nat_step_sum)
        else: new_chlen1 = new_chlen1 + str(k1_sum) + 'x'
    # print(new_chlen1)
    if m_chlen1[m_chlen1.find('+'): len(m_chlen1)].find('x', 2) != - 1: 
        m1_k2 = m_chlen1[m_chlen1.find('+') + 2: m_chlen1.find('x', 2)]
        m1_k3 = m_chlen1[-6: m_chlen1.find('=') - 1]
        if m1_k2 == '': m1_k2 = '0'  
    else: 
        m1_k2 = '0'
        m1_k3 = m_chlen1[-6: m_chlen1.find('=') - 1]
    if m1_k3 == '': m1_k3 = '0'
    if m_chlen2[m_chlen2.find('+'): len(m_chlen2)].find('x', 2) != - 1: 
        m2_k2 = m_chlen2[m_chlen2.find('+') + 2: m_chlen2.find('x', 2)] 
        m2_k3 = m_chlen2[-6: m_chlen2.find('=') - 1]
        if m2_k2 == '': m2_k2 = '0'   
    else: 
        m2_k2 = '0'
        m2_k3 = m_chlen2[-6: m_chlen2.find('=') - 1]
    if m2_k3 == '': m1_k3 = '0'
    k2_sum = int(m1_k2) + int(m2_k2)
    k3_sum = int(m1_k3) + int(m2_k3)
    new_m_chlen = new_m_chlen + new_chlen1
    new_chlen1: str = ''
    new_chlen2: str = ''
    new_chlen3: str = ''
    if k2_sum != 0: 
        new_chlen2 = new_chlen2 + str(k2_sum) + 'x'
        new_m_chlen = new_m_chlen + ' + ' + new_chlen2
    if k3_sum != 0: 
        new_chlen3 = new_chlen3 + str(k3_sum)
        new_m_chlen = new_m_chlen + ' + ' + new_chlen3 + ' = 0'
    else: new_m_chlen = new_m_chlen + ' = 0'
    print()
    new_file_name = 'result.txt'
    print(f'Сумма многочленов = {new_m_chlen}')
    print(f'Записываем результат в {new_file_name}')
    with open(new_file_name, 'w') as res_file:
        res_file.write(new_m_chlen)
        
    
    
    

# zadacha_27()
# zadacha_28()
# zadacha_29()
# zadacha_30()
# zadacha_31()
# zadacha_32()
# zadacha_33()
# zadacha_34()
