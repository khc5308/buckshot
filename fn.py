import pygame,random, time

class Character:
    def __init__(self):
        self.Name = ""
        self.item = [" "]*4
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

font = pygame.font.Font("./fonts/PretendardVariable.ttf", 36)
class img:
    def __init__(self):
        self.background = pygame.image.load("./image/back.png")
        # 총 (45)
        self.gun_45 = pygame.image.load("./image/gun/gun45.png")
        self.saw_gun = pygame.image.load("./image/gun/sawed.png")

        # 총 (90)
        self.gun_90 = pygame.image.load("./image/gun/gun90.png")

        #아이템
        self.tmp_img = pygame.image.load("./image/item/tmp.png")
        self.doll = pygame.image.load("./image/item/doll.png")
        self.gift = pygame.image.load("./image/item/gift.png")
        self.glasses = pygame.image.load("./image/item/glasses.png")
        self.jusagi = pygame.image.load("./image/item/jusagi.png")
        self.pill = pygame.image.load("./image/item/pill.png")
        self.saw = pygame.image.load("./image/item/saw.png")
        self.smoke = pygame.image.load("./image/item/smoke.png")
        #하트
        self.heart = pygame.image.load("./image/heart/heart1.png")
        self.heart_break = pygame.image.load("./image/heart/heart0.png")
        #탄약
        self.real = pygame.image.load("./image/shell/real.png")
        self.fake = pygame.image.load("./image/shell/fake.png")

        #글자
        self.Text_Dealer = font.render("Dealer", True, (255,255,255))
        self.Text_Player = font.render("Player", True, (255,255,255))

        self.light = pygame.image.load("./image/light.png")

        self.dot = pygame.image.load("./image/dot.png")

        

player = Character()
dealer = Character()
gun = Shotgun()
game = GameSetting()
image = img()

player.Name="Player"
dealer.Name="Dealer"

round = -1


def round_start():

    reset_shell()
    game.round += 1

    #hp 뽑기
    num_hp = random.randint(2,4)

    player.max_hp = player.hp = num_hp
    dealer.max_hp = dealer.hp = num_hp

    print("gun.total_num",gun.total_num)
    print("gun.num_real",gun.real_num)
    print("gun.num_fake",gun.fake_num)
    print("gun.shell",gun.shell)

def reset_shell():

    gun.shell = []

    #shell 갯수,실탄,공탄 갯수 랜덤 설정
    num_shell= random.randint(2,8)
    num_real = random.randint(1,num_shell-1)
    num_fake = num_shell - num_real
 
    #class에 넣기
    gun.total_num = num_shell
    gun.real_num = num_real
    gun.fake_num = num_fake

    #갯수에 맞게 랜덤 순서로 넣기
    for _ in range(num_shell):
        n = random.randint(0,1)
        if n and num_real: 
            num_real-=1
            gun.shell.append(n)
        elif not n and num_fake:
            num_fake-=1
            gun.shell.append(n)
        else:
            if num_real:
                gun.shell.append(1)
            else:
                gun.shell.append(0)


def Use_itme(character:Character,slot:int):
    item_name = character.item[slot]
    character.item[slot] = " "
    match item_name:
        case "doll":
            doll(character,slot)
        case "gift":
            gift(character,slot)
        case "glasses":
            glasses(character,slot)
        case "jusagi":
            jusagi(character,slot)
        case "pill":
            pill(character,slot)
        case "saw":
            saw(slot)
        case "smoke":
            smoke(character,slot)   
    
    if item_name != "jusagi" and character.Name == "Dealer":
        print("off adrenaline")
        player.adrenaline = False 


def move_item(character:Character,slot:int):
    pass


#region item 사용 함수
def doll(character:Character,slot:int):
    gun.shell.pop()

def gift(character:Character,slot:int):
    a = int(input("0~6 : "))
    # character.item[slot] = [Items_a_di]

def glasses(character:Character,slot:int):
    print(gun.shell[-1])

def jusagi(character:Character,slot:int):
    if (player.adrenaline or dealer.adrenaline):
        character.item[slot] = "jusagi"
    else:
        character.adrenaline = True

def pill(character:Character,slot:int):
    if random.randint(0,1):
        character.hp += 2
    else:
        character.hp -= 1
    if character.hp > character.max_hp:
        character.hp = character.max_hp

def saw(slot:int):
    gun.saw = True

def smoke(character:Character,slot:int):
    character.hp += 1

def dealer_use_item(character:Character,slot:int):
    pass

#endregion


def shoot(character:Character):

    if gun.shell[-1]:
        character.hp -= 1

    turn = game.isPlayerTurn
    if not((character.Name == "Player" and turn) or (character.Name == "Dealer" and not turn)):
        game.isPlayerTurn = 0 if turn else 1

    gun.saw = False
    
    gun.shell.pop()
    