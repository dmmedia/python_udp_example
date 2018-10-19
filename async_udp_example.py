#/usr/bin/python36

import random
import asyncio
import socket
import signal

exitFlag = False

def stop(signal, frame):
    print("Gracefully exiting")
    global exitFlag
    exitFlag = True

async def generate_random_data():
    randomNumber = random.random()
    randomString = str(randomNumber)
    return randomNumber, randomString;
    
async def udp_random_sender():
    sendto_address = ('localhost', 11234)
    send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    global exitFlag
    while exitFlag == False:
        randomNumber, randomString = await generate_random_data()
        send_sock.sendto(randomString.encode(), sendto_address)
        print("Sending %s" % (randomString))
        await asyncio.sleep(randomNumber)
    send.sock.close()

async def udp_string_receiver():
    bind_adress = ('localhost', 11235)
    listen_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    listen_sock.setblocking(0)
    listen_sock.bind(bind_address)
    listen_sock.listen(1)
    global exitFlag
    buffer = ""
    while exitFlag == False:
        readable, writable, exceptional = select.select([ listen_sock ], [], [ listen_sock ])
        for s in readable:
            data = s.recv(10)
            if data:
                buffer = buffer + data
            else:
                print("Received %s" % buffer.decode())
                buffer = ""
        for s in exceptional:
            if s is listen_sock:
                listen_sock.close()
                listen_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                listen_sock.setblocking(0)
                listen_sock.bind(bind_address)
                listen_sock.listen(1)
                buffer = ""
    listen_sock.close()

signal.signal(signal.SIGINT, stop)

loop = asyncio.get_event_loop()
loop.run_until_complete(udp_random_sender())
loop.close()
