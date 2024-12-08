import random,pygame,time
font = pygame.font.Font("./fonts/PretendardVariable.ttf", 36)

#region class
class Character:
    def __init__(self):
        self.Name = ""
        self.item = [" "] * 4
        self.expected_shell=[-1]#예상 탄환 리스트
        self.max_hp = 4
        self.hp = 4
        self.sugap_num = 0
        self.issugap = False
        self.adrenaline = False
        self.pos_hold_item = () 

class Shotgun:
    def __init__(self):
        self.saw = False
        self.shell = []
        self.total_num = 0
        self.real_num = 0
        self.fake_num = 0

class GameSetting:
    def __init__(self):
        self.round = -1
        self.isPlayerTurn = True

class img:
    def __init__(self):
        self.background  = pygame.image.load("./image/back.png")

        self.deler_1     = pygame.image.load("./image/dealer/enemy-1.png")
        self.deler_2     = pygame.image.load("./image/dealer/enemy-2.png")
        #총_saw
        self.gun_45_saw    = pygame.image.load("./image/gun/saw/gun_45.png")
        self.gun_90_saw    = pygame.image.load("./image/gun/saw/gun_90.png")
        self.gun_fire1_saw = pygame.image.load("./image/gun/saw/gun_fire1.png")
        self.gun_fire2_saw = pygame.image.load("./image/gun/saw/gun_fire2.png")
        self.gun_fire3_saw = pygame.image.load("./image/gun/saw/gun_fire3.png")
        self.gun_fire4_saw = pygame.image.load("./image/gun/saw/gun_fire4.png")
        #총 
        self.gun_45       =  pygame.image.load("./image/gun/nomal/gun_45.png")
        self.gun_90       =  pygame.image.load("./image/gun/nomal/gun_90.png")
        self.gun_fire1    =  pygame.image.load("./image/gun/nomal/gun_fire1.png")
        self.gun_fire2    =  pygame.image.load("./image/gun/nomal/gun_fire2.png")
        self.gun_fire3    =  pygame.image.load("./image/gun/nomal/gun_fire3.png")
        self.gun_fire4    =  pygame.image.load("./image/gun/nomal/gun_fire4.png")


        #아이템
        self.cylinder    = pygame.image.load("./image/item/cylinder.png")
        self.doll        = pygame.image.load("./image/item/doll.png")
        self.gift        = pygame.image.load("./image/item/gift.png")
        self.glasses     = pygame.image.load("./image/item/glasses.png")
        self.jusagi      = pygame.image.load("./image/item/jusagi.png")
        self.phone       = pygame.image.load("./image/item/phone.png")
        self.pill        = pygame.image.load("./image/item/pill.png")
        self.saw         = pygame.image.load("./image/item/saw.png")
        self.smoke       = pygame.image.load("./image/item/smoke.png")
        self.sugap       = pygame.image.load("./image/item/sugap.png")
        self.tmp_img     = pygame.image.load("./image/item/tmp.png")
        self.white       = pygame.image.load("./image/item/white.png")
        #하트   
        self.heart_break = pygame.image.load("./image/heart/heart0.png")
        self.heart       = pygame.image.load("./image/heart/heart1.png")
        #탄약   
        self.real        = pygame.image.load("./image/shell/real.png")
        self.fake        = pygame.image.load("./image/shell/fake.png")        
        #기타   
        self.light       = pygame.image.load("./image/light.png")
        self.dot         = pygame.image.load("./image/dot.png")
        self.item_box    = pygame.image.load("./image/item_box.png")
        self.gift_box    = pygame.image.load("./image/gift_box.png")
        #글자
        self.Text_Dealer = font.render("Dealer", True, (255,255,255))
        self.Text_Player = font.render("Player", True, (255,255,255))

        self.gun_45_saw = pygame.transform.scale(self.gun_45_saw, (self.gun_45.get_width() ,self.gun_45.get_height()))
        self.deler_2    = pygame.transform.scale(self.deler_2   , (self.deler_1.get_width() ,self.deler_1.get_height()))

