"""
File: blur.py
Name: 林劭懿 Ethan
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img:smiley-face.png
    :return: b_img, the image with blur filter.
    """
    # Todo: create a new blank img that is as big as the original one
    b_img = SimpleImage.blank(img.width, img.height)
    # Loop over the picture
    for x in range(img.width):
        for y in range(img.height):

            # set up get_pixel
            img_p = img.get_pixel(x, y)
            b_img_p = b_img.get_pixel(x, y)

            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.

            if x == 0 and y == 0:
                # Get pixel at the top-left corner of the image.
                # b_img_coner = b_img.get_pixel(x, y)
                b_img_10 = img.get_pixel(x+1, y)
                b_img_01 = img.get_pixel(x, y+1)
                b_img_11 = img.get_pixel(x+1, y + 1)
                r_avg = (b_img_10.red + b_img_01.red + b_img_11.red + img_p.red) // 4
                b_avg = (b_img_10.blue + b_img_01.blue + b_img_11.blue + img_p.blue) // 4
                g_avg = (b_img_10.green + b_img_01.green + b_img_11.green + img_p.green) // 4
                b_img_p.red = r_avg
                b_img_p.blue = b_avg
                b_img_p.green = g_avg
            elif x == img.width-1 and y == 0:
                # Get pixel at the top-right corner of the image.
                # b_img_coner_r = b_img.get_pixel(x, y)
                b_img_wid0 = img.get_pixel(img.width-2, y)
                b_img_wid1 = img.get_pixel(img.width-1, y+1)
                b_img_widhei = img.get_pixel(img.width-2, y + 1)
                r_avg = (b_img_wid0.red + b_img_wid1.red + b_img_widhei.red + img_p.red) // 4
                b_avg = (b_img_wid0.blue + b_img_wid1.blue + b_img_widhei.blue + img_p.blue) // 4
                g_avg = (b_img_wid0.green + b_img_wid1.green + b_img_widhei.green + img_p.green) // 4
                b_img_p.red = r_avg
                b_img_p.blue = b_avg
                b_img_p.green = g_avg

            elif x == 0 and y == img.height-1:
                # Get pixel at the bottom-left corner of the image
                # b_img_coner_bottom_left = b_img.get_pixel(x, y)
                b_img_right = img.get_pixel(x+1, y-1)
                b_img_up = img.get_pixel(x, y-1)
                b_img_right_up = img.get_pixel(x+1, y - 1)
                r_avg = (b_img_right.red + b_img_up.red + b_img_right_up.red + img_p.red) // 4
                b_avg = (b_img_right.blue + b_img_up.blue + b_img_right_up.blue + img_p.blue) // 4
                g_avg = (b_img_right.green + b_img_up.green + b_img_right_up.green + img_p.green) // 4
                b_img_p.red = r_avg
                b_img_p.blue = b_avg
                b_img_p.green = g_avg

            elif x == img.width-1 and y == img.height-1:
                # Get pixel at the bottom-right corner of the image
                # b_img_coner_bottom_right = b_img.get_pixel(x, y)
                b_img_left = img.get_pixel(x - 1, y)
                b_img_up = img.get_pixel(x, y - 1)
                b_img_left_up = img.get_pixel(x - 1, y - 1)
                r_avg = (b_img_left.red + b_img_up.red + b_img_left_up.red + img_p.red) // 4
                b_avg = (b_img_left.blue + b_img_up.blue + b_img_left_up.blue + img_p.blue) // 4
                g_avg = (b_img_left.green + b_img_up.green + b_img_left_up.green + img_p.green) // 4
                b_img_p.red = r_avg
                b_img_p.blue = b_avg
                b_img_p.green = g_avg
            elif 0 < x < img.width-1 and y == 0:
                # Get top edge's pixels (without two corners)
                # b_img_topedge = img.get_pixel(x, y)
                b_img_left = img.get_pixel(x - 1, y)
                b_img_right = img.get_pixel(x + 1, y)
                b_img_down = img.get_pixel(x, y+1)
                b_img_left_down = img.get_pixel(x - 1, y+1)
                b_img_right_down = img.get_pixel(x + 1, y + 1)
                r_avg = (b_img_left.red + b_img_right.red + b_img_down.red + b_img_left_down.red + b_img_right_down.red + img_p.red) // 6
                b_avg = (b_img_left.blue + b_img_right.blue + b_img_down.blue + b_img_left_down.blue + b_img_right_down.blue + img_p.blue) // 6
                g_avg = (b_img_left.green + b_img_right.green + b_img_down.green + b_img_left_down.green + b_img_right_down.green + img_p.green) // 6
                b_img_p.red = r_avg
                b_img_p.blue = b_avg
                b_img_p.green = g_avg

            elif 0 < x < img.width-1 and y == img.height-1:
                # Get bottom edge's pixels (without two corners)
                # b_img_bottom_edge = b_img.get_pixel(x, y)
                b_img_left = img.get_pixel(x - 1, y)
                b_img_right = img.get_pixel(x + 1, y)
                b_img_up = img.get_pixel(x, y-1)
                b_img_left_up = img.get_pixel(x - 1, y-1)
                b_img_right_up = img.get_pixel(x - 1, y - 1)
                r_avg = (b_img_left.red + b_img_right.red + b_img_up.red + b_img_left_up.red + b_img_right_up.red + img_p.red) // 6
                b_avg = (b_img_left.blue + b_img_right.blue + b_img_up.blue + b_img_left_up.blue + b_img_right_up.blue + img_p.blue) // 6
                g_avg = (b_img_left.green + b_img_right.green + b_img_up.green + b_img_left_up.green + b_img_right_up.green + img_p.green) // 6
                b_img_p.red = r_avg
                b_img_p.blue = b_avg
                b_img_p.green = g_avg

            elif x == 0 and 0 < y < img.height-1:
                # Get left edge's pixels (without two corners)
                # b_img_left_edge = b_img.get_pixel(x, y)
                b_img_right = img.get_pixel(x + 1, y)
                b_img_up = img.get_pixel(x, y - 1)
                b_img_down = img.get_pixel(x, y + 1)
                b_img_right_up = img.get_pixel(x+1, y - 1)
                b_img_right_down = img.get_pixel(x + 1, y + 1)
                r_avg = (b_img_right.red + b_img_up.red + b_img_right_up.red + b_img_down.red + b_img_right_down.red + img_p.red) // 6
                b_avg = (b_img_right.blue + b_img_up.blue + b_img_right_up.blue + b_img_down.blue + b_img_right_down.blue + img_p.blue) // 6
                g_avg = (b_img_right.green + b_img_up.green + b_img_right_up.green + b_img_down.green + b_img_right_down.green + img_p.green) // 6
                b_img_p.red = r_avg
                b_img_p.blue = b_avg
                b_img_p.green = g_avg
            elif x == img.width-1 and 0 < y < img.height-1:
                # Get right edge's pixels (without two corners)
                # b_img_right_edge = b_img.get_pixel(x, y)
                b_img_left = img.get_pixel(x - 1, y)
                b_img_up = img.get_pixel(x, y - 1)
                b_img_down = img.get_pixel(x, y + 1)
                b_img_left_up = img.get_pixel(x-1, y - 1)
                b_img_left_down = img.get_pixel(x - 1, y + 1)
                r_avg = (b_img_left.red + b_img_up.red + b_img_left_up.red + b_img_down.red + b_img_left_down.red + img_p.red) // 6
                b_avg = (b_img_left.blue + b_img_up.blue + b_img_left_up.blue + b_img_down.blue + b_img_left_down.blue + img_p.blue) // 6
                g_avg = (b_img_left.green + b_img_up.green + b_img_left_up.green + b_img_down.green + b_img_left_down.green + img_p.green) // 6
                b_img_p.red = r_avg
                b_img_p.blue = b_avg
                b_img_p.green = g_avg

            else:
                # Inner pixels.
                # b_img_else = img.get_pixel(x, y)
                b_img_up = img.get_pixel(x, y - 1)
                b_img_down = img.get_pixel(x, y + 1)
                b_img_left = img.get_pixel(x - 1, y)
                b_img_right = img.get_pixel(x + 1, y)
                b_img_right_up = img.get_pixel(x + 1, y - 1)
                b_img_right_down = img.get_pixel(x + 1, y + 1)
                b_img_left_up = img.get_pixel(x - 1, y - 1)
                b_img_left_down = img.get_pixel(x - 1, y + 1)
                r_avg = (b_img_right_down.red + b_img_right.red + b_img_right_up.red + b_img_left.red + b_img_up.red + b_img_left_up.red + b_img_down.red + b_img_left_down.red + img_p.red) // 9
                b_avg = (b_img_right_down.blue + b_img_right.blue + b_img_right_up.blue + b_img_left.blue + b_img_up.blue + b_img_left_up.blue + b_img_down.blue + b_img_left_down.blue + img_p.blue) // 9
                g_avg = (b_img_right_down.green + b_img_right.green + b_img_right_up.green + b_img_left.green + b_img_up.green + b_img_left_up.green + b_img_down.green + b_img_left_down.green + img_p.green) // 9
                b_img_p.red = r_avg
                b_img_p.blue = b_avg
                b_img_p.green = g_avg



    return b_img


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
