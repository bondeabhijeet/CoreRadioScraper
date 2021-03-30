import requests
from bs4 import BeautifulSoup
import time

def NamesOnThisPage(soup, TotalNoOfSongs):
    for source in soup.find_all('div', class_ = 'tcarusel-item-title'):
        name = source.a.text
        print(name)
        TotalNoOfSongs +=1
    PageNavigation = soup.find('div', class_ = 'navigation')
    
    if(PageNavigation.find_all('a')[-1].text == 'Next'):
        return(PageNavigation.find_all('a')[-1]['href'], TotalNoOfSongs)
        
    else:
        print("\n[ DONE ]\n")
        return("Finished", TotalNoOfSongs)

BaseURL = 'https://coreradio.ru/singles/page/337/'
NextURL = BaseURL

TotalNoOfSongs = 0
PagesScanned = 0

while(NextURL != 'Finished'):
    SourceCode = requests.get(NextURL).text
    PagesScanned += 1
    soup = BeautifulSoup(SourceCode, 'lxml')

    NextURL, TotalNoOfSongs = NamesOnThisPage(soup, TotalNoOfSongs)
    print("[ Sleeping 5 seconds ]", end = '\r')
    time.sleep(4)
    print("                      ")

print('[ TOTALSONGS:', TotalNoOfSongs," ]", "\n[ PAGESSCANNED:", PagesScanned, " ]")