class Position:
    def __init__(self):
        self.item             = [(720 ,778),(840 ,778),(960 ,778),(1080,778),
                                 (720 ,180),(840 ,180),(960 ,180),(1080,180)]
        self.shell            = [(1113,418),(1113,449),(1113,480),(1113,511),(1113,541),(1113,572),(1113,603),(1113,634)]
        self.round_dot        = [(1219,543),(1239,543),(1262,543)]
        self.heart_player     = [(1209,597),(1225,597),(1241,597),(1257,597)]
        self.heart_dealer     = [(1209,460),(1225,460),(1241,460),(1257,460)]
        self.dealer           = (780, 0)
        self.light            = (260, 0)
        self.gun              = (625, 180)

        Tmp_width =  image.tmp_img.get_width()
        Tmp_height =  image.tmp_img.get_height()
        self.click_zone = [pygame.Rect(720, 778, Tmp_width, Tmp_height),
              pygame.Rect(840, 778, Tmp_width, Tmp_height),
              pygame.Rect(960, 778, Tmp_width, Tmp_height),
              pygame.Rect(1080,778, Tmp_width, Tmp_height),
              pygame.Rect(720, 180, Tmp_width, Tmp_height),
              pygame.Rect(840, 180, Tmp_width, Tmp_height),
              pygame.Rect(960, 180, Tmp_width, Tmp_height),
              pygame.Rect(1080,180, Tmp_width, Tmp_height)
              ]
        self.click_zone_item_box = pygame.Rect(821, 390, image.item_box.get_width(), image.item_box.get_height())

        self.click_zone_gun = pygame.Rect(625, 180,image.gun_45.get_width(), image.gun_45.get_height())
        self.click_zone_playerText = pygame.Rect(907,330, image.Text_Dealer.get_width(), image.Text_Dealer.get_height())
        self.click_zone_dealerText = pygame.Rect(907,680, image.Text_Player.get_width(), image.Text_Player.get_height())

player = Character()
dealer = Character()
gun = Shotgun()
game = GameSetting()
image = img()
pos = Position()

player.Name = "Player"
dealer.Name = "Dealer"

player.pos_hold_item = (900, 967)
dealer.pos_hold_item = (900, 195)
#endregion

Items_di= {
    "cylinder" : image.cylinder,
    "doll"     : image.doll,
    "gift"     : image.gift,   
    "glasses"  : image.glasses,
    "jusagi"   : image.jusagi, 
    "phone"    : image.phone,  
    "pill"     : image.pill,   
    "saw"      : image.saw,    
    "smoke"    : image.smoke,
    "sugap"    : image.sugap,
    " "        : image.tmp_img
}
items_name = list(Items_di.keys())

screen = pygame.display.set_mode((1920, 1080))
item_name=["gift","glasses","phone","sugap","smoke","saw","doll","pill","cylinder"]
round = -1

Tmp_width  = image.tmp_img.get_width()
Tmp_height = image.tmp_img.get_height()


def round_start():

    game.round += 1

    reset_hp()
    reset_shell()

    print("gun.shell", gun.shell)

def reset_hp():
    # hp 뽑기
    num_hp = random.randint(2, 4)

    player.max_hp = player.hp = num_hp
    dealer.max_hp = dealer.hp = num_hp

def reset_shell():
    game.isPlayerTurn = True
    gun.shell = []
    player.issugap = False
    dealer.issugap = False

    dealer.sugap_num = 0
    player.sugap_num = 0

    # shell 갯수,실탄,공탄 갯수 랜덤 설정
    num_shell = random.randint(2, 8)
    num_real = random.randint(1, num_shell - 1)
    num_fake = num_shell - num_real

    # class에 넣기
    gun.total_num = num_shell
    gun.real_num = num_real
    gun.fake_num = num_fake
    dealer.expected_shell= [-1] * num_shell #예상되는 탄환 길이 설정

    # 갯수에 맞게 랜덤 순서로 넣기
    for _ in range(num_shell):
        n = random.randint(0, 1)
        if n and num_real:
            num_real -= 1
            gun.shell.append(n)
        elif not n and num_fake:
            num_fake -= 1
            gun.shell.append(n)
        else:
            gun.shell.append(int(bool(num_real)))
    
    show_shell()

def reset_item():
    player.item = [" "," "," "," "]
    dealer.item = [" "," "," "," "]

def game_end(text):
    screen.fill((0, 0, 0))
    t = font.render(text, True, (255,255,255))
    screen.blit(t, t.get_rect(center=(960, 540)))
    pygame.display.update()
    time.sleep(2)
    game.round = -1
    reset_item()
    round_start()

def show_shell():
    screen.blit(image.background,(0,0))
    shell = sorted(gun.shell)
    for i in range(1,gun.total_num+1):
        screen.blit(image.real if shell[-i] else image.fake, pos.shell[i-1])
    draw_item()
    draw_dealer()
    screen.blit(image.light,pos.light)
    pygame.display.update()
    time.sleep(2)

