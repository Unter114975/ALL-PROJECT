import os
import platform
from ConnectDB import *

class Ping():
    def __init__(self):
        self.Host = ''
        self.lines = []
        self.STATUS_HOST = ''
        self.SPEED_AVG = ''
        self.SPEED_MAX = ''
        self.SPEED_MIN = ''
        self.IP_HOST = ''


    def testPing(self, Host):
        self.Host = Host
        ping_com = "ping -n 1 "
        comm = ping_com + Host
        response = os.popen(comm)
        LinesPing = response.readlines()
        status = 0
        for line in LinesPing:
            if 'TTL' in line:
               status = 1
        if status:
            return True
        else:
            return False


    def listPing(self):
        ping_com = "ping -n 4 "
        comm = ping_com + self.Host
        response = os.popen(comm)
        LinesPing = response.readlines()
        c = 0
        for line in LinesPing:
            self.lines.append(c)
            self.lines.append(line.encode("ascii", errors="ignore"))
            c += 1
        self.parsingPing()
        print(self.lines)



    def parsingPing(self):
        if len(self.lines[3]) > 30:
            List = self.lines[3]
            x = len(List)
            L = List[10 - 1:10]
            print(L)
            if L == 'y'.encode("ascii", errors="ignore"):
                print(L,"ok")
            #print(List)
            # for i in range(1, x):
            #     print(List[i-1:i])
            #     if List[i-1:i] == ' ':
            #         print(i,"ok")




            #print(List[x-1:x:1])
            # for i in List(0):
            #     print(List)
            #     if i == '[':
            #         a = i
            #         print(a)
            #     elif i == ']':
            #         b = i
            #         print(b)
            #print(List[a:b])


# IP_HOST = '217.25.891.226'
# #'docs-python.ru'
# ping = Ping()
#
# print(ping.testPing(IP_HOST))
# if ping.testPing(IP_HOST):
#     ping.listPing()
#     #ConnetDB.PinginsertDB(IP_HOST)
# else:
#     print("nou ping")
#     #NowPinginsertDB('')

# oc = platform.system()
# if (oc == "Windows"):
#     ping_com = "ping -n 1 "
# else:
#     ping_com = "ping -c 1 "
#
#
comm = ping_com + 'линуксблог.рф'
response = os.popen(comm)
data = response.readlines()

for line in data:
     print(line.encode("ascii", errors="ignore"))
     if 'TTL' in line:
          print( "--> Ping Ok")


