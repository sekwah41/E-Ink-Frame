#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import logging
from waveshare_epd import epd5in65f
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
import sys

logging.basicConfig(level=logging.DEBUG)
display_width = 600
display_height = 448

def centerImage(image):
    result = Image.new('RGB', (display_width, display_height), 0xffffff)
    left = int((display_width - image.width) / 2)
    top = int((display_height - image.height) / 2)
    result.paste(image, (left, top))
    return result

if len(sys.argv) == 0:
    logging.info("Please specify image")
    exit(-1)

try:
    logging.info("Aidan Demo")
    
    epd = epd5in65f.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear()

    Himage = centerImage(Image.open(sys.argv[1]))
    epd.display(epd.getbuffer(Himage))
    time.sleep(3)
    
    logging.info("Goto Sleep...")
    epd.sleep()
    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd5in65f.epdconfig.module_exit()
    exit()
