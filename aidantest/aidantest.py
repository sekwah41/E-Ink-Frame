#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import logging
from waveshare_epd import epd5in65f
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("Aidan Demo")
    
    epd = epd5in65f.EPD()
    logging.info("init and Clear")
    epd.init()

    Himage = Image.open('aidan.bmp')
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
