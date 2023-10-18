from itertools import combinations, groupby


def oneone():
    print("\t\t\t\t\t1.1")
    string = input()
    print(list(string))
#возвращаю стринг используя list(), она разделила по буквам
#не знаю как больше объяснить


def onetwo():
    print("\t\t\t\t\t1.2")
    string = ["T", "h", "e", "B", "i", "g", "B", "e", "n"]
    print(''.join(string))
# .join объединяет элементы, короче говоря



def onethree():
    print("\t\t\t\t\t1.3")
    arr1 = [1,2,3,4,5,6,7]
    arr2 = [5,6,7,9,7,1,10,10]

    array1 = len(arr1) // 2
    array2 = len(arr2) // 2

    print(arr1[:array1] + arr2[array2:])
#Здесь я определил длину массивов, потом разделил их на два
#потом соединил части массивов, :array1 (Беру левую часть), array2: (беру правую)


def onefour():
    print("\t\t\t\t\t1.4")
    arr = (55, 6, 777, 54, 6, 76, 7777, 1, 777, 6)
    count = {}
    result = ()

    for element in arr:
        if element in count:
            count[element] += 1
        else:
            count[element] = 1

    for element, count in count.items():
        result += ((element, count),)

    print(result)

# создаю список, куда закидываю каждый элемент массива, цикл фор проверяет элементы, если есть совпадения, добавляет +1


def onefive():
    print("\t\t\t\t\t1.5")
    arr = (55, 6, 777, 70.0, "7", "A")
    inty = []
    floaty = []
    stringi = []
    for i in arr:
        typ = type(i)
        if typ == int:
            inty.append(i)
        elif typ == float:
            floaty.append(i)
        elif typ == str:
            stringi.append(i)

    print(f"int {inty}")
    print(f"int {floaty}")
    print(f"int {stringi}")


#использовал type() чтобы узнать к какому типу данных принадлежит элемент, дальше все разделил на массивы, все понятно



def twoone():
    print("\t\t\t\t\t2.1")
    str = input()
    my_set = {char for char in str}
    print(my_set)

#посмотрел в лекции, понял что это как бы лист, который хранит уникальные символы char


def twotwo():
    print("\t\t\t\t\t2.2")

    set_A = {1, 2, 3, 4, 5}
    set_B = {5, 7, 8, 9, 2, 10}

    difference1 = set_A - set_B
    difference2 = set_B - set_A

    print(difference1, difference2)


def twothree():
    print("\t\t\t\t\t2.3")

    set_A = {1, 2, 3, 4, 5}
    set_B = {5, 7, 8, 9, 2, 10}

    print(set_B-set_A)

def twofour():
    print("\t\t\t\t\t2.4")

    set_A = {1, 2, 3, 4, 7}
    set_B = {8, 7, 9, 4, 2, 0, 10}
    set_C = {4, 0, 1}

    for element in set_A:
        if element in set_C:
            set_B.add(element)

    print(set_B)

#можете не сравнивать с примером из файла, там перезаписывают С а не Б
# А берылгенынде написано Б



def twofive():
    print("\t\t\t\t\t2.5")

    A = {1, 2, 3, 4, 5, 6}
    n = 3
    m = 5

    combinations_list = []
    while len(combinations_list) < m:
        combo = set(combinations(A, n))
        for c in combo:
            if c not in combinations_list:
                combinations_list.append(c)

    print(combinations_list)

#создал лист куда буду закидывать уникальные комб.
#создал combo которое содержит все возможные комбинации, и она использует функцию combinations
#eсли комбинация C ещё не находится в списке combinations_list, она добавляется в этот список



def threeone():
    cars_list = [('BMW', 'X6'), ('BMW', 'M5'), ('Toyota', 'Mark II'), ('Lexus', 'es300'), ('Toyota', 'Camry 10')]

    sorted_cars = sorted(cars_list, key=lambda x: x[0])
    for manufacturer, group in groupby(sorted_cars, key=lambda x: x[0]):
        group_list = list(group)
        count = len(group_list)
        models = [car[1] for car in group_list]
        print(f"{manufacturer} {count} - {', '.join(models)}")



#сначало сортирую машину по manufacturer, потом создаю цикл, где создаю элементы группы, считаю кол-во машин, и печатаю
oneone()
onetwo()
onethree()
onefour()
onefive()
twoone()
twotwo()
twothree()
twofour()
twofive()
threeone()