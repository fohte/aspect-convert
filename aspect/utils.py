import math


def aspect_ratio(size: (int, int)) -> (int, int):
    width, height = size
    gcd = math.gcd(width, height)
    x = int(width / gcd)
    y = int(height / gcd)
    return x, y


def convert(size: (int, int), to_ratio: (int, int), trim: bool = True) -> (int, int):
    width, height = size
    from_ratio = aspect_ratio(size)
    x_scale = from_ratio[0] / to_ratio[0]
    y_scale = from_ratio[1] / to_ratio[1]

    if trim:
        if x_scale > y_scale:
            w = width / x_scale * y_scale
            h = height

        else:
            w = width
            h = height / y_scale * x_scale

    else:
        if x_scale > y_scale:
            w = width
            h = height / y_scale * x_scale

        else:
            w = width / x_scale * y_scale
            h = height

    return int(w), int(h)
