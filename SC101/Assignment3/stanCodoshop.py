"""
File: stanCodoshop.py
Name: Ethan 林劭懿
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    red_dist = (red - pixel.red)**2
    green_dist = (green - pixel.green)**2
    blue_dist = (blue - pixel.blue)**2
    color_distance = (red_dist + green_dist + blue_dist)**(1/2)
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    # initial setting
    red_pixel_sum = 0
    green_pixel_sum = 0
    blue_pixel_sum = 0

    # calculate sum
    pixel_num = len(pixels)
    for pixel in pixels:
        red_pixel_sum += pixel.red
        green_pixel_sum += pixel.green
        blue_pixel_sum += pixel.blue

    # calculate average
    red_pixel_avg = int(red_pixel_sum / pixel_num)
    green_pixel_avg = int(green_pixel_sum / pixel_num)
    blue_pixel_avg = int(blue_pixel_sum / pixel_num)

    return [red_pixel_avg, green_pixel_avg, blue_pixel_avg]

    # red = 0
    # green = 0
    # blue = 0
    # color_list = []
    # for tokens in pixels:
    #     red_token = tokens[0]
    #     red += red_token
    #     green_token = tokens[1]
    #     green += green_token
    #     blue_token = tokens[2]
    #     blue += blue_token
    # red_avg = red/len(pixels)
    # color_list += red_avg
    # green_avg = green/len(pixels)
    # color_list += green_avg
    # blue_avg = blue/len(pixels)
    # color_list += blue_avg


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    red_pixel_avg = get_average(pixels)[0]
    green_pixel_avg = get_average(pixels)[1]
    blue_pixel_avg = get_average(pixels)[2]

    # set initial condition
    pixel_dist_min = 999999999
    fittest = pixels[0]

    for pixel in pixels:
        pixel_dist = get_pixel_dist(pixel, red_pixel_avg, green_pixel_avg, blue_pixel_avg)
        if pixel_dist < pixel_dist_min:
            pixel_dist_min = pixel_dist
            fittest = pixel

    return fittest


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    for x in range(width):
        for y in range(height):
            fittest_pixel = get_best_pixel([images[i].get_pixel(x, y) for i in range(len(images))])
            result_pixel = result.get_pixel(x, y)
            result_pixel.red = fittest_pixel.red
            result_pixel.green = fittest_pixel.green
            result_pixel.blue = fittest_pixel.blue

    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
