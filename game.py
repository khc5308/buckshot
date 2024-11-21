import pygame
import random
from fn import game_start,Use_itme
from fn import gun, player, dealer

# 초기화
pygame.init()
game_start()
# 화면 크기 설정
screen_width, screen_height = 1535, 863 
screen = pygame.display.set_mode((screen_width, screen_height))

#이미지 로드
#
#배경
background = pygame.image.load("./image/back.png")
#아이템
tmp_img = pygame.image.load("./image/tmp.png")
doll = pygame.image.load("./image/item/doll.png")
gift = pygame.image.load("./image/item/gift.png")
glasses = pygame.image.load("./image/item/glasses.png")
jusagi = pygame.image.load("./image/item/jusagi.png")
pill = pygame.image.load("./image/item/pill.png")
saw = pygame.image.load("./image/item/saw.png")
smoke = pygame.image.load("./image/item/smoke.png")
#하트
heart = pygame.image.load("./image/heart/heart1.png")
heart_break = pygame.image.load("./image/heart/heart0.png")
#탄약
real = pygame.image.load("./image/shell/real.png")
fake = pygame.image.load("./image/shell/fake.png")

Items_di = {" ":tmp_img,"doll" : doll, "gift" : gift, "glasses" : glasses, "jusagi" : jusagi, "pill":pill, "saw":saw, "smoke":smoke}

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

heart_pos_player = [(1209,597),(1225,597),(1241,597),(1257,597)]
heart_pos_dealer = [(1209,460),(1225,460),(1241,460),(1257,460)]

shell_pos = [(1102,418),(1102,447)]

items_name = list(Items_di.keys())
player.item[0] = items_name[random.randint(1,len(items_name)-1)]
player.item[1] = items_name[random.randint(1,len(items_name)-1)]
player.item[2] = items_name[random.randint(1,len(items_name)-1)]
player.item[3] = items_name[random.randint(1,len(items_name)-1)]

# 메인 루프
running = True
while running:
    # 배경 그리기
    screen.blit(background, (0, 0))
    
    # 이벤트 get
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            if click_zone_1.collidepoint(event.pos):
                Use_itme(player,0)
                print("0번 아이템 사용")
            elif click_zone_2.collidepoint(event.pos):
                Use_itme(player,1)
                print("1번 아이템 사용")
            elif click_zone_3.collidepoint(event.pos):
                Use_itme(player,2)
                print("2번 아이템 사용")
            elif click_zone_4.collidepoint(event.pos):
                Use_itme(player,3)
                print("3번 아이템 사용")
            else:
                print("None")


    # heart 그리기
    for i in range(player.max_hp):
        if i < player.hp:
            screen.blit(heart, heart_pos_player[i])
        else:
            screen.blit(heart_break, heart_pos_player[i])
    for i in range(dealer.max_hp):
        if i < dealer.hp:
            screen.blit(heart, heart_pos_dealer[i])
        else:
            screen.blit(heart_break, heart_pos_dealer[i])

    for i in range(1,3):
        screen.blit(real if gun.shell[-i] else fake, shell_pos[i-1])

    #아이템 그리기
    screen.blit(Items_di[player.item[0]], item_pos_1)
    screen.blit(Items_di[player.item[1]], item_pos_2)
    screen.blit(Items_di[player.item[2]], item_pos_3)
    screen.blit(Items_di[player.item[3]], item_pos_4)

    # 화면 업데이트
    pygame.display.update()

pygame.quit()   