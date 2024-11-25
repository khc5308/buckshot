import pygame
import random
from fn import round_start, Use_itme, shoot, reset_shell
from fn import gun, player, dealer, game

pygame.init()
round_start()

#region 이미지 로드

#배경
background = pygame.image.load("./image/back.png")
# 총 (45)
gun_45 = pygame.image.load("./image/gun/gun45.png")
#아이템
tmp_img = pygame.image.load("./image/item/tmp.png")
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

#글자
font = pygame.font.Font("./fonts/PretendardVariable.ttf", 36)
Text_Dealer = font.render("Dealer", True, (255,255,255))
Text_Player = font.render("Player", True, (255,255,255))

#글자
dot = pygame.image.load("./image/dot.png")


#endregion 

#region pos 설정

item_pos = [(720 ,770),(840 ,770),(960 ,770),(1080,770),(720 ,180),(840 ,180),(960 ,180),(1080,180)]

gun_pos = (625, 180)

shell_pos = [(1113,418),(1113,449),(1113,480),(1113,511),(1113,541),(1113,572),(1113,603),(1113,634)]

heart_pos_player = [(1209,597),(1225,597),(1241,597),(1257,597)]
heart_pos_dealer = [(1209,460),(1225,460),(1241,460),(1257,460)]
#endregion

#region click_zone 설정
click_zone_1 = pygame.Rect(720, 770, tmp_img.get_width(), tmp_img.get_height())
click_zone_2 = pygame.Rect(840, 770, tmp_img.get_width(), tmp_img.get_height())
click_zone_3 = pygame.Rect(960, 770, tmp_img.get_width(), tmp_img.get_height())
click_zone_4 = pygame.Rect(1080,770, tmp_img.get_width(), tmp_img.get_height())
click_zone_5 = pygame.Rect(720, 180, tmp_img.get_width(), tmp_img.get_height())
click_zone_6 = pygame.Rect(840, 180, tmp_img.get_width(), tmp_img.get_height())
click_zone_7 = pygame.Rect(960, 180, tmp_img.get_width(), tmp_img.get_height())
click_zone_8 = pygame.Rect(1080,180, tmp_img.get_width(), tmp_img.get_height())

click_zone_gun = pygame.Rect(625, 180,gun_45.get_width(), gun_45.get_height())

click_zone_playerText = pygame.Rect(907,330, Text_Dealer.get_width(), Text_Dealer.get_height())
click_zone_dealerText = pygame.Rect(907,680, Text_Player.get_width(), Text_Player.get_height())


#endregion


running = True
shoot_ready = False
gift_ready = False
round_dot = [(1219,545)]
Items_di = {" ":tmp_img, "doll":doll, "gift":gift, "glasses":glasses, "jusagi":jusagi, "pill":pill, "saw":saw, "smoke":smoke}
items_name = list(Items_di.keys())
screen_width, screen_height = 1920, 1080 


screen = pygame.display.set_mode((screen_width, screen_height))

player.item[0] = items_name[random.randint(1,len(items_name)-1)]
player.item[1] = items_name[random.randint(1,len(items_name)-1)]
player.item[2] = items_name[random.randint(1,len(items_name)-1)]
player.item[3] = items_name[random.randint(1,len(items_name)-1)]

dealer.item[0] = items_name[random.randint(1,len(items_name)-1)]
dealer.item[1] = items_name[random.randint(1,len(items_name)-1)]
dealer.item[2] = items_name[random.randint(1,len(items_name)-1)]
dealer.item[3] = items_name[random.randint(1,len(items_name)-1)]

# 메인 루프
while running:
    # 배경 그리기
    screen.blit(background, (0, 0))
    screen.blit(gun_45, (625, 180))

    # 이벤트 get
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

        if event.type != pygame.MOUSEBUTTONDOWN:
            continue

        
        print(event.pos)
        if shoot_ready:
            if click_zone_playerText.collidepoint(event.pos):
                print("Shoot dealer")
                shoot(dealer)
                shoot_ready = False
            elif click_zone_dealerText.collidepoint(event.pos):
                print("Shoot Player")
                shoot(player)
                shoot_ready = False
            else:
                print("None")

        elif game.isPlayerTurn:
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
            elif click_zone_gun.collidepoint(event.pos):
                print("총")
                shoot_ready = True
            else:
                print("None")

            #아드레날린 사용 시 딜러 아이템 사용 가능
            if player.adrenaline:
                if click_zone_5.collidepoint(event.pos):
                    Use_itme(dealer,0)
                    print("dealer 0번 아이템 사용")
                elif click_zone_6.collidepoint(event.pos):
                    Use_itme(dealer,1)
                    print("dealer 1번 아이템 사용")
                elif click_zone_7.collidepoint(event.pos):
                    Use_itme(dealer,2)
                    print("dealer 2번 아이템 사용")
                elif click_zone_8.collidepoint(event.pos):
                    Use_itme(dealer,3)
                    print("dealer 3번 아이템 사용")
            
    #region 총 클릭 시 text 그리기
    if shoot_ready:
        screen.blit(Text_Dealer, (907,330))
        screen.blit(Text_Player, (907,680))
    #endregion

    if gift_ready:
        pass
        # screen.blit()

    screen.blit(dot, round_dot[game.round])

    #region heart, shell 그리기
    for i in range(player.max_hp):
        screen.blit(heart if i < player.hp else heart_break, heart_pos_player[i])

    for i in range(dealer.max_hp):
        screen.blit(heart if i < dealer.hp else heart_break, heart_pos_dealer[i])

    for i in range(1,len(gun.shell)+1):
        screen.blit(real if gun.shell[-i] else fake, shell_pos[i-1])
    #endregion

    #region 아이템 그리기

    #player
    screen.blit(Items_di[player.item[0]], item_pos[0])
    screen.blit(Items_di[player.item[1]], item_pos[1])
    screen.blit(Items_di[player.item[2]], item_pos[2])
    screen.blit(Items_di[player.item[3]], item_pos[3])
    #dealer
    screen.blit(Items_di[dealer.item[0]], item_pos[4])
    screen.blit(Items_di[dealer.item[1]], item_pos[5])
    screen.blit(Items_di[dealer.item[2]], item_pos[6])
    screen.blit(Items_di[dealer.item[3]], item_pos[7])

    #endregion

    if not gun.shell:
        reset_shell()
    
    if player.hp <= 0 or dealer.hp <= 0:
        round_start()

    pygame.display.update() # 화면 업데이트

pygame.quit()   