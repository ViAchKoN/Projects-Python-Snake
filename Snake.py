import random
import pygame


# SETTING GLOBAL VARIABLES
# Setting number of frames per second
FPS = 10

# Setting starting position of snake
SNAKE_START_X = 300
SNAKE_START_Y = 300

# Setting color variables
COLORS = {
        'BLUE': (0, 0, 255),
        'RED': (255, 0, 0),
        'ORANGE': (255, 165, 0),
        'GREEN': (0, 255, 0),
        'YELLOW': (255, 255, 0),
        'WHITE': (255, 255, 255),
        'BLACK': (0, 0, 0),
        'GREY': (128, 128, 128)
        }

# Setting screen size
WIDTH = 800
HEIGHT = 600

# Setting snake and food size
SNAKE_SIZE = 10
FOOD_SIZE = 10

pygame.init()                                               # Initialize pygame
clock = pygame.time.Clock()                                 # Initialize clock

display = pygame.display.set_mode((WIDTH, HEIGHT))          # Initialize a window for display
pygame.display.set_caption('Snake')                         # Setting screen caption name

font_style = pygame.font.SysFont('comicsansms', 25)         # Setting game font size


# Class Snake
class Snake:
    '''
    Class which defines snake
    '''
    def __init__(self):
        self.size = SNAKE_SIZE
        self.length = 1
        self.body = [[SNAKE_START_X, SNAKE_START_Y]]
        self.color = COLORS['ORANGE']

    def grow(self, body_part: list) -> None:
        '''
        Move snake to a new position
        :param body_part: Cooridinates of the snake body parts
        :return:
        '''
        self.body.append(body_part)

    def incr_length(self) -> None:
        '''
        Increase snake length by one cube
        :return:
        '''
        self.length += 1

    def move(self, x_move: int, y_move: int) -> None:
        '''
        Set a new direction snake to move
        :param x_move: Coordinates where to move on x-axis
        :param y_move: Coordinates where to move on y-axis
        :return:
        '''
        x, y = self.get_head()[0] + x_move, self.get_head()[1] + y_move
        if x <= 0:
            x = WIDTH
        elif x >= WIDTH:
            x = 0
        elif y <= 0:
            y = HEIGHT
        elif y >= HEIGHT:
            y = 0
        self.grow([x, y])
        if len(self.body) > self.length:
            del self.body[0]

    def get_head(self) -> list:
        '''
        Get the coordinates of snake head
        :return:
        '''
        return self.body[-1]

    def check_collision(self) -> bool:
        '''
        Check of snake head hit the body
        :return:
        '''
        for part in self.body[:-1]:
            if self.get_head() == part:
                return True

    def check_back(self, x_move: int, y_move: int) -> bool:
        '''
        Check if a new direction means that snake moves back
        :param x_move: Coordinates where to move on x-axis
        :param y_move: Coordinates where to move on y-axis
        :return: True/False
        '''
        if self.length > 2:
            x, y = self.get_head()[0] + x_move, self.get_head()[1] + y_move
            if [x, y] != self.body[-2]:
                return True
        else:
            return True

    def draw(self) -> None:
        '''
        Draw snake on the screen
        :return:
        '''
        for i in range(0, self.length):
            if i % 2 == 0 or i == 0:
                color = COLORS['ORANGE']
            else:
                color = COLORS['GREY']
            pygame.draw.rect(display, color, [self.body[i][0], self.body[i][1], self.size, self.size])


class Food:
    '''
    Class which defines food
    '''
    def __init__(self):
        self.x = round(random.randrange(0, WIDTH - SNAKE_SIZE)/10.0)*10.0
        self.y = round(random.randrange(0, HEIGHT - SNAKE_SIZE)/10.0)*10.0
        self.size = FOOD_SIZE
        self.color = COLORS['GREEN']

    def get_loc(self) -> tuple:
        '''
        Get coordinates of food
        :return: Coordinates of food
        '''
        return self.x, self.y

    def update_loc(self) -> None:
        '''
        Update coordinates of food
        :return:
        '''
        self.x = round(random.randrange(0, WIDTH - SNAKE_SIZE) / 10.0) * 10.0
        self.y = round(random.randrange(0, HEIGHT - SNAKE_SIZE) / 10.0) * 10.0

    def draw(self) -> None:
        '''
        Draw food on the screen
        :return:
        '''
        pygame.draw.rect(display, self.color, [self.get_loc()[0], self.get_loc()[1], self.size, self.size])


def print_score(score: int) -> None:
    '''
    Display score on the screen
    :param score: Score
    :return:
    '''
    value = font_style.render("Score: " + str(score), True, COLORS['BLUE'])
    display.blit(value, [0, 0])


def print_message(text: str, color: tuple) -> None:
    '''
    Display message on the screen
    :param text: Text to display
    :param color: Color of text
    :return:
    '''
    msg = font_style.render(text, True, color)
    display.blit(msg, [WIDTH/2-150, HEIGHT/2])


def run() -> None:
    '''
    Game procedure
    :return:
    '''
    x1_move = 0
    y1_move = 0

    # Create exemplar of class Snake and Food
    snake = Snake()
    food = Food()

    # Setting variable which sets when close the app
    running = True
    round_end = False

    while running:
        while round_end:
            display.fill(COLORS['GREY'])
            print_message("Press 'C' to play again or 'Q' to exit game", COLORS['RED'])
            print_score(snake.length-1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:                   # Close the app when a user closes the window
                    running = False
                    round_end = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False
                        round_end = False
                    if event.key == pygame.K_c:
                        run()

        for event in pygame.event.get():                        # Processing events
            if event.type == pygame.QUIT:                       # Close the app when a user closes the window
                running = False

            if event.type == pygame.KEYDOWN:                    # Processing pressed keys
                if event.key == pygame.K_LEFT:
                    if snake.check_back(-10, 0):
                        x1_move = -10
                        y1_move = 0
                elif event.key == pygame.K_RIGHT:
                    if snake.check_back(10, 0):
                        x1_move = 10
                        y1_move = 0
                elif event.key == pygame.K_UP:
                    if snake.check_back(0, -10):
                        x1_move = 0
                        y1_move = -10
                elif event.key == pygame.K_DOWN:
                    if snake.check_back(0, 10):
                        x1_move = 0
                        y1_move = 10

        snake.move(x1_move, y1_move)

        # End game when snake touches its tail
        if snake.check_collision():
            round_end = True

        display.fill(COLORS['WHITE'])

        food.draw()
        snake.draw()
        print_score(snake.length-1)
        pygame.display.update()

        if snake.get_head()[0] == food.get_loc()[0] and snake.get_head()[1] == food.get_loc()[1]:
            food.update_loc()
            snake.incr_length()

        # Set number of frames per second
        clock.tick(FPS)

    pygame.quit()
    quit()


if __name__ == "__main__":
    run()
