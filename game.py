import pygame
from fn import game_start,Use_itme
from fn import gun, player, dealer

# 초기화
pygame.init()
game_start()
# 화면 크기 설정
screen_width, screen_height = 1920, 1080
screen = pygame.display.set_mode((screen_width, screen_height))

#이미지 로드
#
#배경
background = pygame.image.load("./image/back.png")
#아이템
tmp_img = pygame.image.load("./image/tmp.png")
glasses = pygame.image.load("./image/item/glasses.png")


item_pos_1=(720,770)
item_pos_2=(840,770)
item_pos_3=(960, 770)
item_pos_4=(1080,770)
# item_pos_5=(,)
# item_pos_6=(,)
# item_pos_7=(,)
# item_pos_8=(,)

click_zone_1 = pygame.Rect(720, 770, tmp_img.get_width(), tmp_img.get_height())
click_zone_2 = pygame.Rect(840, 770, tmp_img.get_width(), tmp_img.get_height())
click_zone_3 = pygame.Rect(960, 770, tmp_img.get_width(), tmp_img.get_height())
click_zone_4 = pygame.Rect(1080, 770,tmp_img.get_width(), tmp_img.get_height())
# click_zone_4 = pygame.Rect(, ,tmp_img.get_width(), tmp_img.get_height())
# click_zone_4 = pygame.Rect(, ,tmp_img.get_width(), tmp_img.get_height())
# click_zone_4 = pygame.Rect(, ,tmp_img.get_width(), tmp_img.get_height())
# click_zone_4 = pygame.Rect(, ,tmp_img.get_width(), tmp_img.get_height())



screen.blit(background, (0, 0))
# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if click_zone_1.collidepoint(event.pos):
                Use_itme(player,1)
            elif click_zone_2.collidepoint(event.pos):
                Use_itme(player,2)
            elif click_zone_3.collidepoint(event.pos):
                Use_itme(player,3)
            elif click_zone_4.collidepoint(event.pos):
                Use_itme(player,4)
            else:
                print("아무곳")
    
    # 화면 업데이트
    pygame.display.update()

pygame.quit()