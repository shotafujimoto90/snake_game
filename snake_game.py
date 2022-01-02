import pygame
import random

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
SNAKE_HEAD_SIZE = 10
FOOD_SIZE = 10
WHITE_COLOUR = (250, 250, 250)
BLACK_COLOR = (0, 0, 0)
RED_COLOUR = (250, 0, 0)
BLUE_COLOUR = (0, 0, 250)

pygame.init()
FONT = pygame.font.SysFont(None, 50)
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake_Game')
clock = pygame.time.Clock()


class DrawScene(object):
    def draw_scene(self, msg, color, position):
        label = FONT.render(msg, True, color)
        screen.blit(label, position)


class DrawCharacter(object):
    def draw_snake(self, snake_cells):
        for cell in snake_cells:
            pygame.draw.rect(screen, BLUE_COLOUR, (cell[0], cell[1], SNAKE_HEAD_SIZE, SNAKE_HEAD_SIZE))

    def make_random_foods(self, num_foods):
        foods_list = []
        for _ in range(num_foods):
            food_x = random.choice(list(range(0, WINDOW_WIDTH, 10)))
            food_y = random.choice(list(range(0, WINDOW_HEIGHT, 10)))
            food = (food_x, food_y)
            foods_list.append(food)
        return foods_list

    def draw_foods(self, foods_list):
        for food_x, food_y in foods_list:
            pygame.draw.rect(screen, RED_COLOUR, (food_x, food_y, FOOD_SIZE, FOOD_SIZE))


def is_gameover(snake_head_x, snake_head_y, snake_body):
    if snake_head_x < 0 or snake_head_x > WINDOW_WIDTH:
        return True
    elif snake_head_y < 0 or snake_head_y > WINDOW_HEIGHT:
        return True
    elif (snake_head_x, snake_head_y) in snake_body:
        return True
    return False


def main():
    initial_position = (200, 200)
    x_speed = 0
    y_speed = 0
    snake_len = 1
    snake_cells = []
    snake_cells.append(initial_position)
    foods_list = make_chara.make_random_foods(10)

    try_again = False
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if y_speed == 0:
                        y_speed += -10
                        x_speed = 0
                elif event.key == pygame.K_DOWN:
                    if y_speed == 0:
                        y_speed += 10
                        x_speed = 0
                elif event.key == pygame.K_RIGHT:
                    if x_speed == 0:
                        x_speed += 10
                        y_speed = 0
                elif event.key == pygame.K_LEFT:
                    if x_speed == 0:
                        x_speed += -10
                        y_speed = 0

        head = snake_cells[-1]
        if x_speed != 0 or y_speed != 0:
            new_head = (head[0] + x_speed, head[1] + y_speed)
            snake_cells.append(new_head)
        else:
            new_head = head

        snake_body = snake_cells[:-1]

        if len(snake_cells) > snake_len:
            snake_cells.pop(0)

        snake_head_x = new_head[0]
        snake_head_y = new_head[1]

        if is_gameover(snake_head_x, snake_head_y, snake_body):
            print('GAME OVER')
            try_again = True

        if (snake_head_x, snake_head_y) in foods_list:
            snake_len += 1
            foods_list.remove((snake_head_x, snake_head_y))
            foods_list.append(make_chara.make_random_foods(1)[-1])

        screen.fill(WHITE_COLOUR)
        make_chara.draw_foods(foods_list)
        make_chara.draw_snake(snake_cells)
        score = snake_len - 1
        score_message = 'score: '+ str(score)
        score_scene.draw_scene(msg=score_message, color=BLACK_COLOR, position=(25, 25))

        if try_again:
            running = scene(score)
            continue

        pygame.display.update()
        clock.tick(10)


def scene(score):
    running = True
    can_try_again = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    running = False
                    can_try_again = True
        screen.fill((100, 100, 100))
        if score >= 0:
            score_message = 'score: ' + str(score)
            score_scene.draw_scene(msg=score_message, color=BLACK_COLOR, position=(25, 25))
            message = "Try again?(push->s)"
            try_again_scene.draw_scene(msg=message, color=BLACK_COLOR, position=(WINDOW_WIDTH / 5, WINDOW_HEIGHT / 2))
            
        else:
            message = "Let's start!(push->s)"
            start_scene.draw_scene(msg=message, color=BLACK_COLOR, position=(WINDOW_WIDTH / 5, WINDOW_HEIGHT / 2))
        pygame.display.update()
        clock.tick(10)

        if can_try_again:
            main()

make_chara = DrawCharacter()
start_scene = DrawScene()
score_scene = DrawScene()
try_again_scene = DrawScene()

scene(-1)

pygame.quit()