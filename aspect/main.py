import os

import click
import numpy
import PIL.Image

from . import utils


def as_ndarray(img: PIL.Image.Image) -> numpy.ndarray:
    return numpy.asarray(img)


def as_pil(img: numpy.ndarray) -> PIL.Image.Image:
    return PIL.Image.fromarray(numpy.uint8(img))


@click.group()
def main():
    pass


@main.command()
@click.argument('input', type=click.Path(exists=True))
def show(input):
    with PIL.Image.open(input) as image:
        x, y = utils.aspect_ratio(image.size)
        print("{}:{}".format(x, y))


@main.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--output', '-o', type=click.Path(), default='.')
@click.option('--in-place', '-i', is_flag=True)
@click.option('--ratio', '-r', type=(int, int), default=(1, 1))
@click.option('--trim/--no-trim', default=True)
def convert(input, output, in_place, ratio, trim):
    filename = os.path.basename(input)

    if in_place:
        output_file = input
    elif os.path.isdir(output):
        output_file = os.path.join(output, filename)
    else:
        output_file = output

    with PIL.Image.open(input) as image:
        w, h = utils.convert(image.size, ratio, trim=True)
        x_offset = int((image.size[0] - w) / 2)
        y_offset = int((image.size[1] - h) / 2)

        pixels = as_ndarray(image)
        converted = pixels[y_offset: y_offset + h, x_offset: x_offset + w]
        as_pil(converted).save(output_file)

if __name__ == '__main__':
    main()
