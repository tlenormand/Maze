#!/usr/bin/python3

def generate_gradient_rgbs(num_buckets):
    rgb_codes = []
    step_size = 1024 / num_buckets
    for step in range(0,num_buckets):
        red = int(max(0, 255 - (step_size*step*0.5))) # step size is half of the step size since both this item goes down and the next one goes up
        blue = int(max(0, 255 - (step_size*0.5*(num_buckets-step-1))))
        green = (255 - red) if red else (255 - blue)
        rgb_codes.append((red, green, blue))
    return rgb_codes
