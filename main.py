''' This is a new version of classic game road fighter'''

import random
import time
import pygame
pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=512)
pygame.mixer.init()
pygame.init()

                                        #Declaring constants
GAME_W = 1100                           #Game window width
GAME_H = 700                            #Game window height
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (186, 12, 0)
ORANGE = (255, 128, 0)
BLUE = (0, 123, 174)
ROAD_W = 287

                                        #Setting game window dimensions and title
SCREEN = pygame.display.set_mode((GAME_W, GAME_H))
pygame.display.set_caption('Road fighter')
CLOCK = pygame.time.Clock()

                                        #Loading all the image sources
carImg = pygame.image.load('cars/main_car.png')
blockcarImg = pygame.image.load('cars/block_car.png')
fuel_car = pygame.image.load('cars/fuel.png')

lev1_road = pygame.image.load('level_1/road.png')
lev1_road1 = pygame.image.load('level_1/road1.png')
lev1_road2 = pygame.image.load('level_1/road2.png')
lev1_bush = pygame.image.load('level_1/bush.png')
lev1_bush1 = pygame.image.load('level_1/bush1.png')

lev2_road = pygame.image.load('level_2/road.png')
lev2_road1 = pygame.image.load('level_2/road1.png')
lev2_road2 = pygame.image.load('level_2/road2.png')
lev2_bush_left = pygame.image.load('level_2/bush_left.png')
lev2_bush1_left = pygame.image.load('level_2/bush1_left.png')
lev2_bush_right = pygame.image.load('level_2/bush_right.png')
lev2_bush1_right = pygame.image.load('level_2/bush1_right.png')

title = pygame.image.load('launch_screen/images.png')
back = pygame.image.load('launch_screen/back.png')

intro_song = pygame.mixer.Sound('Sounds/launch_audio.wav') #loading the intro song



def displaytext(text, x, y, colour, text_size):
    '''displays text on screen with required co-ordinates'''
    textfont = pygame.font.Font('freesansbold.ttf', text_size)
    text_surface = textfont.render(text, False, colour)
    text_box = text_surface.get_rect()
    text_box.center = (x, y)
    SCREEN.blit(text_surface, text_box)



