def doFormat(num):
    resource = "http://www.baidu.com/%s" % num
    print(resource)

if __name__ == "__main__":
    for n in range(100):
        doFormat(n)
    