def give_item():
    screen.blit(image.item_box,(821, 390))
    a = random.randint(1, 4)
    b = a
    isClick_itemBox = False
    while a:
        for e in pygame.event.get():
            if e.type != pygame.MOUSEBUTTONDOWN:
                continue

            if pos.click_zone_item_box.collidepoint(e.pos) and not isClick_itemBox: 
                isClick_itemBox = True
                item = item_name[random.randint(0, len(item_name) - 1)]
                screen.blit(Items_di[item],(821, 390))
            if isClick_itemBox:
                for i in range(4):
                    if pos.click_zone[i].collidepoint(e.pos):
                        if player.item[i] == ' ':
                            player.item[i] = item
                        elif player.item.count(' '):
                            break

                        isClick_itemBox = False
                        a -= 1
                        break
                        
        screen.blit(image.background, (0, 0))
        draw_item()
        screen.blit(image.item_box,(821, 390))
        if isClick_itemBox:
            screen.blit(Items_di[item],(900, 490)) 
        draw_dealer()
        screen.blit(image.light, pos.light)
        pygame.display.update()

    for i in range(min(b)):
        if dealer.item[i] != " ":
            dealer.item[i] = item_name[random.randint(0,len(item_name)-1)]

    draw_item()
                
def Use_itme(character:Character, slot: int):
    opponent = dealer if character.Name=='Player' else player
    item_name = character.item[slot]
    character.item[slot] = " "

    if item_name == " ":
        return
    print(f"{item_name} 사용 시도")

    #상대 판단

    x1,y1 = pos.item[slot+(0 if character.Name=='Player' else 4)]

    if item_name == "sugap":
        x2,y2 = opponent.pos_hold_item
    else:
        x2,y2 = character.pos_hold_item

    linear_function = lambda x: ((y2 - y1) / (x2 - x1)) * (x - x1) + y1

    move_item = Items_di[item_name] if  character.Name=='Player' else pygame.transform.rotate(Items_di[item_name], 180)
    draw_heart()
    draw_dealer()

    accle = 10
    for i in range(x1,x2+1,10):
        moving_item(i+accle,linear_function,slot,move_item)
        accle += 10
    for i in range(x1,x2+1,-10):
        moving_item(i-accle,linear_function,slot,move_item)
        accle += 10

    match item_name:
        case "cylinder":
            cylinder()
        case "doll":
            doll()
        case "gift":
            gift(character, slot)
        case "glasses":
            glasses(character)
        case "jusagi":
            jusagi(character, slot)
        case "pill":
            pill(character)
        case "saw":
            saw()
        case "smoke":
            smoke(character)
        case "phone":
            phone(character)
        case "sugap":
            sugap(opponent)

    if item_name != "jusagi" and character.Name == "Dealer":
        print("off adrenaline")
        player.adrenaline = False

#region item function

def moving_item(i:int,linear_function,slot:int,move_item):
    screen.blit(image.background, (0, 0))
    draw_item()
    draw_dealer()
    draw_heart()
    screen.blit(image.dot, pos.round_dot[game.round])
    screen.blit(image.gun_45_saw if gun.saw else image.gun_45, pos.gun)
    screen.blit(image.tmp_img,pos.item[slot])

    screen.blit(move_item,(i,linear_function(i)))
    screen.blit(image.light, pos.light)
    pygame.display.update()

def cylinder():
    toggled_array = [int(not x) for x in gun.shell]
    toggled_expected =[]
    for i in dealer.expected_shell:
        if i == 0 or i == 1:
            toggled_expected.append(not(i))
        else:
            toggled_expected.append(i)
    gun.fake_num,gun.real_num = gun.real_num,gun.fake_num

    dealer.expected_shell = toggled_expected
    gun.shell = toggled_array

def doll():
    if gun.shell[-1]:
        sound = pygame.mixer.Sound('sound/dryfire.WAV')
        sound.set_volume(0.5)
    else:
        sound = pygame.mixer.Sound('sound/SHot.WAV')

    sound.play()
    time.sleep(sound.get_length())

    dealer.expected_shell.pop()
    gun.shell.pop()

def gift(character:Character,slot:int):
    character.item[slot] = item_name[random.randint(0, len(item_name) - 1)]

