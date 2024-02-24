import pygame
# Paddle class definition
class Paddle:
    """
    Class representing a paddle object in the game.
    """
    COLOR = WHITE
    VEL = 4

    def __init__(self, x, y, width, height):
        """
        Initialize a paddle object with given position and dimensions.

        Args:
            x (int): X-coordinate of the top-left corner of the paddle.
            y (int): Y-coordinate of the top-left corner of the paddle.
            width (int): Width of the paddle.
            height (int): Height of the paddle.
        """
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.original_x = x
        self.original_y = y

    def draw(self, win):
        """
        Draw the paddle on the given window.

        Args:
            win (pygame.Surface): The surface to draw the paddle on.
        """
        pygame.draw.rect(win, self.COLOR, self.rect)

    def move(self, up=True):
        """
        Move the paddle up or down.

        Args:
            up (bool): If True, move the paddle up. If False, move it down.
        """
        if up:
            self.rect.y -= self.VEL
        else:
            self.rect.y += self.VEL

    def reset(self):
        """Reset the paddle to its original position."""
        self.rect.x = self.original_x
        self.rect.y = self.original_y

# Ball class definition
class Ball:
    """
    Class representing a ball object in the game.
    """
    COLOR = WHITE

    def __init__(self, x, y, radius, max_vel):
        """
        Initialize a ball object with given position, radius, and maximum velocity.

        Args:
            x (int): X-coordinate of the center of the ball.
            y (int): Y-coordinate of the center of the ball.
            radius (int): Radius of the ball.
            max_vel (float): Maximum velocity of the ball.
        """
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = random.choice([-1, 1]) * random.uniform(4, 6)
        self.y_vel = random.choice([-1, 1]) * random.uniform(1, 3)
        self.MAX_VEL = max_vel
        self.last_goal_time = 0
        self.goal_scored_flag = False

    def draw(self, win):
         """
        Draw the ball on the given window.

        Args:
            win (pygame.Surface): The surface to draw the ball on.
        """
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

    def move(self):
        """Move the ball according to its velocity."""
        if not self.goal_scored_flag:
            self.x += self.x_vel
            self.y += self.y_vel

    def reset(self, towards_left=True):
        """
        Reset the ball's position and velocity, optionally directing it towards the left.

        Args:
            towards_left (bool): If True, direct the ball towards the left. Default is True.
        """
        self.x = self.original_x
        self.y = self.original_y
        self.x_vel = random.uniform(4, 6)
        if towards_left:
            self.x_vel *= -1
        self.y_vel = random.choice([-1, 1]) * random.uniform(1, 3)
        self.goal_scored_flag = False

    def goal_scored(self):
        """Update the time of the last goal scored and set the goal scored flag."""
        self.last_goal_time = time.time()
        self.goal_scored_flag = True
