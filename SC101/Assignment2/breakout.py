"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
Name : Ethan 林劭懿
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GOval, GRect, GLabel
FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts
# Global Variable
graphics = BreakoutGraphics()
lives = NUM_LIVES
score = 0
lives_label = GLabel('lives:', str(lives))
lives_label.text = 'lives: ' + str(lives)
score_label = GLabel('Score:', str(score))
score_label.text = 'Score: ' + str(score)
# Add the animation loop here!


def main():
    global lives, score, graphics
    graphics.window.add(lives_label, x=graphics.window.width-lives_label.width-5, y=lives_label.height+5)
    graphics.window.add(score_label, x=5, y=lives_label.height + 5)
    while True:
        # end game
        if lives == 0 or graphics.brick_num == 0:
            lives_label.text = 'lives: ' + str(lives)
            final_page = GRect(graphics.window.width, graphics.window.height)
            final_page.filled = True
            final_page.fill_color = 'white'
            f_score = score
            final_score = GLabel('Score:', str(f_score))
            final_score.text = 'Score:', str(f_score)
            final_score.font = '-50'
            graphics.window.add(final_page)
            graphics.window.add(final_score, x=(graphics.window.width - final_score.width) / 2, y=(graphics.window.height - final_score.height) / 2)
            break

        # Lose life
        if graphics.ball.y >= graphics.window.height:
            lives -= 1
            graphics.reset_ball()
            lives_label.text = 'lives: ' + str(lives)
        # check the vertex
        ball_ul = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        ball_ur = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y)
        ball_bl = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height)
        ball_br = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                                graphics.ball.y + graphics.ball.height)

        # reflection : bricks
        if ball_ul is not None and ball_ul is not graphics.paddle:
            reflection(ball_ul)
            score += 5
            score_label.text = 'Score: ' + str(score)
        elif ball_ur is not None and ball_ur is not graphics.paddle:
            reflection(ball_ur)
            score += 5
            score_label.text = 'Score: ' + str(score)
        elif ball_bl is not None and ball_bl is not graphics.paddle:
            reflection(ball_ul)
            score += 5
            score_label.text = 'Score: ' + str(score)
        elif ball_br is not None and ball_br is not graphics.paddle:
            reflection(ball_br)
            score += 5
            score_label.text = 'Score: ' + str(score)

        # reflection : paddle
        if ball_ul is not None and ball_ul is graphics.paddle:
            reflection(ball_ul)
        elif ball_ur is not None and ball_ur is graphics.paddle:
            reflection(ball_ur)
        elif ball_bl is not None and ball_bl is graphics.paddle:
            reflection(ball_ul)
        elif ball_br is not None and ball_br is graphics.paddle:
            reflection(ball_br)

        # reflection : wall
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics.reflect_ball_x()
        if graphics.ball.y <= 0:
            graphics.reflect_ball_y()

        # move the ball
        dx = graphics.get_dx()
        dy = graphics.get_dy()
        graphics.ball.move(dx, dy)
        pause(FRAME_RATE)


def reflection(ball_part):
    global graphics
#     remove the bricks and reflect the ball from bricks
    if ball_part != graphics.paddle:
        graphics.window.remove(ball_part)
        graphics.brick_num -= 1
        graphics.reflect_ball_y()
#     reflect the ball from the paddle
    else:
        dy = graphics.get_dy()
        if dy > 0:
            graphics.reflect_ball_y()


if __name__ == '__main__':
    main()
