#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random
import os, sys


def read_image_info(name):
    im = Image.open(name + '.jpeg')
    w, h = im.size

    print('w = ' + str(w) + ' h = ' + str(h))

    # im.thumbnail((w//2,h//2)) # create a thumbnail with designated width and height\

    im = im.filter(ImageFilter.BLUR)  # blur a image as we want
    im.save(name + '_thumbnail.png', 'png')


# 生成验证码
def generate_capata():
    width = 60 * 4
    height = 60

    image = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建Font对象:
    path = os.path.curdir
    font = ImageFont.truetype(os.path.join(path, 'arial.ttf'), 36)
    # 创建Draw对象:
    draw = ImageDraw.Draw(image)
    # 填充每个像素:
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())

    # 输出文字:
    for t in range(4):
        draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
    # 模糊:
    image = image.filter(ImageFilter.BLUR)
    image.save('captia.jpg', 'jpeg')

    pass


# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))


# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


def convert_file_to_jpeg():
    for infile in sys.argv[1:]:
        f, e = os.path.splitext(infile)
        outfile = f + ".jpeg"
        if infile != outfile:
            try:
                Image.open(infile).save(outfile)
            except IOError:
                print("cannot convert", infile)


# using the default image viewer to show the image
def show_image():
    im = Image.open('Image_65.jpeg')
    print(im.format, im.size, im.mode)
    im.show()


def roll(image, delta):
    "Roll an image sideways"

    xsize, ysize = image.size

    delta = delta % xsize
    if delta == 0: return image

    part1 = image.crop((0, 0, delta, ysize))
    part2 = image.crop((delta, 0, xsize, ysize))
    image.paste(part2, (0, 0, xsize - delta, ysize))
    image.paste(part1, (xsize - delta, 0, xsize, ysize))
    image.save('roll67.jpeg')


def rotate_image(im):
    # out = im.resize((128, 128))
    out = im.rotate(45)  # degrees counter-clockwise
    out.show()

if __name__ == '__main__':
    # read_image_info('Image_67')
    # generate_capata()
    # convert_file_to_jpeg()
    # show_image()
    # roll(Image.open('Image_67.jpeg'), 90)
    rotate_image(Image.open('Image_67.jpeg'))
