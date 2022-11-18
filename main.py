from functions import *
from consts import *
import pandas as pd
import time
import os
import warnings

warnings.filterwarnings('ignore')

def download_all_pages(link:str
                  ,max_page: int
                  ,folder: str)->set:
    
    cant_read = set()
    for i in range(1,max_page+1):
        b = download_page(link.format(i)
                     ,page_number=i
                     ,folder=folder
                     ,headers=header)
        if b:
            cant_read.add(b)
        #time.sleep(4.5)
    return cant_read

def data_to_df(path_format: str
              ,max_page:int
              ,cant_read:set = set()):
    
    df = pd.DataFrame(columns= ['country','review','title','date','stars'])
    for i in range(1,max_page+1):
        if not(i in cant_read): #if we read file correctly
            dicti = get_data_from_page(path_format.format(i))
            #print(dicti[0:2])
            df = pd.concat([df,pd.DataFrame(dicti)],axis = 0,ignore_index=True)
    return df

if __name__ == "__main__":
    max_page = 5
    site_link = 'facebook.com'
    link = "https://www.trustpilot.com/review/{}".format(site_link)+"?page={}"
    folder = f'trust_pilot_pages_{site_link}'
    if not(os.path.exists(folder)):
        os.mkdir(folder)
    cant_read = download_all_pages(link,max_page,folder)
    path_format =  folder + '/page{}.html'

    df = data_to_df(path_format,max_page,cant_read)
    #print(df.head())
    df.to_csv(f'trust_pilot_{site_link}.csv')