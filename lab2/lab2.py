import csv
import os
import time


# получение символа из escape-последовательности
def esc(code):
    return f'\u001b[{code}m'

RED = esc(41)
BLUE = esc(44)
WHITE = esc(47)
END = esc(0)

# 1 вариант


#1 задание. Генерация и отображение Флага Франции
# create_flag() - функция, которая генерирует Флаг Франции
# y - высота флага
# x - ширина флага
def create_flag(y, x):

    # буфер для накопления флага
    flag = ''
    
    # проходим по столбцам
    for i in range(y):
        # проходим по строкам
        for j in range(x):
            # первая треть флага, закрашивается синим
            if j < (x / 3):
                flag += BLUE
            # вторая треть флага, закрашивается белым
            elif (j >= (x / 3)) and (j < (x -(x / 3))) :
                flag += WHITE
            # третья треть флага, закрашивается красным
            elif j >=  (x -(x / 3)):
                flag += RED

            flag += ' '
    
        flag += f'{END}\n'

    return flag
           

#2.сгенерированный узор, № a
# create_pattern() - функция, которая создаем узор под номером a
# h - высота узора
# w - ширина узора
def create_pattern(h,w):

    # буфер для накопления узора
    pattern = ''

    for i in range(h):
        for j in range(w):
            # если четная строка
            if i % 2 == 0:
                # если в строке индекс чётный, добавляем в узор символ для отображения
                if j % 2 == 0:
                    pattern += f'{WHITE}   {END}'
                else:
                    pattern += '   '
            # если не чётная строка
            if i % 2 != 0:
                # если в строке индекс не чётный, добавляем в узор символ для отображения
                if j % 2 != 0:
                    pattern += f'{WHITE}   {END}'
                else:
                    pattern += '   '
        # для перехода на новую строку, в узоре
        pattern += '\n'
    return pattern


#3.Cоздает график функции, f(x) = x^2
# create_graph() - функция, cоздает график функции, f(x) = x^2
# y - высота узора
# x - ширина узора
def create_graph(y,x):

    graph = ''
    # проходим по оси x от -3 с шагом -1, до x (начинаем c -3, для отображения осей и еденицы измерения)
    for i in range(x, -3, -1):
        # проходим по оси y от -1 с шагом 1, до y+1  ( начинаем c -1, для отображения осей и еденицы измерения)
        for j in range(-1, y+1, 1):

            if j == -1 and i > -1:
                graph += f' {i}|'
            elif i == -2 and j != -1:
                graph += f' {j} '
            elif i == -1 and j == -1:
                graph += '   '
            elif i == -1:
                graph += '---'
            # вычисление y = x * x на каждой итерации, если условие выполняется, то в буффер вместо ' ' записываем символ точки на графике
            elif i == j*j and i>= 0 and j>= 0:
                graph += '\33[31m * '
                graph += END
            else:
                graph += f'   '
        graph += '\n'

    # Отображение графика в терминале
    print(graph)


#4.Cоздает гистограмму на основе условия № 1 
# get_percent() - функция, которая создает гистограмму на основе условия № 1: Книги до 2014 (1980) года и после
def get_percent():
    # сколько книг до 1980 года
    to_1980 = 0
    # сколько книг после 1980 года
    from_1980 = 0
    # считываем данные с csv-файла 
    with open('books-en.csv', 'r') as csv_file:
        table = list(csv.reader(csv_file, delimiter=';'))
        # проходим по списку из файла
        for row in table:
            if row == table[0]:
                continue
            # если в столбце 4, год меньше 1980, то увеличиваем счётчик to_1980, если меньше то увеличиваем счетчик from_1980
            if len(row[3]) <= 4:
                if int(row[3]) <= 1980:
                    to_1980 += 1
                else:
                    from_1980 += 1
    
    # округление с точностью 2 после запятой
    from_1980_percent = round(100*from_1980/len(table), 2)
    to_1980_percent = round(100*to_1980/len(table), 2)

    data = [['<=1980',to_1980_percent],[' >1980',from_1980_percent]]
    return data

#4. Строит гистограмму на основе условия № 1 
# create_histogram() - функция, которая строит гистограмму на основе условия полученных данных
# data - данные, полученные в get_percent, сколько книг до 1980 года и после 1980 года
def create_histogram(data):
    
    graph = ''
    
    for i in range(len(data)-1,-3,-1):
        for j in range(0,110,10):
            if j == 0 and i>= 0:
                graph += f'      |\n{data[i][0]}|'
                number_of_timmes = int(data[i][1])//10
                graph += RED
                graph += '    '*number_of_timmes
                graph += f'{END}{data[i][1]}%'
            elif i <= -1 and j== 0:
                graph +='      '
            elif i == -1 and j> 0:
                graph += f'----'
            elif i == -2 and j> 0:
                graph += f' {j} '
        graph += '\n'
    print(graph)


# animate() - функция, которая создает анимацию
# y - высота флага
# x - ширина флага
def animate(y, x):
    os.system('cls')

    # Флаг Франции
    flag = ''
    for i in range(y):
        for j in range(x):

            if j < (x / 3):
                flag += BLUE
            elif (j >= (x / 3)) and (j < (x -(x / 3))) :
                flag += WHITE
            elif j >=  (x -(x / 3)):
                flag += RED
            flag += ' '
    
        flag += f'{END}\n'
    print(flag)
    time.sleep(1)
    os.system('cls')

    # Флаг Польши
    flag = ''
    for i in range(y):
        for j in range(x):
            if i < y//2:
                flag += WHITE
            elif i < 2*y//2:
                flag += RED
            flag += ' '
        flag += f'{END}\n'
    print(flag)

    time.sleep(1)
    os.system('cls')

    # Флаг Нидерландов
    flag = ''
    for i in range(y):
        for j in range(x):
            if i < y//3:
                flag += RED
            elif i < 2*y//3:
                flag += WHITE
            else:
                flag += BLUE
            flag += ' '
        flag += f'{END}\n'
    print(flag)

    time.sleep(1)

    
if __name__ == "__main__":
    print(f"Вариант 1. \n")

    print(f"1. Флаг Франции: \n")
    print(create_flag(6, 36))

    print(f"2. Сгенерированный Узор, № a'\n")
    print(create_pattern(3, 3))

    print('3. График функции, f(x) = x^2')
    create_graph(9,9)
    
    # сбор данных для построения гистограммы
    percents = get_percent()
    print('4. Гистограмма процентного количества книг до 1980 года и после')
    create_histogram(percents)

    # Доп. задание c анимацией
    animate(6, 36)


