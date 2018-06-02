import argparse

def fib(n):
    a,b =0,1
    for i in range(n):
        a,b=b,a+b
    return a


def Main():
    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v","--verbose",action="store_true")
    group.add_argument("-q","--quite",action="store_true")
    parser.add_argument("num",help="the fibonacci number you want calculate",type=int)
    parser.add_argument("-o","--output",help="output result to a file",action="store_true")
    args = parser.parse_args()

    results = fib(args.num)## accepting inputs

    if args.verbose:
        print("The "+str(args.num)+"the fib number is "+str(results))
    elif args.quite:
        print(results)
    else:
        print("Fib("+str(args.num)+") the fib number is "+str(results))

    if args.output:
        with open("fibonacci.txt","a") as f:
            f.write(str(results)+'\n')


if __name__ == '__main__':
    Main()
