import random
import pygame


FPS = 60

SNAKE_START_X = 300
SNAKE_START_Y = 300

# Setting color variables
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH = 800
HEIGHT = 600

SNAKE_SIZE = 10
FOOD_SIZE = 10

pygame.init()
clock = pygame.time.Clock()

# Initialize a window for display
display = pygame.display.set_mode((WIDTH, HEIGHT))
# Setting screen caption name
pygame.display.set_caption('Snake')

font_style = pygame.font.SysFont(None, 50)


class Snake():

    def __init__(self, size: int, length: int, body: list):
        self.size = size
        self.length = length
        self.body = body

    def grow(self, body_part: list):
        self.body.append(body_part)

    def incr_length(self):
        self.length += 1

    def get_body(self) -> list:
        return(self.body)

    def get_length(self) -> int:
        return(self.length)

    def del_tail(self):
        if len(self.get_body()) > self.get_length():
            del self.body[0]

    def draw(self):
        for part in self.get_body():
            pygame.draw.rect(display, BLACK, [part[0], part[1], self.size, self.size])


class food():

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def snake_draw(snake):
    for snake_part in snake:
        pygame.draw.rect(display, BLACK, [snake_part[0], snake_part[1], SNAKE_SIZE, SNAKE_SIZE])


def snake_move(snake, x1_move, y1_move):
    snake_ = []
    for snake_part in snake:
        snake_.append([snake_part[0]+x1_move, snake_part[1]+y1_move])
    return snake_


def print_message(text):
    msg = font_style.render(text, True, RED)
    display.blit(msg, [WIDTH/2, HEIGHT/2])


def game():
    x1 = 300
    y1 = 300

    x1_move = 0
    y1_move = 0

    # snake = []
    # snake_head = []
    # snake_length = 1
    # snake.append([x1, y1])

    snake = Snake(SNAKE_SIZE, 1, [[SNAKE_START_X, SNAKE_START_Y]])

    x_food = 0
    y_food = 0

    # Setting variable which sets when close the app
    running = True

    while running:
        for event in pygame.event.get():                        # Processing events
            if event.type == pygame.QUIT:                       # Close the app when a user closes the window
                running = False

            if event.type == pygame.KEYDOWN:                    # Processing pressed keys
                if event.key == pygame.K_LEFT:
                    x1_move = -10
                    y1_move = 0
                elif event.key == pygame.K_RIGHT:
                    x1_move = 10
                    y1_move = 0
                elif event.key == pygame.K_UP:
                    x1_move = 0
                    y1_move = -10
                elif event.key == pygame.K_DOWN:
                    x1_move = 0
                    y1_move = 10

        # snake_tail = snake[-1]
        # snake.append(snake_tail)
        # snake = snake_move(snake, x1_move, y1_move)

        x1 += x1_move
        y1 += y1_move

        snake_head = [x1, y1]
        snake.grow(snake_head)
        # snake.append(snake_head)

        snake.del_tail()
        # if len(snake) > snake_length:
        #     del snake[0]

        # TODO: MODIFY THIS
        # # End game when snake touches its tail
        # for snake_part in snake[:-1]:
        #     if snake_head == snake_part:
        #         running = False

        # TODO: MODIFY THIS
        # if x1 <= 0:
        #     x1 = WIDTH-1
        # elif x1 >= WIDTH:
        #     x1 = 1
        # elif y1 <= 0:
        #     y1 = HEIGHT-1
        # elif y1 >= HEIGHT:
        #     y1 = 1

        if x_food == 0 and y_food == 0:
            x_food = round(random.randrange(
                0, WIDTH - SNAKE_SIZE) / 10.0) * 10.0
            y_food = round(random.randrange(
                0, HEIGHT - SNAKE_SIZE) / 10.0) * 10.0

        display.fill(WHITE)

        # snake_draw(snake)
        snake.draw()
        pygame.draw.rect(display, RED, [x_food, y_food, FOOD_SIZE, FOOD_SIZE])
        pygame.display.update()

        if x1 == x_food and y1 == y_food:
            x_food = round(random.randrange(1, WIDTH - SNAKE_SIZE)/10)*10
            y_food = round(random.randrange(1, HEIGHT - SNAKE_SIZE)/10)*10
            snake.incr_length()
            # snake_length += 1

            # x_food = round(random.randrange(0, WIDTH - 10) / 10.0) * 10.0
            # y_food = round(random.randrange(0, HEIGHT - 10) / 10.0) * 10.0
            print(1)

        # Set number of frames per second
        clock.tick(10)

    pygame.quit()
    quit()


game()


# if(x1 in (0, WIDTH)) or (y1 in (0, HEIGHT)):
#     running = False

# print_message('YOU FAILED')
# pygame.display.update()
#
# time.sleep(3)
