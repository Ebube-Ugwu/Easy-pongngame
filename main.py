import pygame
import sys
from pygame import *

pygame.font.init()
BALLVELOCITY = 0.15
BARVELOCITY = 30

FIRSTBARCOLOR = (36, 145, 0)
SECONDBARCOLOR = (1, 244, 30)
BALLCOLOR = (206, 245, 213)
BGCOLOR = (0, 0, 0)
HIGHLIGHTCOLOR = (200, 255, 200)
SCREENWIDTH = 800
SCREENHEIGHT = 600
SCOREFONT = pygame.font.Font("METAVERSE.otf", 50)
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))


class Main():
    def __init__(self):
        pygame.init()
        running = True
        pygame.display.set_caption("PONG")
        SCREEN.fill(BGCOLOR)
        player_one = Bar(FIRSTBARCOLOR, 1)
        player_two = Bar(SECONDBARCOLOR, 2)
        ball = Ball()
        score_one = 0
        score_two = 0
        rect_two = (750, 15)

        while running:
            SCREEN.fill(BGCOLOR)
            # start of event handling
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

                # key detection
                keys_pressed = pygame.key.get_pressed()
                if keys_pressed[K_DOWN]:
                    player_two.move_down()
                elif keys_pressed[K_UP]:
                    player_two.move_up()

                if keys_pressed[K_w]:
                    player_one.move_up()
                elif keys_pressed[K_s]:
                    player_one.move_down()

                # end of event handling
            player_one.draw_bar()
            player_two.draw_bar()
            player_one.draw_score(score_one)
            player_two.draw_score(score_two, rect=rect_two)
            ball.draw_ball()
            ball.move_ball()
            ball.check_wall_collision()
            ball.check_bar_collision(player_one)
            ball.check_bar_collision(player_two)

            if ball.check_player_score() == 1:
                print('one')
                score_one += 1
            elif ball.check_player_score() == 2:
                print('yes')
                score_two += 1

            pygame.display.update()


class Bar():
    def __init__(self, color, player):
        self.velocity = BARVELOCITY
        self.color = color
        self.width = 20
        self.height = 100
        self.player = player
        self.x = 0
        self.y = (SCREENHEIGHT // 2 - self.height // 2)

    def draw_bar(self):
        if self.player == 1:
            self.x = 5
        else:
            self.x = 775

        pygame.draw.rect(SCREEN, self.color,
                         (self.x, self.y, self.width, self.height))
        pygame.draw.rect(SCREEN, HIGHLIGHTCOLOR,
                         (self.x, self.y, self.width, self.height), 5)

    def draw_score(self, score, rect=(25, 15)):
        # creates an image of the text that must be blitted
        text = SCOREFONT.render(str(score), True, BALLCOLOR)
        SCREEN.blit(text, rect)

    def move_up(self):
        if self.y <= 15:
            return
        self.y -= self.velocity

    def move_down(self):
        if self.y >= 485:
            return
        self.y += self.velocity


class Ball():
    def __init__(self, ):
        self.x_velocity = BALLVELOCITY
        self.y_velocity = BALLVELOCITY
        self.color = BALLCOLOR
        self.radius = 14
        self.x = SCREENWIDTH // 2
        self.y = SCREENHEIGHT // 2
        self.ball_hits = 0

    def draw_ball(self):
        pygame.draw.circle(SCREEN, self.color, (self.x, self.y), self.radius)
        return

    def check_wall_collision(self):
        if self.y >= (SCREENHEIGHT - (self.radius + 10)) or self.y <= (0 + (self.radius + 10)):
            self.y_velocity *= -1
            return

    def check_bar_collision(self, bar):
        x, y, width, height = bar.x, bar.y, bar.width, bar.height
        rect = pygame.Rect(x, y, width, height)
        if rect.collidepoint(self.x, self.y):
            self.x_velocity *= -1
            self.ball_hits += 1
        return

    def reset_ball(self):
        self.x = SCREENWIDTH // 2
        self.y = SCREENHEIGHT // 2
        return

    def check_player_score(self):
        if self.x >= (SCREENWIDTH + self.radius):
            self.reset_ball()
            return 1
        elif self.x <= (0):
            self.reset_ball()
            return 2

    def move_ball(self):
        self.x += self.x_velocity
        self.y += self.y_velocity
        return


def increase_ball_speed(self):
    if self.ball_hits >= 5:
        self.y_velocity += 0.05
        self.ball_hits = 0


if __name__ == "__main__":
    main = Main()
