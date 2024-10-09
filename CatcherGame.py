import pygame
import sys
from pygame import mixer
from random import randint
import keyboard
from time import time as current_time
import time


pygame.init()
mixer.init()

def setings():
                    global ScreenWidth, ScreenHeight, FPS, BallC, RectC, Backraund, CircleRadius, RectWhigh, RectHight
                    global BonusWidth, BonusHeight, Triangel_widht, Triangel_Hight, BallSpeed, counter, NextLevel, X
                    global AddLevel, Lives, duration, start_time, timer_active, BonusChencs, BonusBool, FrameNum, exit_condition, key_states, counterer
                    global GameOver, key_state, button_state, TimeLived, MoveY, MoveX, GameOverY, d, pause, LevelUpBool
                    global button_state2, key_state, RectSpeed, TriangelSpoawn, TriengelSpeed, SpeedBallSpeed, SpeedBallBool
                    global CircleX, CircleY, RectX, RectY, BonusX, BonusY, BonusSpeed, GameOverScreenY, TriangelY, SpeedBallRadius, SpeedBallX, SpeedBallY, SpeedBallC
                    
                    # Colors:
                    BallC = 209, 186, 109
                    RectC = 109, 169, 209
                    Backraund = 103, 101, 105
                    SpeedBallC = 123, 243, 213


                    # Sizes:
                    ScreenWidth = 600
                    ScreenHeight = 400
                    CircleRadius = 25
                    RectWhigh = ScreenWidth // 10 * 4
                    RectHight = 60
                    BonusWidth = 50
                    BonusHeight = 50
                    Triangel_widht = 60
                    Triangel_Hight = 60
                    SpeedBallRadius = 7

                    # Variables:
                    BallSpeed = 3
                    counter = 0
                    NextLevel = 5
                    X = 10
                    AddLevel = True
                    Lives = 5
                    FPS = 60
                    duration = 3.10
                    start_time = None
                    timer_active = False
                    BonusChencs = None
                    BonusBool = False
                    FrameNum = 0
                    GameOver = False
                    key_state = False
                    button_state = False
                    TimeLived = 0
                    MoveY = 0
                    MoveX = 0
                    GameOverY = -50
                    d = 0
                    pause = False
                    button_state2 = False
                    key_state = False
                    RectSpeed = 10
                    TriangelSpoawn = False
                    TriengelSpeed = 15
                    SpeedBallSpeed = 10
                    SpeedBallBool = False
                    LevelUpBool = False


                    # Coordinates:
                    CircleX = randint(CircleRadius, ScreenWidth - CircleRadius)
                    CircleY = 0 - CircleRadius
                    RectX = ScreenWidth / 2 - RectWhigh / 2
                    RectY = ScreenHeight - RectHight - 15
                    BonusX = randint(CircleRadius, ScreenWidth - CircleRadius)
                    BonusY = 0 - BonusHeight
                    BonusSpeed = BallSpeed + 2
                    GameOverScreenY = ScreenHeight
                    TriangelY = ScreenHeight - 60
                    SpeedBallY = 100
                    SpeedBallX = 0

                    counterer = 2
                    key_states = {'=': False, '-': False}
                    exit_condition = False

setings()

PlayButton = pygame.image.load("Game_Assets\Play button.jpg")

# Set up display
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption("Catcher Game")

# Create a transparent surface (rect)
transparent_rect = pygame.Surface((200, 100), pygame.SRCALPHA)
transparent_rect.fill((255, 0, 255, 0))  # RGB values with alpha (0-255)

