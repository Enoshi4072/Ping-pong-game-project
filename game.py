import pygame
from entities import Paddle, Ball
from players import AIPlayer, TwoPlayerMode
from drawing import draw_menu, draw_instructions, draw, handle_collision



def main():
    """
    Main function controlling the game loop and setup
    """
    run = True
    clock = pygame.time.Clock()
    left_paddle = Paddle(10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS, max_vel=5)  # Default max_vel
    left_score = 0
    right_score = 0
    mode_prompt = "Choose mode: Enter '1' for single player with AI, '2' for two players: "
    mode = None

    draw_menu(WIN)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    mode = '1'
                    break
                elif event.key == pygame.K_2:
                    mode = '2'
                    break
                elif event.key == pygame.K_i:  # Key for instructions
                    draw_instructions(WIN)
        else:
            continue
        break

    if mode == '1':
        difficulty_prompt = "Choose AI difficulty: Enter 'E' for easy, 'M' for medium, 'H' for hard: "
        while True:
            draw(WIN, [left_paddle, right_paddle], ball, left_score, right_score, difficulty_prompt)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS, max_vel=5)  # Easy mode
                        break
                    elif event.key == pygame.K_m:
                        ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS, max_vel=6.5)  # Medium mode
                        break
                    elif event.key == pygame.K_h:
                        ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS, max_vel=8.5)  # Hard mode
                        break
            else:
                continue
            break
        ai_player = AIPlayer(right_paddle, ball)
    else:
        ai_player = None

    player_mode = TwoPlayerMode(left_paddle, right_paddle)
    countdown_timer = None
    paused = False
    pause_text = SCORE_FONT.render("Paused", 1, WHITE)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused  # Toggle pause state
                elif event.key == pygame.K_ESCAPE:
                    draw_menu(WIN)
                    mode = None
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run = False
                                break
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_1:
                                    mode = '1'
                                    break
                                elif event.key == pygame.K_2:
                                    mode = '2'
                                    break
                                elif event.key == pygame.K_i:  # Key for instructions
                                    draw_instructions(WIN)
                        else:
                            continue
                        break
                    if mode == '1':
                        difficulty_prompt = "Choose AI difficulty: Enter 'E' for easy, 'M' for medium, 'H' for hard: "
                        while True:
                            draw(WIN, [left_paddle, right_paddle], ball, left_score, right_score, difficulty_prompt)
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    run = False
                                    break
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_e:
                                        ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS, max_vel=5)  # Easy mode
                                        break
                                    elif event.key == pygame.K_m:
                                        ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS, max_vel=6.5)  # Medium mode
                                        break
                                    elif event.key == pygame.K_h:
                                        ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS, max_vel=8.5)  # Hard mode
                                        break
                            else:
                                continue
                            break
                        ai_player = AIPlayer(right_paddle, ball)
                    else:
                        ai_player = None

                    player_mode = TwoPlayerMode(left_paddle, right_paddle)
                    left_score = 0
                    right_score = 0
                    countdown_timer = None
                    paused = False
                    draw_menu(WIN)
                    break

        if paused:
            WIN.blit(pause_text, (WIDTH // 2 - pause_text.get_width() // 2, HEIGHT // 2 - pause_text.get_height() // 2))
            pygame.display.update()
            continue

        draw(WIN, [left_paddle, right_paddle], ball, left_score, right_score)
        if countdown_timer is not None:
            if time.time() < countdown_timer + GOAL_DELAY:
                timer = int(GOAL_DELAY - (time.time() - countdown_timer))
                draw(WIN, [left_paddle, right_paddle], ball, left_score, right_score, timer=timer)
                continue
            else:
                countdown_timer = None

        keys = pygame.key.get_pressed()
        player_mode.move(keys)
        if ai_player:
            ai_player.move()
        ball.move()
        handle_collision(ball, left_paddle, right_paddle)

        if ball.x < 0:
            right_score += 1
            if right_score >= WINNING_SCORE:
                draw(WIN, [left_paddle, right_paddle], ball, left_score, right_score, winner="Player 2")
                mode = None
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                            break
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_1:
                                mode = '1'
                                break
                            elif event.key == pygame.K_2:
                                mode = '2'
                                break
                            elif event.key == pygame.K_i:  # Key for instructions
                                draw_instructions(WIN)
                    else:
                        continue
                    break
                if mode == '1':
                    difficulty_prompt = "Choose AI difficulty: Enter 'E' for easy, 'M' for medium, 'H' for hard: "
                    while True:
                        draw(WIN, [left_paddle, right_paddle], ball, left_score, right_score, difficulty_prompt)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run = False
                                break
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_e:
                                    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS, max_vel=5)  # Easy mode
                                    break
                                elif event.key == pygame.K_m:
                                    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS, max_vel=6.5)  # Medium mode
                                    break
                                elif event.key == pygame.K_h:
                                    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS, max_vel=8.5)  # Hard mode
                                    break
                        else:
                            continue
                        break
                    ai_player = AIPlayer(right_paddle, ball)
                else:
                    ai_player = None

                player_mode = TwoPlayerMode(left_paddle, right_paddle)
                left_score = 0
                right_score = 0
                countdown_timer = None
                paused = False
                draw_menu(WIN)
            else:
                ball.reset()
                left_paddle.reset()
                right_paddle.reset()
                countdown_timer = time.time()  # Start countdown timer
        elif ball.x > WIDTH:
            left_score += 1
            if left_score >= WINNING_SCORE:
                draw(WIN, [left_paddle, right_paddle], ball, left_score, right_score, winner="Player 1")
                mode = None
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                            break
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_1:
                                mode = '1'
                                break
                            elif event.key == pygame.K_2:
                                mode = '2'
                                break
                            elif event.key == pygame.K_i:  # Key for instructions
                                draw_instructions(WIN)
                    else:
                        continue
                    break
                if mode == '1':
                    difficulty_prompt = "Choose AI difficulty: Enter 'E' for easy, 'M' for medium, 'H' for hard: "
                    while True:
                        draw(WIN, [left_paddle, right_paddle], ball, left_score, right_score, difficulty_prompt)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run = False
                                break
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_e:
                                    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS, max_vel=5)  # Easy mode
                                    break
                                elif event.key == pygame.K_m:
                                    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS, max_vel=6.5)  # Medium mode
                                    break
                                elif event.key == pygame.K_h:
                                    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS, max_vel=8.5)  # Hard mode
                                    break
                        else:
                            continue
                        break
                    ai_player = AIPlayer(right_paddle, ball)
                else:
                    ai_player = None

                player_mode = TwoPlayerMode(left_paddle, right_paddle)
                left_score = 0
                right_score = 0
                countdown_timer = None
                paused = False
                draw_menu(WIN)
            else:
                ball.reset(towards_left=False)
                left_paddle.reset()
                right_paddle.reset()
                countdown_timer = time.time()  # Start countdown timer

    pygame.quit()