def glasses(character:Character):
    if character.Name=="Player":
        screen.blit(image.background,(0,0))
        draw_item()
        draw_dealer()
        draw_heart()
        screen.blit(image.real if gun.shell[-1] else image.fake, pos.shell[0])
        screen.blit(image.gun_45_saw if gun.saw else image.gun_45,pos.gun)
        screen.blit(image.dot, pos.round_dot[game.round])
        screen.blit(image.light,pos.light)
        pygame.display.update()
        time.sleep(1)
    else:
        character.expected_shell[-1]=gun.shell[-1] #맨 앞 탄환의 실탄여부를 저장

def jusagi(character:Character,slot:int):
    if character.Name=="Player":
       player.adrenaline = True
    else:
        for i in item_name:
            if i in player.item:
                dealer.item[slot] = player.item[player.item.index(i)]
                player.item[player.item.index(i)]=" "
                break
        Use_itme(character,slot)#가져온 아이템 바로 사용

def pill(character:Character):
    if random.randint(0,1):
        character.hp += 2
    else:
        character.hp -= 1

    if character.hp > character.max_hp:
        character.hp = character.max_hp

def saw():
    gun.saw = True

def smoke(character:Character):
    character.hp += 1
    if character.hp > character.max_hp:
        character.hp = character.max_hp

def phone(character:Character):
    n = 1 if len(gun.shell) == 1 else random.randint(2, len(gun.shell))
    print(character.Name)
    if character.Name=='Player':
        screen.blit(font.render(f'1번째 탄 - {gun.shell[-1]}', True, (255,255,255)), (907,330))
        time.sleep(1)
    else:
        dealer.expected_shell[-n] = gun.shell[-n]#딜러면 b 위치의 총탄을 리스트에 저장

def sugap(opponent:Character):
    opponent.issugap=True#상대 수갑으로 묶기
    opponent.sugap_num = 2

#endregion

#region draw
def draw_item():
    #player
    screen.blit(Items_di[player.item[0]], pos.item[0])
    screen.blit(Items_di[player.item[1]], pos.item[1])
    screen.blit(Items_di[player.item[2]], pos.item[2])
    screen.blit(Items_di[player.item[3]], pos.item[3])
    #dealer
    screen.blit(Items_di[dealer.item[0]], pos.item[4])
    screen.blit(Items_di[dealer.item[1]], pos.item[5])
    screen.blit(Items_di[dealer.item[2]], pos.item[6])
    screen.blit(Items_di[dealer.item[3]], pos.item[7])

def draw_heart():
    for i in range(player.max_hp):
        screen.blit(image.heart if i < player.hp else image.heart_break, pos.heart_player[i])

    for i in range(dealer.max_hp):
        screen.blit(image.heart if i < dealer.hp else image.heart_break, pos.heart_dealer[i])

def draw_dealer():
    screen.blit([image.deler_1,image.deler_1,image.deler_2,image.deler_1][game.round],pos.dealer)

#endregion

#region ai
def itemDetermine(possibility):
    for i in range(len(dealer.item)):
        match dealer.item[i]:
            case 'smoke':# 담배     : 체력이 1칸 이상 달아있을 떄
                if dealer.max_hp-dealer.hp>=1:
                    Use_itme(dealer,i)
            case 'pill':# 상한약   : 체력이 2칸 이상 있으며, 체력이 1칸 이상 달아있을 때
                if dealer.max_hp-dealer.hp>=1 and dealer.hp>=2:
                    Use_itme(dealer,i)
            case 'gift':# 선물상자 : 50:50 상황에서 확률을 높일 수 있는 아이템이(=대포폰,돋보기?) 없을 때
                if possibility==0.5 and ('phone' not in dealer.item or 'glasses' not in dealer.item):
                    Use_itme(dealer, i)
            case 'jusagi':#아드레날린: 상대 템에 사용하려는 아이템이 있을 경우, 자신 템보다 우선(어려워서 그냥 아이템 가지고 있으면 무조건 뺏어오는걸로)
                if len(player.item)>0 and not dealer.adrenaline:
                    Use_itme(dealer, i)
            case 'saw':# 쇠톱     : 실탄 100%면 사용
                if possibility==1:
                    Use_itme(dealer, i)
            case 'sugap':# 수갑     : 무조건 사용(수갑을 직전에 사용하지 않은 경우)
                if player.issugap==False:
                    Use_itme(dealer, i)
            case " ":# 자리에 아이템이 없으면 그냥 넘어가기
                continue
            case _:#나머지는 무조건 사용
                Use_itme(dealer, i)

