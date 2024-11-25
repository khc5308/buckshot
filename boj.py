import pygame

# 초기화
pygame.init()

# 화면 설정
screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))

# 이미지 로드 및 위치 설정
image = pygame.image.load("./image/gun/gun45.png")
image_pos = [200, 200]  # 이미지를 그릴 위치

# 회전 각도 초기화
angle = 0  # 회전 각도 (도 단위)

# 메인 루프 설정
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 각도 증가 (360도를 넘으면 0도로 초기화)
    angle = (angle + 1) % 360

    # 이미지를 회전
    rotated_image = pygame.transform.rotate(image, angle)

    # 회전된 이미지의 중심을 맞추기 위한 새로운 위치 계산
    rotated_rect = rotated_image.get_rect(center=image.get_rect(topleft=image_pos).center)

    # 화면 지우기
    screen.fill((255, 255, 255))  # 배경 흰색

    # 회전된 이미지 그리기
    screen.blit(rotated_image, rotated_rect.topleft)

    # 화면 업데이트
    pygame.display.flip()

    # 초당 60프레임 설정
    clock.tick(60)

pygame.quit()
