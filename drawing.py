import pygame
from entities import Paddle, Ball

# Functions for drawing menu, instructions, and handling collisions
def draw_menu(win):
    """
    Draw the main menu screen.

    Args:
        win (pygame.Surface): The surface to draw on.

    This function fills the window with a black background and displays the main menu text,
    including instructions for starting the game.

    """
    win.fill(BLACK)
    menu_text = SCORE_FONT.render("Welcome to Pong!", 1, WHITE)
    instructions_text = SCORE_FONT.render("Press 1 for single player with AI", 1, WHITE)
    instructions_text2 = SCORE_FONT.render("Press 2 for two players mode", 1, WHITE)
    instructions_text3 = SCORE_FONT.render("Press I for game instructions", 1, WHITE)
    win.blit(menu_text, (WIDTH // 2 - menu_text.get_width() // 2, HEIGHT // 4))
    win.blit(instructions_text, (WIDTH // 2 - instructions_text.get_width() // 2, HEIGHT // 2 - FONT_SIZE))
    win.blit(instructions_text2, (WIDTH // 2 - instructions_text2.get_width() // 2, HEIGHT // 2))
    win.blit(instructions_text3, (WIDTH // 2 - instructions_text3.get_width() // 2, HEIGHT // 2 + FONT_SIZE))
    pygame.display.update()

def draw_instructions(win):
    """
    Draw the instructions screen.

    Args:
        win (pygame.Surface): The surface to draw on.

    This function fills the window with a black background and displays instructions
    on how to play the game, including controls and objectives.
    """
    win.fill(BLACK)
    instructions_text = INSTRUCTIONS_FONT.render("Instructions:", 1, WHITE)
    controls_text = INSTRUCTIONS_FONT.render("- Player 1 (Left paddle): W (Up), S (Down)", 1, WHITE)
    controls_text2 = INSTRUCTIONS_FONT.render("- Player 2 (Right paddle): Arrow Up (Up), Arrow Down (Down)", 1, WHITE)
    objective_text = INSTRUCTIONS_FONT.render("- Score goals by hitting the ball past your opponent's paddle.", 1, WHITE)
    back_text = INSTRUCTIONS_FONT.render("Press 1 for AI, 2 for 2 player mode", 1, WHITE)
    enjoy_text = INSTRUCTIONS_FONT.render("Enjoy the game!", 1, WHITE)
    win.blit(instructions_text, (WIDTH // 2 - instructions_text.get_width() // 2, HEIGHT // 4))
    win.blit(controls_text, (WIDTH // 2 - controls_text.get_width() // 2, HEIGHT // 2 - FONT_SIZE))
    win.blit(controls_text2, (WIDTH // 2 - controls_text2.get_width() // 2, HEIGHT // 2))
    win.blit(objective_text, (WIDTH // 2 - objective_text.get_width() // 2, HEIGHT // 2 + FONT_SIZE))
    win.blit(back_text, (WIDTH // 2 - back_text.get_width() // 2, HEIGHT // 2 + 3 * FONT_SIZE))
    win.blit(enjoy_text, (WIDTH // 2 - enjoy_text.get_width() // 2, HEIGHT // 2 + 4 * FONT_SIZE))
    pygame.display.update()

def draw(win, paddles, ball, left_score, right_score, mode_prompt=None, timer=None, winner=None):
    """
    Draw the game elements on the window.

    Args:
        win (pygame.Surface): The surface to draw on.
        paddles (list): List of Paddle objects representing the paddles in the game.
        ball (Ball): Ball object representing the ball in the game.
        left_score (int): The score of the left player.
        right_score (int): The score of the right player.
        mode_prompt (str, optional): Prompt text for mode selection screen. Defaults to None.
        timer (int, optional): Countdown timer value. Defaults to None.
        winner (str, optional): Text indicating the winner. Defaults to None.

    If mode_prompt is provided, it displays the mode selection prompt. Otherwise, it draws the
    game elements including paddles, ball, scores, center divider, timer, and winner text if present.
    """
    win.fill(BLACK)
    if mode_prompt:
        mode_text = SCORE_FONT.render(mode_prompt, 1, WHITE)
        win.blit(mode_text, (WIDTH // 2 - mode_text.get_width() // 2, HEIGHT // 3))
    else:
        left_score_text = SCORE_FONT.render(f"{left_score}", 1, WHITE)
        right_score_text = SCORE_FONT.render(f"{right_score}", 1, WHITE)
        win.blit(left_score_text, (WIDTH // 4 - left_score_text.get_width() // 2, 20))
        win.blit(right_score_text, (WIDTH * (3 / 4) - right_score_text.get_width() // 2, 20))
        for paddle in paddles:
            paddle.draw(win)

        for i in range(10, HEIGHT, HEIGHT // 20):
            if i % 2 == 1:
                continue
            pygame.draw.rect(win, WHITE, (WIDTH // 2 - 5, i, 10, HEIGHT // 20))
        ball.draw(win)
        if timer is not None:
            timer_text = TIMER_FONT.render(f"{timer}", 1, WHITE)
            win.blit(timer_text, (WIDTH // 2 - timer_text.get_width() // 2, HEIGHT // 2 - timer_text.get_height() // 2))
        if winner:
            winner_text = WINNER_FONT.render(f"{winner} wins!", 1, WHITE)
            win.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, HEIGHT // 2 - winner_text.get_height() // 2))
    pygame.display.update()

def handle_collision(ball, left_paddle, right_paddle):
    """
    Handle collision between the ball and the paddles.

    Args:
        ball (Ball): The ball object.
        left_paddle (Paddle): The left paddle object.
        right_paddle (Paddle): The right paddle object.

    If the ball collides with the top or bottom of the window, its y velocity is reversed.
    If the ball's x velocity is negative (moving left), and it collides with the left paddle,
    its x velocity is reversed and its y velocity is adjusted based on the position of the collision
    relative to the center of the paddle.
    If the ball's x velocity is positive (moving right), and it collides with the right paddle,
    its x velocity is reversed and its y velocity is adjusted based on the position of the collision
    relative to the center of the paddle.
    """
    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1

    if ball.x_vel < 0:
        if ball.y >= left_paddle.rect.y and ball.y <= left_paddle.rect.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.rect.x + left_paddle.width:
                ball.x_vel *= -1

                middle_y = left_paddle.rect.y + left_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (left_paddle.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel
    else:
        if ball.y >= right_paddle.rect.y and ball.y <= right_paddle.rect.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.rect.x:
                ball.x_vel *= -1

                middle_y = right_paddle.rect.y + right_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (left_paddle.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel
