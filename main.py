import pygame
import sys
import random
from pygame.math import Vector2

class ANACONDA:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0, 0)
        self.new_block = False


        self.head_up = pygame.image.load('head_up.png').convert_alpha()
        self.head_down = pygame.image.load('head_down.png').convert_alpha()
        self.head_right = pygame.image.load('head_right.png').convert_alpha()
        self.head_left = pygame.image.load('head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('tail_up.png').convert_alpha()


        self.body_horizontal = pygame.image.load('body_horizontal.png').convert_alpha()
        self.body_vertical = pygame.image.load('body_vertical.png').convert_alpha()


        self.body_tr = pygame.image.load('body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('body_bl.png').convert_alpha()



    def draw_anaconda(self):
        self.update_head_graphics()
        self.update_tail_graphics()


        for index,block in enumerate(self.body):

            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)


            if index == 0:
                screen.blit(self.head,block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail,block_rect)
            else:
                previous_block = self.body[index - 1] - block
                next_block = self.body[index + 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical,block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl,block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br,block_rect)



            #else:
                #  pygame.draw.rect(screen,(50,220,175),block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1,0): self.head = self.head_right
        elif head_relation == Vector2(0,1): self.head = self.head_up
        elif head_relation == Vector2(0,-1): self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(-1,0): self.tail = self.tail_left
        elif tail_relation == Vector2(1,0): self.tail = self.tail_right
        elif tail_relation == Vector2(0,-1): self.tail = self.tail_up
        elif tail_relation == Vector2(0,1): self.tail = self.tail_down


    def move_anconda(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block =  False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)



class ANIMAL:
    def __init__(self):
        self.randomise()

    def draw_animal(self):
            animal_rect = pygame.Rect(int(self.pos.x * cell_size ),int(self.pos.y * cell_size),cell_size,cell_size)
            screen.blit(Rat,animal_rect)
            #pygame.draw.rect(screen,(180,176,60),fruit_rect)


    def randomise(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)




class MAIN:
    def __init__(self):
        self.anaconda = ANACONDA()
        self.animal = ANIMAL()
    def update(self):
        self.anaconda.move_anconda()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.animal.draw_animal()
        self.draw_grass()
        self.anaconda.draw_anaconda()
        self.draw_score()


    def check_collision(self):
        if self.animal.pos == self.anaconda.body[0]:
            self.animal.randomise()
            self.anaconda.add_block()

        for block in self.anaconda.body[1:]:
            if block == self.animal.pos:
                self.animal.randomise()
    def check_fail(self):
        if not 0 <= self.anaconda.body[0].x < cell_number or not 0 <= self.anaconda.body[0].y < cell_number:
            self.game_over()

        for block in self.anaconda.body[1:]:
            if block == self.anaconda.body[0]:
                self.game_over()


    def game_over(self):
        self.anaconda.reset()


    def draw_grass(self):
        grass_colour = (175, 185, 215)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_colour, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_colour, grass_rect)

    def draw_score(self):
        score_text = str(len(self.anaconda.body) - 3)
        score_surface = game_font.render(score_text,True,(12,56,90))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect  = score_surface.get_rect(center = (score_x,score_y))
        Rat_x = int(cell_size * cell_number - 100)
        Rat_y = int(cell_size * cell_number - 40)
        Rat_rect = Rat.get_rect(center = (Rat_x,Rat_y))



        screen.blit(score_surface,score_rect)
        screen.blit(Rat,Rat_rect)




pygame.init()
cell_size = 25
cell_number = 25
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_number))
clock = pygame.time.Clock()
Rat = pygame.image.load('Rat.png').convert_alpha()
game_font = pygame.font.Font('vanguardian.ttf',20)


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.anaconda.direction.y != 1:
                    main_game.anaconda.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                if main_game.anaconda.direction.y != -1:
                    main_game.anaconda.direction = Vector2(0,1)
            if event.key == pygame.K_RIGHT:
                if main_game.anaconda.direction.x != -1:
                    main_game.anaconda.direction = Vector2(1,0)
            if event.key == pygame.K_LEFT:
                if main_game.anaconda.direction.x != 1:
                    main_game.anaconda.direction = Vector2(-1,0)
        print(main_game.anaconda.direction)
        screen.fill((195,200,245))
        main_game.draw_elements()
        pygame.display.update()
        clock.tick(65)