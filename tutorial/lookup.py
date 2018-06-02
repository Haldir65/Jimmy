import argparse,re

def Main():
    parse = argparse.ArgumentParser()
    parse.add_argument("word",help="specify the word you want to search ")
    parse.add_argument("fname",help="specify file to search")

    args = parse.parse_args()

    with open(args.fname) as searchFile:
        lineNum = 0
        for line in searchFile.readlines():
            line = line.strip("\r\n")
            lineNum+=1
            searchResult = re.search(args.word,line,re.M|re.I)
            if searchResult:
                print(str(lineNum)+' : '+line)
            # else:
            #     print(str(line))

if __name__ == '__main__':
    Main()
