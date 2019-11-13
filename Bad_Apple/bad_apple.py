import video,time
import lcd
from fpioa_manager import *
from Maix import GPIO

lcd.init(freq=15000000)

########### settings ############
WIFI_EN_PIN     = 8
# AUDIO_PA_EN_PIN = None  # Bit Dock and old MaixGo
AUDIO_PA_EN_PIN = 32      # Maix Go(version 2.20)
# AUDIO_PA_EN_PIN = 2     # Maixduino


# disable wifi
fm.register(WIFI_EN_PIN, fm.fpioa.GPIO0)
wifi_en=GPIO(GPIO.GPIO0, GPIO.OUT)
wifi_en.value(0)

# open audio PA
if AUDIO_PA_EN_PIN:
    fm.register(AUDIO_PA_EN_PIN, fm.fpioa.GPIO1)
    wifi_en=GPIO(GPIO.GPIO1, GPIO.OUT)
    wifi_en.value(1)

# register i2s(i2s0) pin
fm.register(34,fm.fpioa.I2S0_OUT_D1)
fm.register(35,fm.fpioa.I2S0_SCLK)
fm.register(33,fm.fpioa.I2S0_WS)

v = video.open("/sd/bad_apple.avi")
print(v)
v.volume(15)
while True:
    if v.play() == 0:
        print("play end")
        break
v.__del__()