# Position of the transparent rectangle
rect_position = (100, 100)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if rect_position[0] < mouse_pos[0] < rect_position[0] + transparent_rect.get_width() and \
                    rect_position[1] < mouse_pos[1] < rect_position[1] + transparent_rect.get_height():
                
                import pygame
                import sys
                from pygame import mixer
                from random import randint
                import keyboard
                from time import time as current_time
                import time


                pygame.init()
                pygame.font.init()
                mixer.init()

                
                setings()

                # Music & Sounds:
                Catch_SFX = pygame.mixer.Sound("Game_Assets\Catch.wav")
                Catch_SFX.set_volume(0.5)
                Fail_SFX = pygame.mixer.Sound("Game_Assets\MissSFX.wav")
                Fail_SFX.set_volume(0.6)
                Bonus_SFX = pygame.mixer.Sound("Game_Assets\Bonus_SFX.wav")
                Bonus_SFX.set_volume(0.2) 
                LevelUp_SFX = pygame.mixer.Sound('Game_Assets\LevelUP_SFX.mp3')

                BackraundMusic = pygame.mixer.Sound('Game_Assets\BackRaundMusic.mp3')
                BackraundMusic.set_volume(0.5)
                GameOverMusic = pygame.mixer.Sound('Game_Assets\GameOverMusic.mp3')
                GameOverMusic.set_volume(0)

                # Fonts:
                font = pygame.font.Font(None, 36)

                #Time:
                MinusTime = round(current_time(), 2)

                #PNGS
                LevelUp = pygame.image.load('Game_Assets\LevelUpjpg-removebg-preview.png')

                def handle_keys():
                    def on_key_release(event):
                        global counterer
                        if event.name in key_states and not key_states[event.name]:
                            if event.name == '=':
                                counterer += 1
                                BackraundMusic.set_volume(counterer/10)
                                GameOverMusic.set_volume(counterer/10)
                            elif event.name == '-':
                                counterer = max(0, counterer - 1)
                                BackraundMusic.set_volume(counterer/10)
                                GameOverMusic.set_volume(counterer/10)

                    def on_key_press(event):
                        if event.name in key_states:
                            key_states[event.name] = True

                    def on_key_release_reset(event):
                        if event.name in key_states:
                            key_states[event.name] = False

                    keyboard.on_release(on_key_release)
                    keyboard.on_press(on_key_press)
                    keyboard.on_release(on_key_release_reset)


                def toggle_key_f():
                    global key_state
                    global button_state
                    if keyboard.is_pressed('f'):
                        if not key_state:
                            button_state = not button_state
                        key_state = True
                    else:
                        key_state = False

                win = pygame.display.set_mode((ScreenWidth, ScreenHeight))

                last_color_change_time = time.time()
                color_change_interval = 10

                Clock = pygame.time.Clock()
                BackraundMusic.play(-1)
                #GameOverMusic.play(-1)

                while True:
                    handle_keys()
                    Clock.tick(FPS)
                    FrameNum += 1

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()  # Exit on window close
                        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()  # Exit on pressing the ESC key

                    keys = pygame.key.get_pressed()


                    if keys[pygame.K_r]:
                        setings()
                        mixer.stop()
                        pygame.time.delay(1500)
                        BackraundMusic.play(-1)

                    win.fill(Backraund)
                ####################################################################
                    if not(GameOver):
                        if not(button_state2):

                            current_time = time.time()
                            if current_time - last_color_change_time >= color_change_interval and not(SpeedBallBool):
                                    SpeedBallX = randint(SpeedBallRadius, ScreenWidth - SpeedBallRadius)
                                    SpeedBallY = 0
                                    SpeedBallBool = True
                                    last_color_change_time = current_time

                            if keys[pygame.K_a] and RectX > 0:
                                RectX -= RectSpeed

                            if keys[pygame.K_d] and RectX + RectWhigh < ScreenWidth:
                                RectX += RectSpeed

                            BonusY += BonusSpeed + 1
                            CircleY += BallSpeed
                            TimeLived = round((round(current_time, 2) - MinusTime), 2)

                            counterX = RectX + RectWhigh // 2
                            counterY = RectY + RectHight // 2

                ####################################################################

                    circle = pygame.draw.circle(
                        win, (BallC), (CircleX, CircleY), CircleRadius
                    )

                    Bonus = pygame.draw.rect(win, (10, 10, 250), (BonusX, BonusY, BonusWidth, BonusHeight))

                    poly = pygame.draw.polygon

                    Rect = pygame.draw.rect(
                        win, (RectC), (RectX, RectY, RectWhigh, RectHight)
                    )
                    
                    if SpeedBallBool:
                        SpeedBall = pygame.draw.circle(
                        win, (SpeedBallC), (SpeedBallX, SpeedBallY), SpeedBallRadius)
                        if not(GameOver):
                            SpeedBallY += 5
                        
                        if SpeedBall.colliderect(Rect):
                            LevelUp_SFX.play()
                            SpeedBallBool = False
                            RectSpeed += 3
                            LevelUpBool = True
                        if SpeedBallY > ScreenHeight: SpeedBallBool = False

                    Score = font.render(f'Score: {counter}', True, (250, 250, 250))
                    Score_rect = Score.get_rect(center=(counterX, counterY))
                    LivesText = font.render(f'Lives: {Lives}', True, (250, 0, 0))
                    LivesText = pygame.transform.scale(LivesText, (200, 50))
                    ShowGameOver = font.render('Game Over', True, (237, 47, 47))
                    win.blit(LivesText, (10, 10))
                    win.blit(Score, Score_rect)
                    if LevelUpBool: win.blit(LevelUp, (RectX + 150, RectY - 30))

                ########################################

                    if GameOver:
                        pygame.draw.rect(win, (0, 0, 0), (0,GameOverScreenY, ScreenWidth, ScreenHeight))
                        if GameOverScreenY != 0:
                            GameOverScreenY -= 5
                        else:Lives = -1

                        counterMoveX = (ScreenWidth // 2)

                        if counterY >= ScreenHeight // 10 * 4:
                            counterY -= 4

                        if (counterMoveX - counterX) > 0:
                            if counterX != counterMoveX:
                                counterX += 4

                        if (counterMoveX - counterX) < 0:
                            if counterX != counterMoveX:
                                counterX -= 4

                        if GameOverY != ScreenHeight//10 * 2:
                            GameOverY += 2

                        ShowGameOver = pygame.transform.scale(ShowGameOver, (200, 50))
                        win.blit(ShowGameOver, (ScreenWidth // 2 - 100, GameOverY))
                        
                        win.blit(ShowTimeLived, (counterMoveX - 70, counterY + 25))

                ########################################
                    win.blit(Score, Score_rect)

                    GetFPS = round((Clock.get_fps()))

                    if circle.colliderect(Rect):
                        CircleY = 10
                        CircleX = randint(CircleRadius, ScreenWidth - CircleRadius)
                        counter += 1
                        Catch_SFX.play()

                    if circle.top > ScreenHeight:
                        Fail_SFX.play()
                        Lives -= 1
                        CircleY = 0
                        CircleX = randint(CircleRadius, ScreenWidth - CircleRadius)
                        if GameOver: mixer.stop()

                    if Rect.colliderect(Bonus):
                        Bonus_SFX.play()
                        BonusX = randint(0, ScreenWidth - BonusWidth)
                        BonusY = 0 - BonusHeight
                        counter += 2

                    if BonusY > ScreenHeight:
                        BonusY = 0 - 500
                        BonusX = randint(0, ScreenWidth - BonusWidth)

                    if BonusY > 0 - BonusHeight: BonusSpeed = BonusSpeed = BallSpeed + 2
                    elif BonusY > 0 and not(GameOver): BonusSpeed = 1


                    if counter >= X:
                        BallSpeed += 1
                        
                        X += 10
                        
                    if Lives == 0:
                        BallSpeed = 0
                        GameOver = True
                        mixer.stop()
                        GameOverMusic.play(-1)

                    
                    
                    toggle_key_f()
                    ShowFPS = font.render(f'FPS: {GetFPS}', True, (250, 250, 250))
                    ShowCircleY = font.render(f'Ball_Y: {CircleY}', True, (250, 250, 250))
                    ShowCircleX = font.render(f'Ball_X: {CircleX}', True, (255, 255, 255))
                    ShowBallSpeed = font.render(f'BallSpeed: {BallSpeed}', True, (255, 255, 255))
                    ShowTimeLived = font.render(f'TimeLived: {TimeLived}', True, (255, 255, 255))

                    ShowFPS = pygame.transform.scale(ShowFPS, (50,15))
                    ShowCircleY = pygame.transform.scale(ShowCircleY, (70,17))
                    ShowCircleX = pygame.transform.scale(ShowCircleX, (70,17))
                    ShowBallSpeed = pygame.transform.scale(ShowBallSpeed, (70,17))
                    ShowTimeLived = pygame.transform.scale(ShowTimeLived, (145, 17))
                    
                    if button_state:
                        win.blit(ShowFPS, (0, 60))
                        win.blit(ShowCircleY, (0, 77))
                        win.blit(ShowCircleX, (0, 97))
                        win.blit(ShowBallSpeed, (0, 117))
                        win.blit(ShowTimeLived, (0, 137))

                    if keyboard.is_pressed('p'):
                        if not key_state2:
                            button_state2 = not button_state2
                        key_state2 = True
                    else:
                        key_state2 = False


                    if button_state2:
                        s = pygame.Surface((1000,750))
                        s.set_alpha(128)
                        s.fill((0,0,0))
                        win.blit(s, (0,0))

                    
                    pygame.display.update()


             # Draw background
    screen.fill((255, 255, 255))

                # Draw transparent rectangle
    screen.blit(transparent_rect, rect_position)
    screen.blit(PlayButton, rect_position)

                    # Update display
    pygame.display.flip()

                    # Cap the frame rate
    pygame.time.Clock().tick(60)
