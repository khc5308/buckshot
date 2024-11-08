import random

class Character:
    Name = ""
    item = [" "," "," "," "]
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
    player.hp=num_hp
    dealer.hp=num_hp

def Use_itme(character,slot:int):
    item_name = character.item[slot]
    if item_name == " ":
        return 0
    elif item_name == "glasses":
        pass
    elif item_name == "glasses":
        pass
    elif item_name == "glasses":
        pass
    elif item_name == "glasses":
        pass
    elif item_name == "glasses":
        pass
    elif item_name == "glasses":
        pass
