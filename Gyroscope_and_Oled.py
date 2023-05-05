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


# Read gyroscope data and display on OLED

while True:
    print("Temp : "+str(mpu.get_temp()))
    print()

    accel_data = mpu.get_accel_data()
    print("Acc X : "+str(accel_data['x']))
    print("Acc Y : "+str(accel_data['y']))
    print("Acc Z : "+str(accel_data['z']))
    print()

    gyro_data = mpu.get_gyro_data()
    print("Gyro X : "+str(gyro_data['x']))
    print("Gyro Y : "+str(gyro_data['y']))
    print("Gyro Z : "+str(gyro_data['z']))
    print()
    print("-------------------------------")
    
    # Loop over the images and display each one on the OLED display
    for image in images:
        with canvas(device1) as draw:
            draw.bitmap((0, 0), image, fill=1)
        with canvas(device2) as draw:
            draw.bitmap((0, 0), image, fill=1)
        time.sleep(1)
