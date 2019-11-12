import video,time
from Maix import GPIO

# disable wifi
fm.register(8,  fm.fpioa.GPIO0)
wifi_en=GPIO(GPIO.GPIO0, GPIO.OUT)
wifi_en.value(0)

# register i2s(i2s0) pin
fm.register(34,  fm.fpioa.I2S0_OUT_D1)
fm.register(35,  fm.fpioa.I2S0_SCLK)
fm.register(33,  fm.fpioa.I2S0_WS)

v = video.open("/sd/bad_apple.avi")
print(v)
v.volume(20)
while True:
    if v.play() == 0:
        print("play end")
        break
v.__del__()
