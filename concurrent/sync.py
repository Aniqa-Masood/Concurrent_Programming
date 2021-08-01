import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import time

textfile = open("C:\\Users\\Aniqa Masood\\Downloads\Gyu Test\GYU Questions\concurrent\\problematic_links.txt", "w")
df = pd.read_excel('C:\\Users\\Aniqa Masood\\Downloads\Gyu Test\GYU Questions\concurrent\\TEST_4.xlsx', usecols='BH')

start = time.time()

def get_status_code(url):
    r = requests.get(url)
    sta_code = r.status_code
    print(sta_code)
    if sta_code == 200:
        textfile.write(str(url)+'\n')


for txt in df.iloc[1:11]["상품상세설명\n[필수]"]:
    soup = BeautifulSoup(txt, 'html.parser')
    for d in soup.select('div#GYU'):
        for i in d.select('img'):
            uurl = i['src']
            print(uurl)
            get_status_code(uurl)
            

textfile.close()

end = time.time()
total_time = end - start
print("It took {} seconds".format(total_time))
print('You did it!')