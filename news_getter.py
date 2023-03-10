#!/opt/homebrew/bin/python3
import subprocess, os, sys, pdfkit, urllib, datetime
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen

chrome_exe='/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome'
output_dir='out'
ft_url='https://www.ft.com/technology'

script_path=os.path.dirname(os.path.realpath(sys.argv[0]))

def getNewsDict():
    newsDict = {}

    html_doc = urlopen(ft_url).read().decode('utf-8')
    soup = BeautifulSoup(html_doc, 'html.parser')

    for link in soup.find_all('a', {'class': 'js-teaser-heading-link'}):
        # print(link)
        url = link.get('href')
        title = link.string
        if url is not None and title is not None:
            if "/content/" in url:
                fullURL = "https://12ft.io/api/proxy?ref=&q=" + urllib.parse.quote("https://www.ft.com" + url, safe='')
                item = {fullURL: title}
                newsDict.update(item)    
    return newsDict

def printToPDF(dict):
    if not os.path.exists(script_path + '/' + output_dir):
        os.makedirs(script_path + '/' + output_dir)

    for key in dict.keys():
        val = dict[key]
        # print("Title: ",val)
        # print("URL  : ",key)
        # print("")
        
        cmd = chrome_exe + " --headless --disable-gpu --print-to-pdf='" + script_path + '/' + output_dir + "/" + val + ".pdf' '" + key + "'"
        returned_value = subprocess.call(cmd, shell=True)

def syncToRM():
    current_date = datetime.date.today().strftime("%d-%m-%Y")
    rm2_folder = 'news_' + current_date
    subprocess.Popen(['rmapi','mkdir',rm2_folder])

    # loop, waiting for the new folder to appear
    while True:
        time.sleep(3)
        cmd = "rmapi ls | grep " + rm2_folder
        returned_value = subprocess.call(cmd, shell=True)
        # 1 = folder doesn't exist, sleep and try again
        # 0 = folder does exist, move to upload
        if returned_value==0:
            break

    os.chdir(script_path + '/' + output_dir)
    subprocess.Popen(['rmapi','mput',rm2_folder])

# todo
def removeOldNews():
    # get list of news folders
    # rmapi ls | grep news | awk {'print $2'}

    # get todays date and folder, to exclude from deletion
    current_date = datetime.date.today().strftime("%d-%m-%Y")
    rm2_folder = 'news_' + current_date

    # interate list of folders
        # get list of files in folder
        # call delete on file
        # call delete on folder


newsDict=getNewsDict()
printToPDF(newsDict)
syncToRM()
