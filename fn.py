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
        self.issugap = False
        self.adrenaline = False

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
        # 총 (45)
        self.gun_45      = pygame.image.load("./image/gun/gun45.png")
        self.gun_45_saw  = pygame.image.load("./image/gun/gun45_saw.png")
        # 총 (90)
        self.gun_90      = pygame.image.load("./image/gun/gun90.png")
        self.gun_90_saw  = pygame.image.load("./image/gun/gun90_saw.png")
        #아이템
        self.doll        = pygame.image.load("./image/item/doll.png")
        self.gift        = pygame.image.load("./image/item/gift.png")
        self.glasses     = pygame.image.load("./image/item/glasses.png")
        self.jusagi      = pygame.image.load("./image/item/jusagi.png")
        self.phone       = pygame.image.load("./image/item/phone.png")
        self.pill        = pygame.image.load("./image/item/pill.png")
        self.saw         = pygame.image.load("./image/item/saw.png")
        self.smoke       = pygame.image.load("./image/item/smoke.png")
        self.tmp_img     = pygame.image.load("./image/item/tmp.png")
        #하트   
        self.heart_break = pygame.image.load("./image/heart/heart0.png")
        self.heart       = pygame.image.load("./image/heart/heart1.png")
        #탄약   
        self.real        = pygame.image.load("./image/shell/real.png")
        self.fake        = pygame.image.load("./image/shell/fake.png")
        #기타   
        self.light       = pygame.image.load("./image/light.png")
        self.dot         = pygame.image.load("./image/dot.png")
        #글자
        self.Text_Dealer = font.render("Dealer", True, (255,255,255))
        self.Text_Player = font.render("Player", True, (255,255,255))
#endregion

player = Character()
dealer = Character()
gun = Shotgun()
game = GameSetting()
image = img()

player.Name = "Player"
dealer.Name = "Dealer"

screen_width, screen_height = 1920, 1080 
screen = pygame.display.set_mode((screen_width, screen_height))

item_name=["gift","glasses","phone","sugap","smoke","saw","doll","pill"]
round = -1

def round_start():

    game.round += 1

    reset_shell()
    reset_hp()

    print("gun.total_num", gun.total_num)
    print("gun.num_real", gun.real_num)
    print("gun.num_fake", gun.fake_num)
    print("gun.shell", gun.shell)

def reset_hp():
    # hp 뽑기
    num_hp = random.randint(2, 4)

    player.max_hp = player.hp = num_hp
    dealer.max_hp = dealer.hp = num_hp

def reset_shell():
    gun.shell = []

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

def Use_itme(character:Character, slot: int):
    item_name = character.item[slot]
    character.item[slot] = " "

    print(f"{item_name} 사용 시도")
    #상대 판단
    opponent = dealer if character.Name=='Player' else player

    match item_name:
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

def doll():
    dealer.expected_shell.pop()
    gun.shell.pop()

def gift(character:Character,slot:int):
    if character.Name=='Player':
        character.item[slot] = item_name[2]
    else:
        character.item[slot] = "glasses" #돋보기 선택

def glasses(character:Character):
    if character.Name=="Player":
        print(gun.shell[-1])
    else:
        character.expected_shell[-1]=gun.shell[-1]#맨 앞 탄환의 실탄여부를 저장

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
    n = random.randint(2, len(gun.shell)-1)#2부터 총탄 길이까지의 정수인 난수 b
    if character.Name=='player':
        if len(gun.shell) == 1:
            print(f'1번째 탄 - {gun.shell[-1]}')
        else:
            print(f'{n}번째 탄 - {gun.shell[-n]}') #플레이어면 b 위치의 총탄 알려주기
    else:
        dealer.expected_shell[-n] = gun.shell[-n]#딜러면 b 위치의 총탄을 리스트에 저장

def sugap(opponent:Character):
    opponent.issugap=True#상대 수갑으로 묶기

#endregion

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

def shoot(character: Character):
    turn = game.isPlayerTurn

    #실탄일 시 
    if gun.shell[-1]:
        character.hp -= 1 + int(gun.saw)

    #자신을 쏠 때
    if character.Name == ("Player" if turn else "Dealer"):
        if gun.shell[-1]:
            game.isPlayerTurn = int(not turn)
    else:
        game.isPlayerTurn = int(not turn)

    gun.saw = False
    gun.shell.pop()
    dealer.expected_shell.pop()
