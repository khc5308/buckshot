import pygame
import random,time
pygame.init()
from fn import round_start, Use_itme, shoot, reset_shell, determine #함수
from fn import gun, player, dealer, image, game #class
from fn import screen


round_start()

#region pos 설정

item_pos = [(720 ,778),(840 ,778),(960 ,778),(1080,778),(720 ,180),(840 ,180),(960 ,180),(1080,180)]

dealer_pos = (780, 0)

gun_pos = (625, 180)

shell_pos = [(1113,418),(1113,449),(1113,480),(1113,511),(1113,541),(1113,572),(1113,603),(1113,634)]

heart_pos_player = [(1209,597),(1225,597),(1241,597),(1257,597)]
heart_pos_dealer = [(1209,460),(1225,460),(1241,460),(1257,460)]
#endregion

#region click_zone 설정
Tmp_width =  image.tmp_img.get_width()
Tmp_height =  image.tmp_img.get_height()
click_zone_1 = pygame.Rect(720, 778, Tmp_width, Tmp_height)
click_zone_2 = pygame.Rect(840, 778, Tmp_width, Tmp_height)
click_zone_3 = pygame.Rect(960, 778, Tmp_width, Tmp_height)
click_zone_4 = pygame.Rect(1080,778, Tmp_width, Tmp_height)
click_zone_5 = pygame.Rect(720, 180, Tmp_width, Tmp_height)
click_zone_6 = pygame.Rect(840, 180, Tmp_width, Tmp_height)
click_zone_7 = pygame.Rect(960, 180, Tmp_width, Tmp_height)
click_zone_8 = pygame.Rect(1080,180, Tmp_width, Tmp_height)

click_zone_gun = pygame.Rect(625, 180,image.gun_45.get_width(), image.gun_45.get_height())

click_zone_playerText = pygame.Rect(907,330, image.Text_Dealer.get_width(), image.Text_Dealer.get_height())
click_zone_dealerText = pygame.Rect(907,680, image.Text_Player.get_width(), image.Text_Player.get_height())

#endregion

running = True
shoot_ready = False
gift_ready = False

move_gun = True

round_dot = [(1219,543),(1239,543),(1262,543)]
           
Items_di= {
    "doll"    : image.doll,
    "gift"    : image.gift,   
    "glasses" : image.glasses,
    "jusagi"  : image.jusagi, 
    "phone"   : image.phone,  
    "pill"    : image.pill,   
    "saw"     : image.saw,    
    "smoke"   : image.smoke,
    " "       : image.tmp_img
}


items_name = list(Items_di.keys())

gun_angle = 0
y_move = 0

player.item[0] = items_name[random.randint(1,len(items_name)-2)]
player.item[1] = items_name[random.randint(1,len(items_name)-2)]
player.item[2] = items_name[random.randint(1,len(items_name)-2)]
player.item[3] = items_name[random.randint(1,len(items_name)-2)]

dealer.item[0] = items_name[random.randint(1,len(items_name)-2)]
dealer.item[1] = items_name[random.randint(1,len(items_name)-2)]
dealer.item[2] = items_name[random.randint(1,len(items_name)-2)]
dealer.item[3] = items_name[random.randint(1,len(items_name)-2)]

image.gun_45_saw = pygame.transform.scale(image.gun_45_saw, (image.gun_45.get_width() ,image.gun_45.get_height()))
image.deler_2    = pygame.transform.scale(image.deler_2   , (image.deler_1.get_width() ,image.deler_1.get_height()))
print(image.deler_1.get_width(), image.deler_1.get_height)
print(image.deler_2.get_width(), image.deler_2.get_height)


