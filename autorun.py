import time

#现阶段没什么用，不过写着，之后好调试
machineStatus = "IDLE"

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
    global machineStatus

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
'''
# built-in func, its a prototype here
def Up(moveTime):
    print("向上升磁铁 " + str(moveTime) + " 秒")
    Wait(moveTime)
def Down(moveTime):
    print("向下降磁铁 " + str(moveTime) + " 秒")
    Wait(moveTime)
def Magnet_on():
    print("开启磁铁")
def Magnet_off():
    print("关闭磁铁")
def Brake(reason = "DEFAULT"):
    global machineStatus
    #should set the driver speed to 0 and magnet off
    if reason != "DEFAULT":
        machineStatus = "ABORTED"
        print("机器由于" + str(reason) + "终止运行")
        exit()

def Wait(someTime):
    print("等待 " + str(someTime) + " 秒")
    try:
        time.sleep(someTime)
    except KeyboardInterrupt:
        Brake("Keyboard Interrupt")


if __name__ == "__main__":
    loopTimes = 3
    #second
    catchTime = 0.2
    waitTime = 1
    multiBounceLoop(loopTimes, waitTime)
    singleBounceLoop(loopTimes, catchTime)
'''
    