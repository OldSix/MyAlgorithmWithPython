

from random import randint
import time


class SortTestHelper:
    def __init__(self, count, range_l, range_r, verbose=False):
        self.verbose = verbose
        self.count = count
        self.range_l = range_l
        self.range_r = range_r
        self.list = self.__generate_random_list()

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, *args):
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000   # milliseconds

        assert self.is_sorted()

        if self.verbose:
            print('elapsed time: %s ms' % self.msecs)
        else:
            print('elapsed time: %s s' % self.secs)

    def __generate_random_list(self):
        return [randint(self.range_l, self.range_r) for _ in range(0, self.count)]

    def is_sorted(self):
        for index, x in enumerate(self.list[:-1]):
            if self.list[index] > self.list[index+1]:
                return False
        return True

