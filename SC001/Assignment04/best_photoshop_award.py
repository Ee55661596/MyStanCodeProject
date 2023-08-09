"""
File: best_photoshop_award.py
Name: Ethan 林劭懿
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage

# Controls the threshold of detecting green screen pixel
THRESHOLD = 1.5

# Controls the upper bound for black pixel
BLACK_PIXEL = 100


def main():
    """
    創作理念：接受人生一切的摧殘，躺平比較輕鬆一點
    """
    fg = SimpleImage('image_contest/ethan.jpg')
    bg = SimpleImage('image_contest/background.jpg')
    bg.make_as_big_as(fg)
    combined_img = combine(fg, bg)
    combined_img.show()


def combine(fg, bg):
    """
    : param1 bg: SimpleImage, the background image
    : param2 ma: SimpleImage, blue screen figure image
    : return fg: SimpleImage, the green screen pixels are replaced by pixels of background image
    """
    for x in range(fg.width):
        for y in range(fg.height):
            pixel_fg = fg.get_pixel(x, y)
            avg = (pixel_fg.red + pixel_fg.blue + pixel_fg.green) // 3
            total = pixel_fg.red + pixel_fg.blue + pixel_fg.green
            if pixel_fg.blue > avg * THRESHOLD and total > BLACK_PIXEL:
                pixel_bg = bg.get_pixel(x, y)
                pixel_fg.red = pixel_bg.red
                pixel_fg.blue = pixel_bg.blue
                pixel_fg.green = pixel_bg.green
    return fg


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
