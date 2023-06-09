import asyncio
import psutil

from luma.core.interface.serial import i2c
from luma.oled.device import sh1106
from luma.core.render import canvas
from PIL import Image
import time
from mpu6050 import mpu6050


# OLED display dimensions
width = 128
height = 64

# Initialize OLED display
serial1 = i2c(port=3, address=0x3C)
device1 = sh1106(serial1)

#Second OLED display
serial2 = i2c(port=4, address=0x3C)
device2 = sh1106(serial2)

# Initialize MPU6050 sensor
mpu = mpu6050(0x68, bus = 1)

# Load the sequence of images
images = [
    Image.open('Cherry.png'),
    Image.open('Cherry2.bmp'),
    Image.open('Cherry.png')
]

# Resize the images to fit the OLED display
images = [image.resize((width, height), Image.LANCZOS) for image in images]


async def proximitly_sensor():
    mem = psutil.virtual_memory()
    total_memory = mem.total / (1024 * 1024)
    available_memory = mem.available / (1024 * 1024)
    used_memory = mem.used / (1024 * 1024)
    print("proximitly")
    for image in images:
        with canvas(device1) as draw:
            draw.bitmap((0, 0), image, fill=1)
        with canvas(device2) as draw:
            draw.bitmap((0, 0), image, fill=1)
        time.sleep(1)
    #print(total_memory)
    #print(used_memory)
    #print(available_memory)

async def pressure_sensor():
    print("pressure")

async def main():
    await asyncio.gather(proximitly_sensor(), pressure_sensor())

def sleepMode(mode):
    asyncio.run(main())


    

