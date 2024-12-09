import pygame, time
pygame.init()
from souse.fn import round_start, Use_itme, shoot, reset_shell, determine, give_item, draw_item, draw_heart,draw_dealer ,game_end #함수
from souse.fn import gun, player, dealer, image, game, pos #class
from souse.fn import screen, item_name

#region 변수 설정

running = True
shoot_ready = False
gift_ready = False
move_gun = True

gun_angle = 0
y_move = 0

clock = pygame.time.Clock()
#endregion

screen.blit(image.background, (0, 0))
screen.blit(image.dot, pos.round_dot[game.round])
screen.blit(image.light, pos.light)

round_start()

# 메인 루프
while running:
    screen.blit(image.background, (0, 0))
    screen.blit(image.dot, pos.round_dot[game.round])

    # 이벤트 get
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.KEYDOWN:
            match(event.key):
                case pygame.K_F1:
                    player.item[0] = item_name[0]
                    player.item[1] = item_name[1]
                    player.item[2] = item_name[2]
                    player.item[3] = item_name[3]
                case pygame.K_F2:
                    player.item[0] = item_name[4]
                    player.item[1] = item_name[5]
                    player.item[2] = item_name[6]
                    player.item[3] = item_name[7]
                case pygame.K_F3:
                    player.item[0] = item_name[8]
                    player.item[1] = " "
                    player.item[2] = " "
                    player.item[3] = " "
                case pygame.K_F11:
                    dealer.item[0] = item_name[0]
                    dealer.item[1] = item_name[1]
                    dealer.item[2] = item_name[2]
                    dealer.item[3] = item_name[3]
                case pygame.K_F12:
                    dealer.item[0] = item_name[4]
                    dealer.item[1] = item_name[5]
                    dealer.item[2] = item_name[6]
                    dealer.item[3] = item_name[7]
                case pygame.K_r:
                    game.round += 1
                case pygame.K_s:
                    screen.blit(image.background,(0,0))
                    for i in range(1,len(gun.shell)+1):
                        screen.blit(image.real if gun.shell[-i] else image.fake, pos.shell[i-1])
                    screen.blit(image.light,pos.light)
                    pygame.display.update()

                    time.sleep(2)
                


        if event.type != pygame.MOUSEBUTTONDOWN:
            continue

        
        print(event.pos)
        if shoot_ready and not move_gun and game.isPlayerTurn:
            if pos.click_zone_playerText.collidepoint(event.pos):
                shoot(dealer)
                shoot_ready = False
                move_gun = True
            elif pos.click_zone_dealerText.collidepoint(event.pos):
                shoot(player)
                shoot_ready = False
                move_gun = True
            else:
                print("None")

        elif game.isPlayerTurn:
            if pos.click_zone[0].collidepoint(event.pos):
                Use_itme(player,0)
                print("0번 아이템 사용")
            elif pos.click_zone[1].collidepoint(event.pos):
                Use_itme(player,1)
                print("1번 아이템 사용")
            elif pos.click_zone[2].collidepoint(event.pos):
                Use_itme(player,2)
                print("2번 아이템 사용")
            elif pos.click_zone[3].collidepoint(event.pos):
                Use_itme(player,3)
                print("3번 아이템 사용")
            elif pos.click_zone_gun.collidepoint(event.pos):
                print("총")
                shoot_ready = True
            else:
                print("None")

            #아드레날린 사용 시 딜러 아이템 사용 가능
            if player.adrenaline:
                if pos.click_zone[4].collidepoint(event.pos):
                    Use_itme(dealer,0)
                    print("dealer 4번 아이템 사용 시도")
                elif pos.click_zone[5].collidepoint(event.pos):
                    Use_itme(dealer,1)
                    print("dealer 5번 아이템 사용 시도")
                elif pos.click_zone[6].collidepoint(event.pos):
                    Use_itme(dealer,2)
                    print("dealer 6번 아이템 사용 시도")
                elif pos.click_zone[7].collidepoint(event.pos):
                    Use_itme(dealer,3)
                    print("dealer 7번 아이템 사용 시도")

    if dealer.hp <= 0:
        round_start()
        pygame.display.update()

    if player.hp <= 0: 
        game_end("You Lose..")

    if not game.isPlayerTurn:
        shoot_ready = True
        move_gun = True
    

    #region 총 클릭 시 text 그리기
    if shoot_ready and game.isPlayerTurn:
        screen.blit(image.Text_Dealer, (907,330))
        screen.blit(image.Text_Player, (907,680))
    #endregion

    #region heart, shell, item, dealer 그리기
    draw_dealer()
    draw_heart()
    draw_item()
    
 
    #endregion
    
    #region 총 애니메이션 및 그리기

    saw_OR_nomal_45 = image.gun_45_saw if gun.saw else image.gun_45
    saw_OR_nomal_90 = image.gun_90_saw if gun.saw else image.gun_90

    if shoot_ready and gun.shell:
        turn_value = 1 if game.isPlayerTurn else -1

        if gun_angle < -45 or gun_angle > 135: 
            time.sleep(0.1)
            move_gun = False
            gun_angle = y_move = 0

        if move_gun:
            gun_angle += -3 * turn_value
            y_move += 3 if game.isPlayerTurn else 1
            r = pygame.transform.rotate(saw_OR_nomal_45, gun_angle)
            rr = r.get_rect(center=(saw_OR_nomal_45).get_rect(topleft=pos.gun).center)
            rr.y += 10 * y_move * turn_value
            screen.blit(r, rr.topleft)
        else:
            screen.blit(saw_OR_nomal_90 if game.isPlayerTurn else pygame.transform.rotate(saw_OR_nomal_90, 180), (906, 770) if game.isPlayerTurn else (856,-200))
    elif not gun.shell:
        give_item()
    else:
        screen.blit(saw_OR_nomal_45, pos.gun)


    #endregion    

    if not game.isPlayerTurn and not move_gun:
        shoot([dealer,player][determine()])
        shoot_ready = False
        move_gun = True


    if not gun.shell:
        reset_shell()

    # 배경 그리기
    screen.blit(image.light, pos.light)

    clock.tick(60)
    pygame.display.update()

pygame.quit()