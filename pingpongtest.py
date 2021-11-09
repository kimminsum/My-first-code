import pygame
import random
from tkinter import *
from pygame import mixer
  
# Starting the mixer
mixer.init()
  
# Loading the song
mixer.music.load("alice.mp3")
  
# Setting the volume
mixer.music.set_volume(0.3)
  
# Start playing the song
mixer.music.play()

##################################################################
pygame.init()

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        # create button, link it to clickExitButton()
        exitButton = Button(self, text="끝", command=self.clickExitButton)

        # place button at (0,0)
        exitButton.place(x=50, y=80)

    def clickExitButton(self):
        exit()

#스크린 보여주기
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 게임 제목
pygame.display.set_caption("Mingame")
pygame.time.delay(1000)
#FPS
clock = pygame.time.Clock()

#배경 이미지 
background = pygame.image.load("D:/정보발표/codes/Mingame/background.png")
##################################################################################
#캐릭터
character = pygame.image.load("D:/정보발표/codes/Mingame/character.png")
character_size = character.get_rect().size #이미지 크기
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - (character_height / 2)

# enemy character
enemy = pygame.image.load("D:/정보발표/codes/Mingame/enemy.png")
enemy_size = enemy.get_rect().size #이미지 크기
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)
enemy_y_pos = -screen_height - (enemy_height / 2)
###################################################################################
#이동거리
to_x = 0

#이동속도
character_speed = 0.6
###################################################################################
#시작 시간
start_ticks = pygame.time.get_ticks()

#총 남은 시간
total_time = 300
enemy_speed = 2
###################################################################################
#폰트 정의
game_font = pygame.font.Font(None, 40) # (폰트 , 크기)

#이벤트 루프
running = True #겜 진행중 ?
while running:

    enemy_y_pos += enemy_speed
    if enemy_y_pos >= 530 :
        enemy_y_pos = 0
        enemy_x_pos = random.randrange(35, 410)
        enemy_speed += 0.1

    dt = clock.tick(60) #게임화면 초당 프레임 수 설정
    # 1초 동안 100 이동 
    #10 fps : 1초에 10번동작 ->10*10 = 100

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창 닫기 
            running = False

        if event.type == pygame.KEYDOWN: #키눌림
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

                #스페이스바 == 끄기
            elif event.key == pygame.K_SPACE:
                running = False

        if event.type == pygame.KEYUP: #방향키 때면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

        # fps 움직임
    character_x_pos += to_x * dt

# border me
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

# border enemy
    if enemy_x_pos < 0:
        enemy_x_pos = 0
    elif enemy_x_pos > screen_width - enemy_width:
        enemy_x_pos = screen_width - enemy_width

    if enemy_y_pos < 0:
        enemy_y_pos = 0
    elif enemy_y_pos > screen_height - enemy_height:
        enemy_y_pos = screen_height - enemy_height   


    # crashing me
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    # crashing enemy
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos 


    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("crashed!")
        running = False

    #screen.fill((0, 0, 0))

    screen.blit(background, (0, 0)) #배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    #timer
    passed_time = (pygame.time.get_ticks() - start_ticks) / 1000

    timer = game_font.render(str(int(total_time - passed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))

    #시간 지남 = 패배
    if total_time - passed_time <= 0:
        print("TIME OUT")
        running = False
        
    pygame.display.update() #게임화면 다시

#대기
pygame.time.delay(2000)

#End
root = Tk()
app = Window(root)
root.wm_title("Game Over")
root.geometry("200x200")
root.mainloop()

#게임 종료
pygame.quit()