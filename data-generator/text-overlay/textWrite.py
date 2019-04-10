#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: abqader
"""

from PIL import Image, ImageDraw, ImageFont
import os 
from random import randint 


font_size = 100


def textWrite(imgx, text):
    '''
    imgx: The image to add text to 
    text: The Arabic text to overlay on top

    Result: saves the image to the same directory with "texter" added to the filename 
    '''
    img = Image.open(imgx)
    img = img.convert('RGB')
    draw = ImageDraw.Draw(img)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    pather = dir_path + '/arial.ttf'
    font = ImageFont.truetype(pather, font_size, encoding="unic")
    
    reversed_text = reversed(text)
    
    fill = (0,0,0)
    font = font
    
    string_text = ""
    for i in reversed_text:
        string_text += i
    x = (randint(0, 100))
    y = (randint(0, 100))
    draw.text((x, y), string_text, fill, font)
    newFiler = imgx[:-4] + 'texter.jpg'
    img.save(newFiler)
    

# -- Example Case -- #
    
text = "ڕۆژتان باش ئازیزان"

for file in os.listdir('/Users/abqader/Desktop/terrorPositiveNew/'):
    if file == '.DS_Store':
        continue
    textWrite('/Users/abqader/Desktop/terrorPositiveNew/' + file, text)
    


    