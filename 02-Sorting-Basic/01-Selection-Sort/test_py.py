__author__ = 'CP6'

if __name__ == '__main__':
    alist = [1, 3, 2]
    alist[1], alist[2] = alist[2], alist[1]
    print(alist)
    print(alist[:-1])