def D_button(x, y, width, length, colour_of_border, colour_on, colour_off, text):
    '''displays button and returns whether it is pressed or not'''
    pygame.draw.rect(SCREEN, colour_of_border, [x, y, width, length], 5)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + 30 < mouse_x < x + width - 30 and y + 10 < mouse_y < y + length - 10:
        displaytext(text, x + width//2 + 1, y + length//2 + 1, colour_on, 50)
        if click[0] == 1:
            return 1
    else:
        displaytext(text, x + width//2, y + length//2, colour_off, 50)
    return 0



def intro():
    '''Displays the entry screen of the game'''
    play_status = 0                                 #stores whether the user presses play or not
    quit_status = 0                                 #stores whether the user presses quit or not
    SCREEN.blit(back, (0, 0))                       #background image of fire
    intro_song.play(-1)                             #plays war-like-song indefinitely until stopped by start() function
    while play_status == 0:
        SCREEN.blit(title, (GAME_W*0.28, GAME_H*0.1))
        pygame.draw.rect(SCREEN, WHITE, [GAME_W*0.05, GAME_H*0.05, GAME_W*0.9, GAME_H*0.9], 4)
        #Displaying both and Checking either of play or quit button is pressed
        play_status = D_button(GAME_W*0.4, GAME_H*0.5, GAME_W*0.15, GAME_H*0.1, ORANGE, RED, ORANGE, "PLAY")
        quit_status = D_button(GAME_W*0.4, GAME_H*0.7, GAME_W*0.15, GAME_H*0.1, ORANGE, RED, ORANGE, "QUIT")
        #Whether user exits the game window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_status = 1
        if quit_status == 1:
            pygame.quit()
            quit()
        pygame.display.flip()


def reprint(road_change, level):
    '''changes road and side bushes per frame to give effect of driving car'''
    SCREEN.fill(BLACK)
    x, y = GAME_W*0.3 + ROAD_W + 100, 0  
    width, length = GAME_W - x, GAME_H
    if level == 1:
        pygame.draw.rect(SCREEN, BLUE, [x, y, width, length])
        pygame.draw.rect(SCREEN, BLUE, [0, 0, (width + x)*0.3 - 100, length])
        #NO.1 Config of road and bushes
        if road_change == 0:
            SCREEN.blit(lev1_road, (GAME_W*0.3, 0))
            SCREEN.blit(lev1_bush, (GAME_W*0.3-100, 0))
            SCREEN.blit(lev1_bush, (GAME_W*0.3 + ROAD_W, 0))
        #NO.2 Config of road and bushes
        elif road_change == 1:
            SCREEN.blit(lev1_road2, (GAME_W*0.3, 0))
            SCREEN.blit(lev1_bush1, (GAME_W*0.3-100, 0))
            SCREEN.blit(lev1_bush1, (GAME_W*0.3 + ROAD_W, 0))
        #NO.3 Config of road and bushes
        else:
            SCREEN.blit(lev1_road1, (GAME_W*0.3, 0))
            SCREEN.blit(lev1_bush, (GAME_W*0.3-100, 0))
            SCREEN.blit(lev1_bush, (GAME_W*0.3 + ROAD_W, 0))
    elif level == 2:
        pygame.draw.rect(SCREEN, ORANGE, [x, y, width, length])
        pygame.draw.rect(SCREEN, ORANGE, [0, 0, (width + x)*0.3 - 100, length])
        #NO.1 Config of road and bushes
        if road_change == 0:
            SCREEN.blit(lev2_road, (GAME_W*0.3, 0))
            SCREEN.blit(lev2_bush_left, (GAME_W*0.3-100, 0))
            SCREEN.blit(lev2_bush_right, (GAME_W*0.3 + ROAD_W, 0))
        #NO.2 Config of road and bushes
        elif road_change == 1:
            SCREEN.blit(lev2_road2, (GAME_W*0.3, 0))
            SCREEN.blit(lev2_bush1_left, (GAME_W*0.3-100, 0))
            SCREEN.blit(lev2_bush1_right, (GAME_W*0.3 + ROAD_W, 0))
        #NO.3 Config of road and bushes
        else:
            SCREEN.blit(lev2_road1, (GAME_W*0.3, 0))
            SCREEN.blit(lev2_bush_left, (GAME_W*0.3-100, 0))
            SCREEN.blit(lev2_bush_right, (GAME_W*0.3 + ROAD_W, 0))
    
    #Black line border for road
    pygame.draw.line(SCREEN, BLACK, [x, 0], [x, GAME_H], 8)
    pygame.draw.line(SCREEN, BLACK, [x - ROAD_W - 200, 0], [x - ROAD_W - 200, GAME_H], 8)
    displaytext("Press SPACE to pause", GAME_W*0.815, GAME_H*0.6, RED, 30)
    displaytext("Press SPACE to unpause", GAME_W*0.83, GAME_H*0.65, RED, 30)
    displaytext("Press M to mute", GAME_W*0.771, GAME_H*0.7, RED, 30)
    displaytext("Press M to unmute", GAME_W*0.788, GAME_H*0.75, RED, 30)

def pause():
    '''Pauses the game'''
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False
                    pygame.mixer.unpause()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


def fuel_change(fuel, color):
    '''Displays fuel bar and updates bar length according to fuel'''
    displaytext("FUEL", GAME_W*0.8 + 50, GAME_H*0.2 - 50, BLACK, 40)
    pygame.draw.rect(SCREEN, color, [GAME_W*0.8 - 50, GAME_H*0.2 + 10, fuel*2 - 5, 50])
    pygame.draw.rect(SCREEN, BLACK, [GAME_W*0.8 - 50, GAME_H*0.2 + 10, 200, 50], 5)

def display_score(score):
    '''displays updated score'''
    displaytext("SCORE", GAME_W*0.8 + 50, GAME_H*0.4, BLACK, 40)
    score_str = str(score)
    displaytext(score_str, GAME_W*0.8 + 50, GAME_H*0.4 + 60, WHITE, 40)


def crash(score, fuel):
    meme = pygame.image.load('game_over/over.png')
    if fuel < 30:
        fuel_change(fuel, RED)
    else:
        fuel_change(fuel, WHITE)
    display_score(score)
    SCREEN.blit(meme, (GAME_W*0.3 - 50, GAME_H*0.2))
    pygame.mixer.stop()
    crash_sound = pygame.mixer.Sound('Sounds/crash.wav')
    crash_sound.play()
    time.sleep(2)
    pygame.display.flip()
    time.sleep(2)

def no_fuel():
    meme = pygame.image.load('game_over/fuel_over.png')
    if fuel < 30:
        fuel_change(fuel, RED)
    else:
        fuel_change(fuel, WHITE)
    display_score(score)
    SCREEN.blit(meme, (GAME_W*0.3 - 50, GAME_H*0.2))
    pygame.mixer.stop()
    crash_sound = pygame.mixer.Sound('Sounds/crash.wav')
    crash_sound.play()
    time.sleep(2)
    pygame.display.flip()
    time.sleep(2)




def check_crash(x, y, x_blockcar1, y_blockcar1):
    '''checks for crash of car with other cars'''
    if x >= x_blockcar1 - 47 and x <= x_blockcar1 + 45 and y >= y_blockcar1 and y <= y_blockcar1 + 59:
        return True
    return False


def car(x, y):
    '''displays car'''
    SCREEN.blit(carImg, (x, y))


def blockcar(x, y):
    '''displays blocking yellow car'''
    SCREEN.blit(blockcarImg, (x, y))


def pfuel_car(x, y):
    '''displays fuel car'''
    SCREEN.blit(fuel_car, (x, y))


def start(x, y, road_change):
    '''Is called when user presses play
    prints initial playing screen and plays music while engine is starting'''
    reprint(road_change, 1)                             #display road and bush
    car(x, y)                                        #display car
    fuel = 100
    score = 0
    fuel_change(fuel, WHITE)                         #display fuel bar
    display_score(score)                             #display score
    pygame.display.flip()
    start_sound = pygame.mixer.Sound('Sounds/race_start.wav')
    start_sound.play()                               #plays start music
    start_time = time.time()
    curr_time = start_time
    mute = False
    while curr_time - start_time < 9:
        curr_time = time.time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pygame.mixer.pause()
                    pause()
                elif event.key == pygame.K_m:
                    if mute:
                        pygame.mixer.unpause()
                        mute = False
                    else:
                        pygame.mixer.pause()
                        mute = True
    start_sound.stop()




def game_loop():
    '''Main function which manages the game'''
    #declaring variables
    x = GAME_W*0.45
    y = GAME_H*0.6
    x_change, swap = 0, 1
    score, fuel = 0, 100
    level = 1
    #x-coordinate of blocking car no.1
    x_blockcar1 = random.randrange(GAME_W*0.3, GAME_W*0.3 + ROAD_W - 45)
    #x-coordinate of blocking car no.2
    x_blockcar2 = random.randrange(GAME_W*0.3, GAME_W*0.3 + ROAD_W - 45)
    #y-coordinates of both the blocking cars
    y_blockcar1, y_blockcar2 = -200, -1000
    #x and y coordinates of fuel car
    x_fuel_car = random.randrange(GAME_W*0.3, GAME_W*0.3 + ROAD_W - 45)
    y_fuel_car = 0
    isfuelcar = False                                   #whether fuel car is on screen
    speed, road_change = 6, 3
    game_exit_status = 1
    mute = False

    intro_song.stop()                                   #Stopping the 'heavy' game intro music
    start(x, y, road_change)                            #starting the drive

    buzz = pygame.mixer.Sound('Sounds/running.wav')
    buzz.play(-1)                                       #playing the sound of engine
    pygame.time.set_timer(pygame.USEREVENT + 1, 6000)
    while game_exit_status == 1:                                #runs loop while car is not crashing or exit is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5                       #decreasing x coordinate so that car moves left
                elif event.key == pygame.K_RIGHT:
                    x_change = 5     
                elif event.key == pygame.K_SPACE:
                    pygame.mixer.pause()
                    pause()
                elif event.key == pygame.K_m:
                    if mute:
                        pygame.mixer.unpause()
                        mute = False
                    else:
                        pygame.mixer.pause()
                        mute = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        reprint(road_change, level)        #regularly changes environment
        x += x_change               #changes position of car
        y_blockcar1 += speed        #block car moves down


        if x < GAME_W*0.3 or x > GAME_W*0.3 + ROAD_W - 46:   #if car goes out of bounds
            game_exit_status = 2
            return game_exit_status, score, fuel
        
        blockcar(x_blockcar1, y_blockcar1)              #displaying blocking car no.1
        
        if y_blockcar1 > GAME_H*0.6 and swap == 1:      #Now the 2nd block car would be first and a new block car is added 
            y_blockcar2 = 0
            x_blockcar2 = random.randrange(GAME_W*0.3, GAME_W*0.3 + ROAD_W - 45)
            swap = 0
        
        blockcar(x_blockcar2, y_blockcar2)              #displaying blocking car no.2
        y_blockcar2 += speed
        
        if y_blockcar1 > GAME_H:
            y_blockcar1 = y_blockcar2
            x_blockcar1 = x_blockcar2
            swap = 1
            score += 2
            fuel -= 2
            if fuel <= 2:
                game_exit_status = 3
                return game_exit_status, score, fuel
            if speed < 10:
                speed += (score/700)
        
        car(x, y)
        
        if check_crash(x, y, x_blockcar1, y_blockcar1):
            game_exit_status = 2
            return game_exit_status, score, fuel
        
        road_change = (road_change + 1)%3
        
        if pygame.event.get(pygame.USEREVENT + 1):
            isfuelcar = True
            if x_blockcar2 - 50 > GAME_W*0.3:
                x1 = random.randrange(GAME_W*0.3, x_blockcar2 - 50)
            else:
                x1 = random.randrange(x_blockcar2 + 45, GAME_W*0.3 + ROAD_W - 50)
            if x_blockcar2 + 45 < GAME_W*0.3 + ROAD_W - 50:
                x2 = random.randrange(x_blockcar2 + 45, GAME_W*0.3 + ROAD_W - 50)
            else:
                x2 = random.randrange(GAME_W*0.3, x_blockcar2 - 50)
            x_fuel_car = min(x1, x2)
        
        if isfuelcar:
            pfuel_car(x_fuel_car, y_fuel_car)
            y_fuel_car += speed
        
        if check_crash(x, y, x_fuel_car, y_fuel_car):
            isfuelcar = False
            y_fuel_car = 0
            if fuel <= 90:
                fuel += 10
            else:
                fuel = 100
            winning_sound = pygame.mixer.Sound('Sounds/fuel_sound.wav')
            winning_sound.play()
        
        if y_fuel_car > GAME_H:
            y_fuel_car = 0
            isfuelcar = False
        
        if fuel < 30:
            fuel_change(fuel, RED)
        else:
            fuel_change(fuel, WHITE)
        
        if score >= 60 and score < 66:
            level = 2
            displaytext('LEVEL 2!',GAME_W*0.45, GAME_H*0.1, ORANGE, 40)

        display_score(score)
        
        pygame.display.flip()
        CLOCK.tick(60)


while True:
    intro()
    status, score, fuel = game_loop()
    if status == 2:
        crash(score, fuel)
    else:
        no_fuel()

