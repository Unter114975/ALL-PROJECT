import psycopg2
from PingConnect import *

class ConnetDB():
    def __init__(self):
         self.con = psycopg2.connect(database="postgres",
            user="postgres",
            password="admin",
            host="127.0.0.1",
            port="5432")



    def selectDB(self, id_user):
        cur = self.con.cursor()
        cur.execute(f'SELECT "NAME_HOST" FROM public."INPUT_INF_HOST" where "ID_USER" = {id_user}')
        rows = cur.fetchall()
        for row in rows:
            print(row[0])



    def PinginsertDB(self,IP_HOST):
        IP_HOST = (" '" + IP_HOST + "' ")
        print(IP_HOST)
        cur = self.con.cursor()
        cur.execute(f'INSERT INTO public."INPUT_STATUS_HOST"("ID_HOST", "STATUS_HOST", "SPEED_AVG","SPEED_MAX", "SPEED_MIN", "IP_HOST", "INT_TIME") VALUES (1, 1, 40, 41, 42, {IP_HOST},NOW());')
        print("PinginsertDB OK")
        self.con.commit()


    def NowPinginsertDB(self,IP_HOST):
        IP_HOST = (" '" + IP_HOST + "' ")
        cur = self.con.cursor()
        cur.execute(f'INSERT INTO public."INPUT_STATUS_HOST"("ID_HOST", "STATUS_HOST", "SPEED_AVG","SPEED_MAX", "SPEED_MIN", "IP_HOST", "INT_TIME") VALUES (1, 0, 0, 0, 0, {IP_HOST},NOW())')
        print("NowPinginsertDB OK")
        self.con.commit()


    def CloseConnect(self):
        self.con.close()


#IP_HOST = "'217.25.89.226'"
#Con=ConnetDB()
#Con.NowPinginsertDB(IP_HOST)
#Con.PinginsertDB(IP_HOST)
#self.con.close()