import re


def Main():
    line = "I think I understand regular expressions"

    matchResult = re.match('think',line,re.M|re.I) ## case  Insitive

    if matchResult:
        print("match found "+matchResult.group())
    else:
        print("No Match was found")


    searchResult = re.search("think",line,re.M|re.L)
    if searchResult:
        print("search found: "+searchResult.group())
    else:
        print('nothing found in search')

if __name__ == '__main__':
    Main()