# 메인 루프
clock = pygame.time.Clock()
while running:

    screen.blit(image.background, (0, 0))
    screen.blit(image.dot, round_dot[game.round])



    # 이벤트 get
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

        elif event.type == pygame.KEYDOWN:
            match(event.key):
                case pygame.K_F1:
                    player.item[0] = items_name[0]
                    player.item[1] = items_name[1]
                    player.item[2] = items_name[2]
                    player.item[3] = items_name[3]
                case pygame.K_F2:
                    player.item[0] = items_name[4]
                    player.item[1] = items_name[5]
                    player.item[2] = items_name[6]
                    player.item[3] = items_name[7]
                case pygame.K_r:
                    game.round += 1
                    game.round %= 3


        if event.type != pygame.MOUSEBUTTONDOWN:
            continue

        
        print(event.pos)
        if shoot_ready and not move_gun and game.isPlayerTurn:
            if click_zone_playerText.collidepoint(event.pos):
                print("Shoot dealer")
                shoot(dealer)
                shoot_ready = False
                move_gun = True
            elif click_zone_dealerText.collidepoint(event.pos):
                print("Shoot Player")
                shoot(player)
                shoot_ready = False
                move_gun = True
            else:
                print("None")

        elif game.isPlayerTurn or not game.isPlayerTurn:
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
                    print("dealer 0번 아이템 사용 시도")
                elif click_zone_6.collidepoint(event.pos):
                    Use_itme(dealer,1)
                    print("dealer 1번 아이템 사용 시도")
                elif click_zone_7.collidepoint(event.pos):
                    Use_itme(dealer,2)
                    print("dealer 2번 아이템 사용 시도")
                elif click_zone_8.collidepoint(event.pos):
                    Use_itme(dealer,3)
                    print("dealer 3번 아이템 사용 시도")
            
    if not gun.shell:
        reset_shell()
    
    if player.hp <= 0 or dealer.hp <= 0:
        round_start()


    if not game.isPlayerTurn:
        shoot([dealer,player][determine()])
        

    #region 총 클릭 시 text 그리기
    if shoot_ready and game.isPlayerTurn:
        screen.blit(image.Text_Dealer, (907,330))
        screen.blit(image.Text_Player, (907,680))
    #endregion

    #region heart, shell 그리기
    for i in range(player.max_hp):
        screen.blit(image.heart if i < player.hp else image.heart_break, heart_pos_player[i])

    for i in range(dealer.max_hp):
        screen.blit(image.heart if i < dealer.hp else image.heart_break, heart_pos_dealer[i])

    for i in range(1,len(gun.shell)+1):
        screen.blit(image.real if gun.shell[-i] else image.fake, shell_pos[i-1])
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

    screen.blit([image.deler_1,image.deler_1,image.deler_2][game.round],dealer_pos)
    
    #region 총 애니메이션 및 그리기

    saw_OR_nomal_45 = image.gun_45_saw if gun.saw else image.gun_45
    saw_OR_nomal_90 = image.gun_90_saw if gun.saw else image.gun_90

    if shoot_ready:
        turn_value = 1 if game.isPlayerTurn else -1

        if gun_angle < -45 or gun_angle > 135: 
            time.sleep(0.1)
            move_gun = False
            gun_angle = y_move = 0

        if move_gun:
            gun_angle += -3 * turn_value
            y_move += 3 if game.isPlayerTurn else 1
            r = pygame.transform.rotate(saw_OR_nomal_45, gun_angle)
            rr = r.get_rect(center=(saw_OR_nomal_45).get_rect(topleft=gun_pos).center)
            rr.y += 10 * y_move * turn_value
            screen.blit(r, rr.topleft)
        else:
            screen.blit(saw_OR_nomal_90 if game.isPlayerTurn else pygame.transform.rotate(saw_OR_nomal_90, 180), (906, 770) if game.isPlayerTurn else (856,-200))
    else:
        screen.blit(saw_OR_nomal_45, gun_pos)


    #endregion


    # 배경 그리기
    screen.blit(image.light, (260, 0))

    clock.tick(60)
    pygame.display.update() # 화면 업데이트

pygame.quit()