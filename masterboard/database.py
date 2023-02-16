import datetime
import sqlite3
import json
import pickle
import pytz
import requests

# COORDINATOR_IP = "127.0.0.1:8000"
COORDINATOR_IP = "10.0.0.41:8000"


local_tz = pytz.timezone("Australia/Sydney")

class Masterboard:
    def __init__(self):
        self.db_path = "masterboard.db"
        self.init_database_tables()

    def init_database_tables(self):
        conn = sqlite3.connect(self.db_path, detect_types=sqlite3.PARSE_DECLTYPES)
        conn.row_factory = sqlite3.Row
        c = conn.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS masterboard
                     (ip_id INTEGER PRIMARY KEY,
                     ip text DEFAULT NULL,
                     rink_id text"")''')

        conn.commit()


    def setup(self, js):
        print(js)
        con = sqlite3.connect(self.db_path, detect_types=sqlite3.PARSE_DECLTYPES)
        con.row_factory = sqlite3.Row
        cursor = con.cursor()

        sql = "DELETE FROM masterboard;"
        cursor.execute(sql)

        sql = "INSERT INTO masterboard (ip, rink_id) VALUES(?, ?);"
        game_id = cursor.executemany(sql, js)

        con.commit()


    def encode_if_required(self, str_val):
        try:
            return str_val.encode()
        except Exception:
            return str_val

    def get_masterboard(self):
        con = sqlite3.connect(self.db_path, detect_types=sqlite3.PARSE_DECLTYPES)
        con.row_factory = sqlite3.Row
        cursor = con.cursor()

        summed = []
        ips = cursor.execute('''SELECT * FROM masterboard''').fetchall()
        for ip in ips:
            print('IPS', ip['ip'])
            try:
                response = requests.get('http://'+ip['ip']+'/get_game')
            except:
                continue
            data = json.loads(response.content)
            print(data)
            summed.append(data[0])

        # print {k: x.get(k, 0) + y.get(k, 0) for k in set(summed) & set(y)}

        return json.dumps(data, indent=4, sort_keys=True)


    def write_coordinator_score(self, js):
        response = requests.post('http://'+COORDINATOR_IP+'/games/add_score', json = js)
        print(response)
        return response.status_code


    def write_coordinator_ends(self, js):
        response = requests.post('http://'+COORDINATOR_IP+'/games/add_ends', json = js)
        print(response)
        return response.status_code

