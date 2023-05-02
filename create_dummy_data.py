import requests
from datetime import date
from datetime import datetime, timedelta
import json
import random
import re

url = 'http://localhost:3000/add'
today=date.today().strftime("%Y-%m-%d")
f = open("dummy_data.sh", "+w")

with open("source_data.json","r") as infile:
    lines  = infile.readlines()
    for line in lines:
        line = re.sub('2023-02-17', today, line).strip('\n')
        f.write(f'curl -X POST http://localhost:3000/add -H "Content-Type: application/json" -d \'{line}\'\n')
# for t in range(0, 288):
#     stringtime = newtime.strftime("%Y-%m-%dT%H:%M:%S")
#     t10 = random.uniform(20.234,21.456)
#     t9 = random.uniform(t10,30.456)
#     t8 = random.uniform(t9,40.456)
#     t7 = random.uniform(t8,50.456)
#     t6 = random.uniform(t7,60.456)
#     t5 = random.uniform(t6,70.456)
#     t4 = random.uniform(t5,70.456)
#     t3 = random.uniform(t4,70.456)
#     t2 = random.uniform(t3,70.456)
#     t1 = random.uniform(t2,70.456)
#
#     print(f"{t1} {t2} {t3} {t4} {t5} {t6} {t7} {t8} {t9} {t10}")
#
#     data = {"time":f"{stringtime}", "data": [
#             {"id": "t1", "time":f"{stringtime}", "temp": t1},
#             {"id": "t2", "time":f"{stringtime}", "temp": t2},
#             {"id": "t3", "time":f"{stringtime}", "temp": t3},
#             {"id": "t4", "time":f"{stringtime}", "temp": t4},
#             {"id": "t5", "time":f"{stringtime}", "temp": t5},
#             {"id": "t6", "time":f"{stringtime}", "temp": t6},
#             {"id": "t7", "time":f"{stringtime}", "temp": t7},
#             {"id": "t8", "time":f"{stringtime}", "temp": t8},
#             {"id": "t9", "time":f"{stringtime}", "temp": t9},
#            {"id": "t10", "time":f"{stringtime}", "temp": t10}]}
#
#     newtime = newtime + timedelta(0,300)
#
#     print(f'curl -X POST http://localhost:3000/add -H "Content-Type: application/json" -d \'{json.dumps(data)}\'')
#     f.write(f'curl -X POST http://localhost:3000/add -H "Content-Type: application/json" -d \'{json.dumps(data)}\'\n')

f.close()
    # x = requests.post(url, json=data)
    # print(x)