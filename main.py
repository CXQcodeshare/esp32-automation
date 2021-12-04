import socket
import gc
do_connect()
gc.collect()
#防止内存boom

def web_page():
    #判断机器运行状态
    if magnet.value() == 1:
        magnet_state = 'OFF'
    else:
        magnet_state = 'ON'
    if rotate_1.value() == 1 and rotate_2.value() == 0:
        motor_state = 'UP'
    elif rotate_1.value() == 0 and rotate_2.value() == 1:
        motor_state = 'DOWN'
    else:
        motor_state = 'OFF'

    # html code ...
    html = """<html><head> 
    <title>ESP 32 自动化实验控制面板 verson1.0</title> 
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:,"> 
    <style>
    html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
    h1{color: #0F3376; padding: 2vh;}
    p{font-size: 1.5rem;}
    .button{display: inline-block; background-color: #e7bd3b; border: none; 
    border-radius: 4px; color: white; padding: 16px 30px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
    .button2{background-color: #4286f4;}
    .button3{background-color: #e73b3b;}
    .button4{background-color: #48f442a9;}
    .button5{background-color: #8b3be7;}
    .button6{background-color: #ffa602;}
    </style></head>
    <body> <h1>ESP 32 automate control pannel verson1.0</h1> 
    <p>magnet_state state: <strong>""" + magnet_state + """</strong></p>
    <p><a href="/?magnet=off"><button class="button">magnet OFF</button></a></p>
    <p><a href="/?magnet=on"><button class="button button2">magnet   ON</button></a></p>
    <p>motor_state: <strong>""" + motor_state + """</strong></p>
    <p><a href="/?motor=up10"><button class="button button3">motor  UP-1s</button></a></p>
    <p><a href="/?motor=down10"><button class="button button4">motor DOWN-1s</button></a></p>
    <p><a href="/?motor=up01"><button class="button button3">motor UP-0.1s</button></a></p>
    <p><a href="/?motor=down01"><button class="button button4">motor DOWN-0.1s</button></a></p>
    <p><a href="/?singleBounceLoop"><button class="button button5">singleBounceLoop</button></a></p>
    <p><a href="/?multiBounceLoop"><button class="button button6">multiBounceLoop</button></a></p>
    <p>duty: <strong>""" + str(duty) + """</strong></p>
    <p><a href="/?duty-50"><button class="button button5">DUTY -50</button></a></p>
    <p><a href="/?duty+50"><button class="button button6">DUTY +50</button></a></p>
</body></html>"""
    return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('# your cilent IP adress printed #', 80))
#绑定端口

s.listen(5)

while True:
    if gc.mem_free() < 102000:
        gc.collect()
    conn, addr = s.accept()
    print('Connection: %s' % str(addr))
    req = conn.recv(1024)
    req = str(req)
    print('Connect = %s' % req)
    magnet_on0 = req.find('/?magnet=on')
    magnet_off0 = req.find('/?magnet=off')
    up10 = req.find('/?motor=up10')
    up01 = req.find('/?motor=up01')
    down10 = req.find('/?motor=down10')    
    down01 = req.find('/?motor=down01')    
    duty01 = req.find('/?duty-50')    
    duty10 = req.find('/?duty+50')    

    singleBounceLoop0 = req.find('/?singleBounceLoop')
    multiBounceLoop0 = req.find('/?multiBounceLoop')
    
    #调节占空比
    if  duty01 == 6:
        duty = duty - 50
        print("duty - 50")

    if  duty10 == 6:
        duty = duty + 50
        print("duty + 50")

    #触发function
    if singleBounceLoop0 == 6:
        print('singleBounceLoop')
        singleBounceLoop(3,10)

    if multiBounceLoop0 == 6:
        print('multiBounceLoop')
        multiBounceLoop(5,3)
    
    #调节电磁铁开关
    if magnet_off0 == 6:
        print('magnet OFF')
        Magnet_off()
    else:
        print('magnet ON')
        Magnet_on()

    #上升:up/down10粗调节;up/down01微调节        
    if up10 == 6:
        print('motor UP 1s')
        Up(1)
    elif up01 == 6:
        print('motor UP 0.1s')
        Up(0.1)
    elif down10 == 6:
        print('motor DOWN 1s')
        Down(1)
    elif down01 == 6:
        print('motor DOWN 0.1s')
        Down(0.1)
    else:
        print('motor OFF')
    
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()




