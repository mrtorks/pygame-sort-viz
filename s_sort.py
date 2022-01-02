from g_list import draw_list
from rs_check import rev_sort_check


# Shell sort in python


def shell_sort(draw_info, ascending=True):
    lst = draw_info.lst
    n = draw_info.list_size
    sorted_list = all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
    rev_sorted_list = rev_sort_check(lst)

    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        if(ascending and not sorted_list):
            for i in range(interval, n):
                temp = lst[i]
                j = i
                while j >= interval and lst[j - interval] > temp:
                    lst[j] = lst[j - interval]
                    j -= interval

                lst[j] = temp
                draw_list(draw_info, {i - 1: draw_info.GREEN,
                                      i: draw_info.RED}, True)
                yield True
        elif(not ascending and not rev_sorted_list):
            for i in range(interval, n):
                temp = lst[i]
                j = i
                while j >= interval and lst[j - interval] < temp:
                    lst[j] = lst[j - interval]
                    j -= interval

                lst[j] = temp
                draw_list(draw_info, {i - 1: draw_info.GREEN,
                                      i: draw_info.RED}, True)
                yield True
        interval //= 2
    return lst
