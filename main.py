import random

class Character:
    Name = ""
    item = []
    hp = 4
    issugap = False
    adrenaline = False

class Shotgun:
    saw = False
    shell = []

player = Character()
dealer = Character()
gun = Shotgun()

player.Name="Player"
dealer.Name="Dealer"

def game_start():
    #shell 갯수,
    num_shell = random.randint(2,9)
    num_real = random.randint(1,num_shell-1)
    num_fake = num_shell - num_real
 
    print(num_shell,num_real,num_fake)

    for i in range(num_shell):
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



game_start()
print(gun.shell)

# 확률이 높은 쪽으로 판단
# 50 : 50인 경우 확률을 높이는 판단을 하나
# 그렇지 못 하는 경우 실탄으로 판단
# 아이템을 최대한 사용함
# 
# 담배     : 체력이 1칸 이상 달아있을 떄
# 상한약   : 체력이 2칸 이상 있으며, 체력이 1칸 이상 달아있을 때
#
# 선물상자 : 50:50 상황에서 확률을 높일 수 있는 아이템이 없을 때
#
#아드레날린: 상대 템에 사용하려는 아이템이 있을 경우, 자신 템보다 우선
#
# 대포폰   : 무조건 사용, 판단에 관여 X
# 수갑     : 무조건 사용(수갑을 직전에 사용하지 않은 경우)
# 인형(맥주):공탄
# 변환기   : 공탄 
# 돋보기   : 실탄
# 쇠톱     : 실탄
