import network

def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('yourSSID(Name of the wlan)', 'yourpassword')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
from machine import Pin,PWM
import time

magnet = Pin(4,Pin.OUT)
#4脚接电磁铁控制器
#输出低电压启动

# = Pin(,Pin.OUT)
##_脚接_

pwm = PWM(Pin(5),1000)
#5接PWM调节转速

rotate_1 = Pin(16,Pin.OUT)
rotate_2 = Pin(17,Pin.OUT)
#16-17接电机IO


led = Pin(2,Pin.OUT)
#在pin2上有蓝色led
duty = 1000

##初始化装置
machineStatus = "IDLE"

magnet.value(1)
rotate_1.value(0)
rotate_2.value(0)

def Magnet_on():
    print("开启磁铁")
    magnet.value(0)
#开磁铁

def Magnet_off():
    print("关闭磁铁")
    magnet.value(1)

#关磁铁

def Up(moveTime):
    print("向上升磁铁 " + str(moveTime) + " 秒")
    pwm.duty(duty)
    rotate_1.value(1)
    rotate_2.value(0)
    Wait(moveTime)
    Brake()
#上升

def Down(moveTime):
    print("向下降磁铁 " + str(moveTime) + " 秒")
    pwm.duty(duty)
    rotate_1.value(0)
    rotate_2.value(1)
    Wait(moveTime)
    Brake()
#下降
def Brake(reason = "DEFAULT"):
    global machineStatus
    rotate_1.value(1)
    rotate_2.value(1)
    #should set the driver speed to 0 and magnet off
    if reason != "DEFAULT":
        machineStatus = "ABORTED"
        print("机器由于" + str(reason) + "终止运行")
        exit()

#刹车

def Wait(someTime):
    print("等待 " + str(someTime) + " 秒")
    try:
        time.sleep(someTime)
    except KeyboardInterrupt:
        Brake("Keyboard Interrupt")


def singleBounce(catchTime):
    Magnet_off()
    #lift down to a lower level to catch the ball after it single bounces
    Down(catchTime)
    Magnet_on()
    Up(catchTime)

def multiBounce(waitTime,liftTime = 3):
    #predeterminded number of seconds
    Magnet_off()
    # wait until it multi bounce
    Wait(waitTime)
    # get it
    Down(liftTime)
    Magnet_on()
    Up(liftTime)
    
def singleBounceLoop(loopTime, catchTime):
    Magnet_on()
    print("磁铁已开启，请在5秒内放上小球")
    time.sleep(5)

    machineStatus = "RUNNING"

    while loopTime > 0:
        loopTime -= 1
        singleBounce(catchTime)

    machineStatus = "IDLE"

def multiBounceLoop(loopTime, waitTime):
    global machineStatus

    Magnet_on()
    print("磁铁已开启，请在5秒内放上小球")
    time.sleep(5)

    machineStatus = "RUNNING"

    while loopTime > 0:
        loopTime -= 1
        multiBounce(waitTime)

    machineStatus = "IDLE"