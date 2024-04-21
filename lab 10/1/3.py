import pygame  # Импортируем библиотеку pygame для работы с графикой
import math  # Импортируем математическую библиотеку для выполнения математических операций

# Инициализация pygame
pygame.init()

# Установка количества кадров в секунду
fps = 60

# Создание объекта часов для управления частотой кадров
timer = pygame.time.Clock()

# Задаем ширину и высоту экрана
WIDTH = 800
HEIGHT = 600

# Инициализация переменных для активной фигуры и цвета
active_figure = 0
active_color = 'white'

# Создаем экран с указанными размерами
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# Устанавливаем заголовок окна
pygame.display.set_caption("Paint")

# Инициализируем список для хранения данных о рисунке
painting = []


# Функция для отрисовки меню
def draw_menu(color):
    # Рисуем фоновый прямоугольник меню
    pygame.draw.rect(screen, 'gray', [0, 0, WIDTH, 70])

    # Рисуем горизонтальную линию для разделения меню и холста
    pygame.draw.line(screen, 'black', (0, 70), (WIDTH, 70), 3)

    # Рисуем значок кисти в виде круга
    circle_brush = [pygame.draw.rect(screen, 'black', [10, 10, 50, 50]), 0]
    pygame.draw.circle(screen, 'white', (35, 35), 20)
    pygame.draw.circle(screen, 'black', (35, 35), 18)

    # Рисуем значок кисти в виде прямоугольника
    rect_brush = [pygame.draw.rect(screen, 'black', [70, 10, 50, 50]), 1]
    pygame.draw.rect(screen, 'white', [76.5, 26, 37, 20], 2)

    # Рисуем значок кисти в виде квадрата
    square_brush = [pygame.draw.rect(screen, 'black', [130, 10, 50, 50]), 2]
    pygame.draw.rect(screen, 'white', [135, 15, 40, 40], 2)

    # Рисуем значок кисти в виде прямоугольного треугольника
    right_triangle_brush = [pygame.draw.rect(screen, 'black', [190, 10, 50, 50]), 3]
    pygame.draw.polygon(screen, 'white', [(195, 15), (195, 55), (235, 15)], 2)

    # Рисуем значок кисти в виде равностороннего треугольника
    equilateral_triangle_brush = [pygame.draw.rect(screen, 'black', [250, 10, 50, 50]), 4]
    side_length = 50  # Длина стороны квадрата
    center_x = 250 + side_length / 2  # x-координата центра квадрата
    center_y = 10 + side_length / 2  # y-координата центра квадрата
    triangle_height = side_length * math.sqrt(3) / 2  # Высота равностороннего треугольника

    # Уменьшаем высоту треугольника, чтобы он поместился в квадрат
    triangle_height *= 1

    # Вершины равностороннего треугольника
    vertex1 = (center_x, center_y - triangle_height / 2)
    vertex2 = (center_x - side_length / 2 * 0.9, center_y + triangle_height / 2 * 0.9)
    vertex3 = (center_x + side_length / 2 * 0.9, center_y + triangle_height / 2 * 0.9)

    # Рисуем равносторонний треугольник
    pygame.draw.polygon(screen, 'white', [vertex1, vertex2, vertex3], 2)

    # Рисуем значок кисти в виде ромба
    rhombus_brush = [pygame.draw.rect(screen, 'black', [310, 10, 50, 50]), 5]
    top_left = (310, 10)
    top_right = (360, 10)
    bottom_left = (310, 60)
    bottom_right = (360, 60)

    # Корректируем положение серединных точек, чтобы уменьшить размер ромба
    mid_top = ((top_left[0] + top_right[0]) // 2, (top_left[1] + top_right[1]) // 2 + 4)
    mid_left = ((top_left[0] + bottom_left[0]) // 2 + 4, (top_left[1] + bottom_left[1]) // 2)
    mid_bottom = ((bottom_left[0] + bottom_right[0]) // 2, (bottom_left[1] + bottom_right[1]) // 2 - 4)
    mid_right = ((top_right[0] + bottom_right[0]) // 2 - 4, (top_right[1] + bottom_right[1]) // 2)

    # Рисуем ромб
    pygame.draw.polygon(screen, 'white', [mid_top, mid_left, mid_bottom, mid_right], 2)

    # Создаем список значков кистей
    brush_list = [circle_brush, rect_brush, square_brush, right_triangle_brush, equilateral_triangle_brush,
                  rhombus_brush]

    # Рисуем палитру цветов
    pygame.draw.circle(screen, color, (400, 35), 30)
    pygame.draw.circle(screen, 'dark gray', (400, 35), 30, 3)

    # Загружаем значок ластика и рисуем его
    eraser = pygame.image.load("assets/eraser-square-svgrepo-com.svg")
    eraser_rect = eraser.get_rect(topleft=(WIDTH - 150, 7))
    eraser_rect.width = eraser_rect.height = 25
    screen.blit(eraser, [WIDTH - 150

, 7, 25, 25])

    # Рисуем прямоугольники цветов
    blue = pygame.draw.rect(screen, (0, 0, 255), [WIDTH - 35, 10, 25, 25])
    red = pygame.draw.rect(screen, (255, 0, 0), [WIDTH - 35, 35, 25, 25])
    green = pygame.draw.rect(screen, (0, 255, 0), [WIDTH - 60, 10, 25, 25])
    yellow = pygame.draw.rect(screen, (255, 255, 0), [WIDTH - 60, 35, 25, 25])
    teal = pygame.draw.rect(screen, (0, 255, 255), [WIDTH - 85, 10, 25, 25])
    purple = pygame.draw.rect(screen, (255, 0, 255), [WIDTH - 85, 35, 25, 25])
    black = pygame.draw.rect(screen, (0, 0, 0), [WIDTH - 110, 10, 25, 25])
    color_rect = [blue, red, green, yellow, teal, purple, black, eraser_rect]
    rgb_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0),
                (0, 255, 255), (255, 0, 255), (0, 0, 0), (255, 255, 255)]

    return brush_list, color_rect, rgb_list


# Функция для отрисовки рисунка
def draw_painting(paints):
    for color, pos, figure in paints:
        if color == (255, 255, 255):  # Если цвет - белый
            pygame.draw.rect(screen, color, [pos[0] - 15, pos[1] - 15, 37, 50])  # Рисуем белый прямоугольник
        else:
            if figure == 0:  # Если фигура - круг
                pygame.draw.circle(screen, color, pos, 20, 2)  # Рисуем круг
            elif figure == 1:  # Если фигура - прямоугольник
                pygame.draw.rect(screen, color, [pos[0] - 15, pos[1] - 15, 37, 20], 2)  # Рисуем прямоугольник
            elif figure == 2:  # Если фигура - квадрат
                pygame.draw.rect(screen, color, [pos[0] - 15, pos[1] - 15, 35, 35], 2)  # Рисуем квадрат
            elif figure == 3:  # Если фигура - прямоугольный треугольник
                pygame.draw.polygon(screen, color, [(pos[0] - 15, pos[1] - 15),
                                                    (pos[0] - 15, pos[1] + 35),
                                                    (pos[0] + 35, pos[1] - 15)], 2)  # Рисуем прямоугольный треугольник
            elif figure == 4:  # Если фигура - равносторонний треугольник
                size = 50
                triangle_height = size * math.sqrt(3) / 2
                vertex1 = (pos[0], pos[1] - triangle_height / 2)
                vertex2 = (pos[0] - size / 2, pos[1] + triangle_height / 2)
                vertex3 = (pos[0] + size / 2, pos[1] + triangle_height / 2)
                pygame.draw.polygon(screen, color, [vertex1, vertex2, vertex3], 2)  # Рисуем равносторонний треугольник
            elif figure == 5:  # Если фигура - ромб
                pygame.draw.polygon(screen, color, [(pos[0] - 25, pos[1]),
                                                    (pos[0], pos[1] - 25),
                                                    (pos[0] + 25, pos[1]),
                                                    (pos[0], pos[1] + 25)], 2)  # Рисуем ромб


# Основной цикл программы
run = True
while run:
    # Управляем частотой кадров
    timer.tick(fps)

    # Заполняем экран белым цветом
    screen.fill("white")

    # Получаем текущее положение мыши
    mouse = pygame.mouse.get_pos()

    # Проверяем, нажата ли левая кнопка мыши
    left_click = pygame.mouse.get_pressed()[0]

    # Рисуем меню и получаем список кистей, цветовых прямоугольников и RGB значений
    brushes, colors, rgbs = draw_menu(active_color)

    # Если нажата левая кнопка мыши и мышь находится под меню
    if left_click and mouse[1] > 85:
        # Добавляем данные о рисунке (цвет, позиция, фигура) в список рисования
        painting.append((active_color, mouse, active_figure))

    # Рисуем рисунок
    draw_painting(painting)

    # Если мышь находится под меню
    if mouse[1] > 85:
        # Если активный цвет - белый
        if active_color == (255, 255, 255):
            # Рисуем белый прямоугольник в позиции мыши
            pygame.draw.rect(screen, active_color, [mouse[0] - 15, mouse[1] - 15, 37, 50])
        else:
            # В зависимости от активной фигуры рисуем соответствующую форму в позиции мыши
            if active_figure == 0:  # Круг
                pygame.draw.circle(screen, active_color, mouse, 20, 2)
            elif active_figure == 1:  # Прямоугольник
                pygame.draw.rect(screen, active_color, [mouse[0] - 15, mouse[1] - 15, 37, 20], 2)
            elif active_figure == 2:  # Квадрат
                pygame.draw.rect(screen, active_color, [mouse[0] - 15, mouse

[1] - 15, 35, 35], 2)
            elif active_figure == 3:  # Прямоугольный треугольник
                pygame.draw.polygon(screen, active_color, [(mouse[0] - 15, mouse[1] - 15),
                                                           (mouse[0] - 15, mouse[1] + 35),
                                                           (mouse[0] + 35, mouse[1] - 15)], 2)
            elif active_figure == 4:  # Равносторонний треугольник
                size = 50
                triangle_height = size * math.sqrt(3) / 2
                vertex1 = (mouse[0], mouse[1] - triangle_height / 2)
                vertex2 = (mouse[0] - size / 2, mouse[1] + triangle_height / 2)
                vertex3 = (mouse[0] + size / 2, mouse[1] + triangle_height / 2)
                pygame.draw.polygon(screen, active_color, [vertex1, vertex2, vertex3], 2)
            elif active_figure == 5:  # Ромб
                pygame.draw.polygon(screen, active_color, [(mouse[0] - 25, mouse[1]),
                                                           (mouse[0], mouse[1] - 25),
                                                           (mouse[0] + 25, mouse[1]),
                                                           (mouse[0], mouse[1] + 25)], 2)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Если пользователь нажимает кнопку закрытия окна
            run = False  # Устанавливаем run в False для выхода из цикла

        if event.type == pygame.MOUSEBUTTONDOWN:  # Если пользователь нажимает кнопку мыши
            for i in range(len(colors)):  # Перебираем цветовые прямоугольники
                if colors[i].collidepoint(event.pos):  # Если щелчок мыши внутри цветового прямоугольника
                    active_color = rgbs[i]  # Устанавливаем активный цвет в соответствующее RGB значение

            for i in brushes:  # Перебираем значки кистей
                if i[0].collidepoint(event.pos):  # Если щелчок мыши внутри значка кисти
                    active_figure = i[1]  # Устанавливаем активную фигуру в соответствующий тип кисти

        # Обновляем экран
        pygame.display.flip()

# Завершаем pygame
pygame.quit()