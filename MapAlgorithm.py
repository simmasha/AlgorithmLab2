def LeftBinarySearch(Array: list, Target: int) -> int:
    Start = 0
    End = len(Array) - 1
    while Start <= End:
        Middle = (Start+End)//2
        if Array[Middle] > Target: End = Middle-1
        else: Start = Middle + 1
    return End

def CoordinateCompressing(Rectangles: list, Points: list): #сжатие координат
    x = [] # координаты x
    y = [] # координаты y

    for i in range(len(Rectangles)): # добавляем без повторов
        if Rectangles[i].x1 not in x: x.append(Rectangles[i].x1)
        if Rectangles[i].x2 not in x: x.append(Rectangles[i].x2)
        if Rectangles[i].y1 not in y: y.append(Rectangles[i].y1)
        if Rectangles[i].y2 not in y: y.append(Rectangles[i].y2)

    x.sort() # сортируем
    y.sort()

    for i in range(len(Rectangles)): # записываем новые (сжатые) координаты прямоугольников
        Rectangles[i].x1 = x.index(Rectangles[i].x1)
        Rectangles[i].x2 = x.index(Rectangles[i].x2)
        Rectangles[i].y1 = y.index(Rectangles[i].y1)
        Rectangles[i].y2 = y.index(Rectangles[i].y2)

    for i in range(len(Points)):
        if Points[i].x not in x: Points[i].x = LeftBinarySearch(x, Points[i].x)
        else: Points[i].x = x.index(Points[i].x)
        if Points[i].y not in y: Points[i].y = LeftBinarySearch(y, Points[i].y)
        else: Points[i].y = y.index(Points[i].y)

    return Rectangles, Points, x, y

def Map(Rectangles: list, MaxX: int, MaxY: int): # построение карты
    field = [[0 for x in range(MaxY)] for y in range(MaxX)] # карта заполнена нулями
    for k in range(len(Rectangles)): # повторяем для каждого прямоугольника заполнение
        for i in range(Rectangles[k].x1, Rectangles[k].x2):
            for j in range(Rectangles[k].y1, Rectangles[k].y2):
                field[i][j] += 1
    return field

def RectanglesCounting(Field: list, Points: list):
    for i in range(len(Points)): print(Field[Points[i].x][Points[i].y], end=' ')

