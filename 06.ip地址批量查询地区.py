import json
import random
import pandas as pd
import time

import requests

'''
可用以下接口查询
http://whois.pconline.com.cn/ipJson.jsp?json=true&ip=
http://opendata.baidu.com/api.php?query='+str(ip)+'&co=&resource_id=6006&ie=utf8&oe=utf-8&format=json
http://ip.ws.126.net/ipquery?ip=
http://ip-api.com/json/14.16.139.216
'''


def generate_random_number(start: int, end: int) -> int:
    cryptogen = random.SystemRandom()
    random_number = cryptogen.randint(start, end)
    return random_number


def get_ip():
    ips = pd.read_csv('C:/Users/Administrator/Desktop/ipcode.csv', encoding='utf-8', header=None)
    user_ids = pd.Series(ips.iloc[:, 0])
    ip_list = pd.Series(ips.iloc[:, 1])
    a = []
    count = 0
    time_count = 0
    for i in ip_list:
        try:
            url = 'http://opendata.baidu.com/api.php?query=' + str(
                i) + '&co=&resource_id=6006&ie=utf8&oe=utf-8&format=json'
            r = requests.get(url)
            uid = user_ids[count]
            count += 1
            k = json.loads(r.text)
            ip = k['data'][0]['origip']
            country = k['data'][0]['location']
            all = str(uid) + ',' + ip + ',' + country
            a.append(all)
            sleep_time = 0.1 * generate_random_number(1, 5)
            print("sleep_time: ", sleep_time)
            time_count += sleep_time
            time.sleep(sleep_time)
        except Exception as e:
            print(e)
            return
    print(time_count, "  --time_count second")
    k = pd.DataFrame(a)
    name = 'C:/Users/Administrator/Desktop/iplocation.csv'
    k.to_csv(name, encoding='ansi', header=None, index=False)


if __name__ == '__main__':
    get_ip()
