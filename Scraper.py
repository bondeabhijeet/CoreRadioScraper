import requests
from bs4 import BeautifulSoup
import time

def NamesOnThisPage(soup, TotalNoOfSongs):
    SongsOnCurrentPage = ''
    for source in soup.find_all('div', class_ = 'tcarusel-item-title'):
        name = source.a.text
        #print(name)
        SongsOnCurrentPage += name + '\n'
        TotalNoOfSongs +=1
    print(SongsOnCurrentPage, end = '')

    with open ('ScrappedData.txt', 'a') as f:
        f.write(SongsOnCurrentPage)

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
    print("                      ", end = '\r')

print('[ TOTALSONGS:', TotalNoOfSongs," ]", "\n[ PAGESSCANNED:", PagesScanned, " ]")

with open('ScrappedData.txt', 'a') as f:
    f.write(f'[ TOTALSONGS: {TotalNoOfSongs} ]\n[ PAGESSCANNED: {PagesScanned} ]')

#-------------------------------------------------------------------------------------------------------------------------------------
print("[ PRESS ENTER TO CONTINUE ]")
input()
