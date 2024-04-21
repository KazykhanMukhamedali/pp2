import pygame
import random

pygame.init()

# Установка параметров окна игры
W, H = 1200, 800  # Ширина и высота окна игры
FPS = 60  # Количество кадров в секунду

# Создание окна с заданными размерами
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()  # Создание объекта Clock для управления FPS
done = False  # Переменная для отслеживания завершения игры
bg = (0, 0, 0)  # Цвет фона

# Параметры платформы
paddleW = 150  # Ширина платформы
paddleH = 25  # Высота платформы
paddleSpeed = 20  # Скорость движения платформы
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)  # Создание прямоугольника для платформы

# Параметры мяча
ballRadius = 20  # Радиус мяча
ballSpeed = 6  # Скорость мяча
ball_rect = int(ballRadius * 2 ** 0.5)  # Диаметр мяча (квадрат, в который вписан круг)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)  # Создание прямоугольника для мяча
dx, dy = 1, -1  # Направление движения мяча

# Счет игры
game_score = 0  # Игровой счет
game_score_fonts = pygame.font.SysFont('comicsansms', 40)  # Шрифт для отображения счета
game_score_text = game_score_fonts.render(f'Ваш счет: {game_score}', True, (0, 0, 0))  # Текст для отображения счета
game_score_rect = game_score_text.get_rect()  # Получение прямоугольника для позиционирования текста
game_score_rect.center = (210, 20)  # Центрирование текста по горизонтали и вертикали

# Звук при столкновении
collision_sound = pygame.mixer.Sound('assets/catch.mp3')

# Переменные времени
time_elapsed = 0  # Время, прошедшее с начала игры
speed_increase_interval = 1000  # Интервал увеличения скорости мяча (в миллисекундах)
speed_increase_amount = 0.2  # Величина увеличения скорости мяча
shrink_paddle_interval = 5000  # Интервал уменьшения платформы (в миллисекундах)
shrink_paddle_amount = 10  # Величина уменьшения платформы

# Состояние паузы
is_paused = False  # Переменная для отслеживания состояния паузы

# Экран окончания игры
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Игра окончена', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

# Экран победы
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = winfont.render('Вы победили!', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

# Переменные для сообщений
message_font = pygame.font.SysFont('comicsansms', 40)

last_message = ""  # Последнее сообщение
last_message_rect = None  # Прямоугольник для последнего сообщения

# Функция обнаружения столкновения мяча с объектами
def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    elif delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

# Настройки блоков
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(10) for j in range(4)]  # Создание списка блоков
color_list = [(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)) for i in range(10) for j in range(4)]  # Список случайных цветов для блоков

# Выбор случайных неразрушаемых блоков
unbreakable_block_list = []
for _ in range(5):
    random_index = random.randint(0, len(block_list) - 1)
    unbreakable_block_list.append(block_list.pop(random_index))

unbreakable_color_list = [(0, 0, 255) for _ in range(len(unbreakable_block_list))]

# Типы бонусных кирпичей
bonus_brick_types = {
    "longer_paddle": {"color": (0, 255, 0), "perk": "paddle", "message": "Длинная платформа!"},
    "increase_speed": {"color": (255, 165, 0), "perk": "speed", "message": "Увеличение скорости!"},
}

# Создание бонусных кирпичей
bonus_brick_list = []
for _ in range(5):
    random_index = random.randint(0, len(block_list) - 1)
    bonus_brick_type = random.choice(list(bonus_brick_types.keys()))
    bonus_brick_list.append((block_list.pop(random_index), bonus_brick_type))

# Основной игровой цикл
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                is_paused = not is_paused
            if is_paused:
                if event.key == pygame.K_w:
                    paddleW += 10
                    paddle = pygame.Rect(paddle.left, paddle.top, paddleW, paddleH)
                if event.key == pygame.K_s and paddleW > 10:
                    paddleW -= 10
                    paddle = pygame.Rect(paddle.left, paddle.top, paddleW, paddleH)
                if event.key == pygame.K_d:
                    ballRadius += 1
                if event.key == pygame.K_a and ballRadius > 1:
                    ballRadius -= 1

    if is_paused:
        screen.fill((100, 100, 100))
        pause_text = game_score_fonts.render('Игра приостановлена. Нажмите P, чтобы продолжить.', True, (255, 255, 255))
        settings_text_1 = game_score_fonts.render(
            f'Ширина платформы: {paddleW}, Радиус мяча: {ballRadius}.', True,
            (255, 255, 255))
        settings_text_2 = game_score_fonts.render(
            'W/S: Изменить ширину платформы. D/A: Изменить радиус мяча.', True,
            (255, 255, 255))

        screen.blit(pause_text, (W / 2 - pause_text.get_width() / 2, H / 2 - pause_text.get_height() / 2 - 20))
        screen.blit(settings_text_1, (W / 2 - settings_text_1.get_width() / 2, H / 2 + 20))
        screen.blit(settings_text_2, (W / 2 - settings_text_2.get_width() / 2, H / 2 + 80))

        pygame.display.flip()
        continue

    screen.fill(bg)

    [pygame.draw.rect(screen, color_list[color], block) for color, block in enumerate(block_list)]
    [pygame.draw.rect(screen, (0, 0, 255), block) for block in unbreakable_block_list]

    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    if ball.centery < ballRadius + 50:
        dy = -dy
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    hitIndex = ball.collidelist(block_list)

    if hitIndex != -1:
        hitRect = block_list.pop(hitIndex)
        hitColor = color_list.pop(hitIndex)
        dx, dy = detect_collision(dx, dy, ball, hitRect)
        game_score += 1
        collision_sound.play()

    for i, unbreakable_block in enumerate(unbreakable_block_list):
        if ball.colliderect(unbreakable_block):
            dx, dy = detect_collision(dx, dy, ball, unbreakable_block)

    for block, bonus_type in bonus_brick_list:
        pygame.draw.rect(screen, bonus_brick_types[bonus_type]["color"], block)

    for i, (bonus_brick, bonus_type) in enumerate(bonus_brick_list):
        if ball.colliderect(bonus_brick):
            if bonus_brick_types[bonus_type]["perk"] == "speed":
                ballSpeed += 2

            last_message = bonus_brick_types[bonus_type]["message"]
            last_message_surface = message_font.render(last_message, True, (255, 255, 255))
            last_message_rect = last_message_surface.get_rect(topright=(W - 10, -10))

            del bonus_brick_list[i]
            break

    if last_message:
        screen.blit(last_message_surface, last_message_rect)

    game_score_text = game_score_fonts.render(f'Ваш счет: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)

    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not len(block_list):
        screen.fill((255, 255, 255))
        screen.blit(wintext, wintextRect)
        pygame.display.flip()
        continue

    time_elapsed += clock.get_rawtime()
    if time_elapsed >= speed_increase_interval:
        ballSpeed += speed_increase_amount
        time_elapsed = 0

    if time_elapsed >= shrink_paddle_interval:
        paddleW -= shrink_paddle_amount
        if paddleW < 50:
            paddleW = 50
        paddle.width = paddleW
        time_elapsed = 0

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed

    pygame.display.flip()
    clock.tick(FPS)