def determine():
    if dealer.expected_shell[-1] != -1:#리스트에 현재 탄의 실탄 여부가 저장돼있을 시 그 값을 사용
        possibility = dealer.expected_shell[-1]
    else:
        possibility = gun.shell.count(1) / len(gun.shell)#아니면 그냥 기본 확률로

    itemDetermine(possibility)#아이템 사용

    if dealer.expected_shell[-1] != -1:
        possibility = dealer.expected_shell[-1]
    else:
        possibility = gun.shell.count(1) / len(gun.shell)#아이템 사용으로 인해 확률이 변동될 수 있으니 다시 확률 계산

    if 1 - possibility > possibility:#실탄 공탄 중 확률이 높은 쪽에 가중치를 둠, 같으면 그냥 무작위로, 액션==1-자신 쏘기 액션==2-상대 쏘기
        action = random.choices(range(1, 3), weights=[1 - possibility * 0.7, possibility * 0.7])[0]
    elif possibility > 1 - possibility:
        action = random.choices(range(1, 3), weights=[(1 - possibility) * 0.7, 1 - (1 - possibility) * 0.7])[0]
    else:
        action = random.randint(1, 2)
    return action - 1

#endregion

def shoot(character: Character):
    turn = game.isPlayerTurn
    opponent = dealer if character.Name=='Player' else player    
    isnt_self_shot = not (character.Name == ("Player" if turn else "Dealer"))

    #사운드, 체력
    if gun.shell[-1]:
        character.hp -= 1 + int(gun.saw)
        sound = pygame.mixer.Sound('sound/SHot.WAV')
        sound.set_volume(0.5)
    else:
        sound = pygame.mixer.Sound('sound/dryfire.WAV')

    #이미지
    a = [image.gun_fire1, image.gun_fire2, image.gun_fire3, image.gun_fire4]
    b = [pygame.transform.rotate(image.gun_fire1, 180),
         pygame.transform.rotate(image.gun_fire2, 180),
         pygame.transform.rotate(image.gun_fire3, 180),
         pygame.transform.rotate(image.gun_fire4, 180)]
    c = [image.gun_fire1_saw, image.gun_fire2_saw, image.gun_fire3, image.gun_fire4_saw]
    d = [pygame.transform.rotate(image.gun_fire1_saw, 180),
         pygame.transform.rotate(image.gun_fire2_saw, 180),
         pygame.transform.rotate(image.gun_fire3_saw, 180),
         pygame.transform.rotate(image.gun_fire4_saw, 180)]

    #그리기
    fire_img_arr = [a,b,c,d][(2 if gun.saw else 1) * (2 if character.Name != 'Dealer' else 1) - 1] 
    sound.play()

    if gun.shell[-1]:
        for i in fire_img_arr:
            screen.blit(image.background,(0,0))
            draw_item()
            draw_dealer()
            draw_heart()

            if game.isPlayerTurn:
                screen.blit(i, (906, 770))
            else:
                if isnt_self_shot:
                    screen.blit(pygame.transform.rotate(i, 180), (856,-500))
                else:
                    screen.blit(pygame.transform.rotate(i, 180), (856,-200))

            screen.blit(image.light,pos.light)

            pygame.display.update()
            pygame.time.delay(100)
    else:
        screen.blit(image.background,(0,0))
        draw_item()
        draw_dealer()
        draw_heart()

        i = image.gun_90_saw if gun.saw else image.gun_90
        if game.isPlayerTurn:
            screen.blit(i if isnt_self_shot else pygame.transform.rotate(i, 180),(906, 770))
        else:
            if isnt_self_shot:
                screen.blit(pygame.transform.rotate(i, 180) ,(856,-200))
            else:
                screen.blit(i ,(856,-450))
                

        screen.blit(image.light,pos.light)
        pygame.display.update()

    time.sleep(sound.get_length() + 0.5)

    # 턴 넘기기
    if character.issugap:
        if isnt_self_shot:
            character.sugap_num -= 1
        else:
            if gun.shell[-1]:
                character.sugap_num -= 1
    else:
        if isnt_self_shot:
            game.isPlayerTurn = int(not turn)
        else:
            if gun.shell[-1]:
                game.isPlayerTurn = int(not turn)

    character.issugap = character.sugap_num > 0
    gun.saw = False
    gun.shell.pop()
    dealer.expected_shell.pop()

    
