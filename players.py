import pygame
from entities import Ball, Paddle
# AIPlayer class definition
class AIPlayer:
    """
    Represents an AI player in the game.

    This AI player is responsible for moving its associated paddle based on the movement of the ball.

    Attributes:
        paddle (Paddle): The paddle controlled by the AI player.
        ball (Ball): The ball object being tracked by the AI player.
    """
    def __init__(self, paddle, ball):
        """
        Initialize the AIPlayer with the specified paddle and ball objects.

        Args:
            paddle (Paddle): The paddle object controlled by the AI player.
            ball (Ball): The ball object being tracked by the AI player.
        """
        self.paddle = paddle
        self.ball = ball

    def move(self):
        """
        Move the paddle based on the position of the ball.

        The paddle moves up or down depending on the position of the ball relative to its own position.
        """
        if self.ball.x_vel > 0:
            if self.ball.y < self.paddle.rect.centery:
                if self.paddle.rect.top - self.paddle.VEL >= 0:
                    self.paddle.move(up=True)
            elif self.ball.y > self.paddle.rect.centery:
                if self.paddle.rect.bottom + self.paddle.VEL <= HEIGHT:
                    self.paddle.move(up=False)

# TwoPlayerMode class definition
class TwoPlayerMode:
    """
    Represents a two-player mode in the game.

    This mode allows two human players to control the left and right paddles using specified keys.

    Attributes:
        left_paddle (Paddle): The paddle object controlled by the left player.
        right_paddle (Paddle): The paddle object controlled by the right player.
    """
    def __init__(self, left_paddle, right_paddle):
        """
        Initialize the TwoPlayerMode with the specified left and right paddle objects.

        Args:
            left_paddle (Paddle): The paddle object controlled by the left player.
            right_paddle (Paddle): The paddle object controlled by the right player.
        """
        self.left_paddle = left_paddle
        self.right_paddle = right_paddle

    def move(self, keys):
        """
        Move the paddles based on the pressed keys.

        Args:
            keys (dict): A dictionary containing the state of pressed keys.

        The paddles move up or down based on the keys pressed by the left and right players.
        """
        if keys[pygame.K_w] and self.left_paddle.rect.top - self.left_paddle.VEL >= 0:
            self.left_paddle.move(up=True)
        if keys[pygame.K_s] and self.left_paddle.rect.bottom + self.left_paddle.VEL <= HEIGHT:
            self.left_paddle.move(up=False)

        if keys[pygame.K_UP] and self.right_paddle.rect.top - self.right_paddle.VEL >= 0:
            self.right_paddle.move(up=True)
        if keys[pygame.K_DOWN] and self.right_paddle.rect.bottom + self.right_paddle.VEL <= HEIGHT:
            self.right_paddle.move(up=False)
