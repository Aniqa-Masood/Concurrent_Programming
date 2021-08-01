import asyncio
import aiohttp
import os
import time
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

textfile = open("C:\\Users\\Aniqa Masood\\Downloads\Gyu Test\GYU Questions\concurrent\\problematic_links.txt", "w")
df = pd.read_excel('C:\\Users\\Aniqa Masood\\Downloads\Gyu Test\GYU Questions\concurrent\\TEST_4.xlsx', usecols='BH')

start = time.time()

def get_tasks(session):
    tasks = []
    for txt in df.iloc[1:11]["상품상세설명\n[필수]"]:
        soup = BeautifulSoup(txt, 'html.parser')
        for d in soup.select('div#GYU'):
            for i in d.select('img'):
                url = i['src']
                tasks.append(asyncio.create_task(session.get(url, ssl=False)))
    return tasks

async def get_symbols():
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        responses = await asyncio.gather(*tasks)
        for response in responses:
            print(response.url,response.status)
            if response.status != 200:
                textfile.write(str(response.url)+'\n')
            

asyncio.run(get_symbols())

end = time.time()
total_time = end - start
print("It took {} seconds".format(total_time))
print('You did it!')

textfile.close()