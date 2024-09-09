import sys
import os
picdir = "/home/samaniego/OLED_Module_Code/RaspberryPi/python/pic"
libdir = "/home/samaniego/OLED_Module_Code/RaspberryPi/python/lib"
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
import time
import traceback
from waveshare_OLED import OLED_0in96
from PIL import Image,ImageDraw,ImageFont
logging.basicConfig(level=logging.DEBUG)


def show(direcao):
    try:
        disp = OLED_0in96.OLED_0in96()

        logging.info("\r 0.96inch OLED ")
        # Initialize library.
        disp.Init()
        # Clear display.
        logging.info("clear display")
        disp.clear()

        # Create blank image for drawing.
        image1 = Image.new('1', (disp.width, disp.height), "WHITE")
        draw = ImageDraw.Draw(image1)
        font1 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 30)
        logging.info ("Escrevendo texto...")
        draw.text((30,0), direcao, font = font1, fill = 0)
        #image1 = image1.rotate(0)
        disp.ShowImage(disp.getbuffer(image1))
        time.sleep(5)

    except IOError as e:
        logging.info(e)

    except KeyboardInterrupt:
        logging.info("ctrl + c:")
        disp.module_exit()
        exit()


