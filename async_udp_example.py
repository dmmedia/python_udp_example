#/usr/bin/python36

import random
import asyncio
import socket
import signal

# Graceful stop of all operations on SIGINT
class StopException(BaseException): pass

def stop(signal, frame):
    raise StopException

signal.signal(signal.SIGINT, stop)

# Generate random number for delay and convert it to string to send as a message
async def generate_random_data():
    randomNumber = random.random()
    randomString = str(randomNumber)
    return randomNumber, randomString;

# Send random numbers as string to local port 11234 with the same random delay
async def udp_random_sender():
    sendto_address = ('localhost', 11234)
    send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        randomNumber, randomString = await generate_random_data()
        send_sock.sendto(randomString.encode(), sendto_address)
        await asyncio.sleep(randomNumber)

# receive strings on port 11235 and print them out
class UdpReceiverProtocol:
    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        message = data.decode()
        print(message)

loop = asyncio.get_event_loop()

# A protocol instance will serve all incoming datagrams
listener = loop.create_datagram_endpoint(
    UdpReceiverProtocol, local_addr=('127.0.0.1', 11235))
transport, protocol = loop.run_until_complete(listener)

try:
    # Start both sender and receiver
    loop.run_until_complete(udp_random_sender())

    # Run forever or until SIGINT
    loop.run_forever()

except StopException:
    pass

transport.close()
loop.close()
