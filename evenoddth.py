import threading

odd_num = threading.Event()
even_num = threading.Event()


def printEven(n):
    for i in range(0, n, 2):
        print('Core 1:',i)
        odd_num.set()
        even_num.clear()
        even_num.wait()

def printOdd(n):
    odd_num.wait()
    for i in range(1, n, 2):
        print('Core 2:',i)
        even_num.set()
        odd_num.clear()
        odd_num.wait()

if __name__ == "__main__":
    n = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    t1 = threading.Thread(target=printEven, args=(n,))
    t2 = threading.Thread(target=printOdd, args=(n,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()