# trust_pilot_scrapper

### Script that helps you to get a reviews from trustpilot.com

How to run script(macos). In terminal run :
```
git clone https://github.com/dont-4get-me-men/trust_pilot_scrapper
cd trust_pilot_scrapper
```
Create virtual enviroment. Version of python is 3.9.12
```
python -m venv env
source env/bin/activate
pip intsall -r requirements.txt
```

Change site that you want to inspect (site_link Line 39 main.py, format "facebook.com") and number of pages that you want to download(max_page line 38 main.py).

<img width="597" alt="image" src="https://user-images.githubusercontent.com/51093985/202701786-3faa80a6-bbe5-402c-9b9a-a93edd8f42e6.png">

Run in terminal.
```
python main.py
```

After you run this scipt in folder that you cloned will appear folder that contains downloaded html pages 1 ... max_page and file that contains csv file with columns = index,country,review,title,date,stars.

Example folder name : trust_pilot_pages_facebook.com.
Example csv file name: trust_pilot_facebook.com.csv

P.S. trust_pilot has rate limit, so if you want to download a lot of pages you should to uncomment time.sllep(4.5) at main.py download_all_pages function (line 22)
