import requests
from bs4 import BeautifulSoup
import time

#-----------------------------------------------FUNCTION----------------------------------------------------------------------

def NamesOnThisPage(soup, TotalNoOfSongs):
    SongsOnCurrentPage = ''
    
    for SongTile in soup.find_all('li', class_ = 'tcarusel-item main-news'):
        name = SongTile.find('div', class_ = 'tcarusel-item-title').text.strip()
        SongsOnCurrentPage += name + '\n'
        TotalNoOfSongs +=1
    print(SongsOnCurrentPage, end = '')

    with open ('ScrappedData.txt', 'a') as f:
        f.write(SongsOnCurrentPage)

    PageNavigation = soup.find('div', class_ = 'navigation')
    
    if(PageNavigation.find_all('a')[-1].text == 'Next'):
            print("[ Sleeping 2 seconds ]", end = '\r')
            time.sleep(2)
            print("                      ", end = '\r')
            return(PageNavigation.find_all('a')[-1]['href'], TotalNoOfSongs)
        
    else:
        print("\n[ DONE ]\n")
        return("Finished", TotalNoOfSongs)

BaseURL = 'https://coreradio.ru/singles/page/341/'
NextURL = BaseURL

TotalNoOfSongs = 0
PagesScanned = 0

while(NextURL != 'Finished'):
    SourceCode = requests.get(NextURL).text
    PagesScanned += 1
    soup = BeautifulSoup(SourceCode, 'lxml')

    NextURL, TotalNoOfSongs = NamesOnThisPage(soup, TotalNoOfSongs)

print('[ TOTALSONGS:', TotalNoOfSongs," ]", "\n[ PAGESSCANNED:", PagesScanned, " ]")

with open('ScrappedData.txt', 'a') as f:
    f.write(f'[ TOTALSONGS: {TotalNoOfSongs} ]\n[ PAGESSCANNED: {PagesScanned} ]')

#-------------------------------------------------------------------------------------------------------------------------------
print("[ PRESS ENTER TO CONTINUE ]")
input()
