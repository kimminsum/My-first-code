import pygame
#####################################################################
pygame.init()

#스크린 보여주기
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 게임 제목
pygame.display.set_caption("Mingame")

#FPS
clock = pygame.time.Clock()
#####################################################################

# 게임 리셋(background, image, x,y, speed, font, etc)
# 이벤트 처리
# 게임 캐릭터 위치 정의
# 충돌 처리
# 화면 생성
pygame.display.update()