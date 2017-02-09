from selection_sort import selection_sort
from sort_test_helper import SortTestHelper

count = 1000

if __name__ == '__main__':
    st = SortTestHelper(count, 0, count)

    # 计算运行时间方法一
    with st as t:
        selection_sort(st.list)

    with st as t:
        st.list.sort()

    # 计算运行时间方法二
    # from time import clock
    #
    # start = clock()
    # selection_sort(tlist)
    # finish = clock()
    # print("{:<20}{:10.6} s".format(selection_sort.__name__ + ":", finish - start))
    #
    # start = clock()
    # tlist.sort()
    # finish = clock()
    # print("{:<20}{:10.6} s".format("built_in sort" + ":", finish - start))


