import threading, time
from ConnectDB import *
from PingConnect import *

class Error(Exception):
    pass

class ConnectError(Exception):
    pass

class SelectError(Error):
    pass

#try:
def programm():
    conn = ConnetDB()
    ping = Ping()
    IP_HOST = '217.25.89.226'
    print(ping.testPing(IP_HOST))

    if ping.testPing(IP_HOST):
        conn.PinginsertDB(IP_HOST)
    else:
        conn.NowPinginsertDB(IP_HOST)
    conn.CloseConnect()

def test():
    print("ok")
timerStart = threading.Timer(10.0, test())
timerStart.start()
