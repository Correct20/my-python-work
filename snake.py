import pygame
from sys import exit
while True:
    #init
    pygame.init()
    game_mode = 1#游戏状态：1开始，"p1_die"，"p2_die"结束
    selfkill_mode = 0#掉头自杀：0不可以，1可以
    edge_col = (17, 45, 78)#边界颜色
    p1_col = (63, 114, 175)#p1颜色
    p2_col = (240, 150, 70)#p2颜色
    text_col = (219, 226, 239)#字体颜色
    score = 0
    #window
    screen = pygame.display.set_mode((1600,900))
    pygame.display.set_caption('SNAKE')#窗口标题

    #重玩
    again_n = 0
    #画背景和边界
    screen.fill(edge_col)#边界颜色
    pygame.draw.rect(screen,(37, 42, 52),pygame.Rect(15,15,1570,870))#放置背景矩形
    #clock
    clock = pygame.time.Clock()
    #隐藏鼠标
    pygame.mouse.set_visible(0)
    #text
    font = pygame.font.Font(None,15)
    #P1
    p1_size = 5
    p1_rect = pygame.Rect(100,100,p1_size,p1_size)
    p1_v = 5#瞬时速度
    p1_dir = "RIGHT"#"UP","DOWN","LEFT","RIGHT"方向
    #P2
    p2_size = 5
    p2_rect = pygame.Rect(1500,100,p2_size,p2_size)
    p2_v = 5#瞬时速度
    p2_dir = "LEFT"#"UP","DOWN","LEFT","RIGHT"方向

    #开始时
    while game_mode ==1 :
        score += 1#分数更新

        for event in pygame.event.get():
            #退出
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            #按esc退出
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
            #按下与松开控制p1方向
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:#p1的上按键
                    if selfkill_mode == 0 and p1_dir != "DOWN":
                        p1_dir = "UP"
                    if selfkill_mode == 1:
                        p1_dir = "UP"
                if event.key == pygame.K_s:#p1的下按键
                    if selfkill_mode == 0 and p1_dir != "UP":
                        p1_dir = "DOWN"
                    if selfkill_mode == 1:
                        p1_dir = "DOWN"
                if event.key == pygame.K_a:#p1的左按键
                    if selfkill_mode == 0 and p1_dir != "RIGHT":
                        p1_dir = "LEFT"
                    if selfkill_mode == 1:
                        p1_dir = "LEFT"
                if event.key == pygame.K_d:#p1的右按键
                    if selfkill_mode == 0 and p1_dir != "LEFT":
                        p1_dir = "RIGHT"
                    if selfkill_mode == 1:
                        p1_dir = "RIGHT"
                if event.key == pygame.K_SPACE:#p1的加速键
                    p1_v = 10#加速时的瞬时速度
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:#p1的加速键（和上方的一致）
                    p1_v = 5#瞬时速度(应和初始时的一致)
            #按下与松开控制p2方向
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:#p2的上按键
                    if selfkill_mode == 0 and p2_dir != "DOWN":
                        p2_dir = "UP"
                    if selfkill_mode == 1:
                        p2_dir = "UP"
                if event.key == pygame.K_DOWN:#p2的下按键
                    if selfkill_mode == 0 and p2_dir != "UP":
                        p2_dir = "DOWN"
                    if selfkill_mode == 1:
                        p2_dir = "DOWN"
                if event.key == pygame.K_LEFT:#p2的左按键
                    if selfkill_mode == 0 and p2_dir != "RIGHT":
                        p2_dir = "LEFT"
                    if selfkill_mode == 1:
                        p2_dir = "LEFT"
                if event.key == pygame.K_RIGHT:#p2的右按键";"
                    if selfkill_mode == 0 and p2_dir != "LEFT":
                        p2_dir = "RIGHT"
                    if selfkill_mode == 1:
                        p2_dir = "RIGHT"
                if event.key == pygame.K_RCTRL:#p2的加速键
                    p2_v = 10#加速时的瞬时速度
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RCTRL:#p2的加速键（和上方的一致）
                    p2_v = 5#瞬时速度(应和初始时的一致)
                
        #p1移动和碰撞
        if p1_dir == "UP":
            p1_rect.y -= p1_v#移动
            if screen.get_at((p1_rect.topleft)) in (edge_col,p1_col,p2_col)\
            or screen.get_at((p1_rect.topright)) in (edge_col,p1_col,p2_col):#碰撞
                game_mode = "p1_die"
        if p1_dir == "DOWN":
            p1_rect.y += p1_v#移动
            if screen.get_at((p1_rect.bottomleft)) in (edge_col,p1_col,p2_col)\
            or screen.get_at((p1_rect.bottomright)) in (edge_col,p1_col,p2_col):#碰撞
                game_mode = "p1_die"
        if p1_dir == "LEFT":
            p1_rect.x -= p1_v#移动
            if screen.get_at((p1_rect.topleft)) in (edge_col,p1_col,p2_col)\
            or screen.get_at((p1_rect.bottomleft)) in (edge_col,p1_col,p2_col):#碰撞
                game_mode = "p1_die"
        if p1_dir == "RIGHT":
            p1_rect.x += p1_v#移动
            if screen.get_at((p1_rect.topright)) in (edge_col,p1_col,p2_col)\
            or screen.get_at((p1_rect.bottomright)) in (edge_col,p1_col,p2_col):#碰撞
                game_mode = "p1_die"
        #p2移动和碰撞
        if p2_dir == "UP":
            p2_rect.y -= p2_v#移动
            if screen.get_at((p2_rect.topleft)) in (edge_col,p1_col,p2_col)\
            or screen.get_at((p2_rect.topright)) in (edge_col,p1_col,p2_col):#碰撞
                game_mode = "p2_die"
        if p2_dir == "DOWN":
            p2_rect.y += p2_v#移动
            if screen.get_at((p2_rect.bottomleft)) in (edge_col,p1_col,p2_col)\
            or screen.get_at((p2_rect.bottomright)) in (edge_col,p1_col,p2_col):#碰撞
                game_mode = "p2_die"
        if p2_dir == "LEFT":
            p2_rect.x -= p2_v#移动
            if screen.get_at((p2_rect.topleft)) in (edge_col,p1_col,p2_col)\
            or screen.get_at((p2_rect.bottomleft)) in (edge_col,p1_col,p2_col):#碰撞
                game_mode = "p2_die"
        if p2_dir == "RIGHT":
            p2_rect.x += p2_v#移动
            if screen.get_at((p2_rect.topright)) in (edge_col,p1_col,p2_col)\
            or screen.get_at((p2_rect.bottomright)) in (edge_col,p1_col,p2_col):#碰撞
                game_mode = "p2_die"

        #画矩形到屏幕
        pygame.draw.rect(screen,p1_col,p1_rect)#p1
        pygame.draw.rect(screen,p2_col,p2_rect)#p2
        
        pygame.display.update()#更新
        clock.tick(60)#clock

    #撞到结束
    die_t = 0
    text_sur = font.render(f"{score/60:.2f}",True,text_col)#分数/60
    screen.blit(text_sur,(0,0))#显示分数
    tip_sur = font.render(f"Press 'R' to play again",True,text_col)#提示
    screen.blit(tip_sur,(700,0))#显示提示
    while True:
        for event in pygame.event.get():
            #退出
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            #按esc退出
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
            #按R重玩
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    again_n = 1
        
        #重玩
        if again_n == 1:
            break

        #p1 die
        if game_mode == "p1_die" and die_t < 6:
            #p1变大
            p1_rect.inflate_ip(5,5)
            die_t += 1
        #p2 die
        if game_mode == "p2_die" and die_t < 6:
            #p2变大
            p2_rect.inflate_ip(5,5)
            die_t += 1

        #画矩形到屏幕
        pygame.draw.rect(screen,p1_col,p1_rect)#p1
        pygame.draw.rect(screen,p2_col,p2_rect)#p2

        pygame.display.update()#更新
        clock.tick(60)#clock