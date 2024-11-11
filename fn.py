import random

class Character:
    Name = ""
    item = [" "," "," "," "]
    max_hp = 4
    hp = 4
    issugap = False
    adrenaline = False

class Shotgun:
    saw = False
    shell = []
    total_num = 0
    real_num = 0
    fake_num = 0

player = Character()
dealer = Character()
gun = Shotgun()

player.Name="Player"
dealer.Name="Dealer"

Items = ["doll", "gift", "glasses", "jusagi", "pill", "saw", "smoke"]
 
def game_start():

    #shell 갯수,실탄,공탄 갯수 랜덤 설정
    num_shell = random.randint(2,9)
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

    #hp 뽑기
    num_hp = random.randint(2,5)

    player.max_hp = player.hp = num_hp
    dealer.max_hp = dealer.hp = num_hp


def Use_itme(character,slot:int):
    item_name = character.item[slot]

    if item_name == "doll":
        doll()
    elif item_name == "gift":
        gift()
    elif item_name == "glasses":
        glasses()
    elif item_name == "jusagi":
        jusagi()
    elif item_name == "pill":
        pill(character)
    elif item_name == "saw":
        saw()
    elif item_name == "smoke":
        smoke(character)
    else:
        pass


# 애니메이션, 효과 추가할 것
def doll():
    gun.shell.pop()

def gift(character,slot:int):
    a = int(input("0~6 : "))
    character.item[slot] = Items[a]

def glasses():
    print(gun.shell[1])

def jusagi():
    pass

def pill(character):
    if random.randint(0,1):
        character.hp += 2
    else:
        character.hp -= 1
    
    if character.hp > character.max_hp:
        character.hp = character.max_hp

def saw():
    gun.saw = True

def smoke(character):
    character.hp += 1