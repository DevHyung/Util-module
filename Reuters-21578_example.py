__email__ = "khuphj@gmail.com"
'''
File        : Reuters-21578_exmaple.py
Description : Reuters-21578 data set Print using by above Python3.6.x version 
'''
from typing import TextIO
from bs4 import BeautifulSoup
import re
# Category files
category_files = {
    'to_': ('Topics', 'all-topics-strings.lc.txt'),
    'pl_': ('Places', 'all-places-strings.lc.txt'),
    'pe_': ('People', 'all-people-strings.lc.txt'),
    'or_': ('Organizations', 'all-orgs-strings.lc.txt'),
    'ex_': ('Exchanges', 'all-exchanges-strings.lc.txt')
}

def get_article_by_bs4() -> None:
    """
    get reuters aritcle example code
    :return: None because example code
    """
    dataDir = "YOUR_FILE_DIRECTORY" # If you are in the same directory, you can use "./"
    sgmlFileFormat = dataDir + "reut2-{}.sgm"

    for fileIdx in range(0, 2):  # 22 last
        # Get file IO stream
        f: TextIO = open(sgmlFileFormat.format(str(fileIdx).zfill(3)), 'r')
        content: str = f.read()
        f.close()

        # Parsing
        bs = BeautifulSoup(content, 'lxml')
        reuters: List[bs4.element.Tag]  = bs.find_all('reuters')
        for article in reuters:
            newId: str = article['newid']
            oldId: str = article['oldid']
            textTag = article.find('text')
            try:
                title: str = textTag.find('title').get_text().strip()
            except AttributeError: # no title content
                title: str = ''
            print("NEWID : {}, OLDID : {}, TITLE : {} ".format(newId,oldId,title))

def get_article_by_regex() -> None:
    '''
    It is the same function as above, except that it is just writing Bs module -> Regexs.
    :return:
    '''
    lines: list[str] = "sgm 파일 전체 라인을 읽어서"
    for line in lines: # 전체 iteration 돌면서
        value = _strip_tags(line)
        # 후처리
    # 필요한거 반환
    pass

def _strip_tags(text)-> str:
    return re.sub('<[^<]+?>', '', text).strip()

if __name__ == "__main__":
    get_article_by_bs4()

