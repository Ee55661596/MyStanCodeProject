"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
Name: Ethan 林劭懿
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 20      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
BRICK_COL_LIST = ['red', 'orange', 'yellow', 'green', 'blue']  # List for the brick color

# Global variable
unlock = True


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2, y=self.window.height-paddle_offset)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                        y=(self.window.height - self.ball.height) / 2)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        # Initialize our mouse listeners
        onmousemoved(self.move_paddle)
        onmouseclicked(self.move_ball)

        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height,
                                   x=j*(brick_spacing + brick_width), y=brick_offset+i*(brick_spacing+brick_height))
                self.brick.filled = True
                self.brick.fill_color = BRICK_COL_LIST[i // 2]
                self.window.add(self.brick)
                
    #     number of bricks
        self.brick_num = BRICK_COLS * BRICK_ROWS

    def move_paddle(self, mouse_move):
        """
        This function may allow the paddle move horizontally.
        """
        mouse_center = mouse_move.x - self.paddle.width/2
        if mouse_center < (self.paddle.width/2):
            self.paddle.x = 0
        elif mouse_center > (self.window.width - self.paddle.width):
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = mouse_center

    def move_ball(self, mouse_switch):
        """
        This function trigger the start of the game
        """
        global unlock
        if unlock:
            unlock = False
            # set ball's random velocity
            self.set_ball_velocity()

    def set_ball_velocity(self):
        """
        This function set the initial speed and direction when the ball start falling.
        """
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randrange(1, MAX_X_SPEED)

        if random.random() > 0.5:
            self.__dx = -self.__dx

    def reset_ball(self):
        global unlock
        # reset position
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = (self.window.height - self.ball.height) / 2
        # reset velocity
        self.__dx = 0
        self.__dy = 0
        unlock = True

    def reflect_ball_x(self):
        self.__dx = -self.__dx

    def reflect_ball_y(self):
        self.__dy = -self.__dy
        
# get value of dx, dy
    
    def get_dx(self):
        return self.__dx
    
    def get_dy(self):
        return self.__dy
