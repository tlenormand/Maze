#!/usr/bin/python3
from Models import *


def sub_to_hexa(key, rgb_idx):
    """
    translates an rgb tuple of int to an hexa color

    Arguments:
        key: index of a maze color dictionnary to stock into
        rgb_idx: index of the color to get from the "key" dictionnary

    Return:
        an hexadecimal color
    """
    r, g, b = Maze_class._maze_rgb_dict[key][rgb_idx]
    hexa_color = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return hexa_color


def generate_gradient_rgbs(num_buckets):
    """
    function that create "num_buckets" times a r, g, b color

    Arguments:
        num_buckets: the number of color needed to be created

    Return:
        a tuple (r, g, b) color
    """
    if num_buckets == 0:
        return ([(255, 255, 255)])
    rgb_codes = []
    step_size = 1024 / num_buckets
    for step in range(0, num_buckets):
        red = int(max(0, 255 - (step_size * step * 0.5)))
        blue = int(max(0, 255 - (step_size * 0.5 * (num_buckets - step - 1))))
        green = (255 - red) if red else (255 - blue)
        rgb_codes.append((red, green, blue))
    return rgb_codes
