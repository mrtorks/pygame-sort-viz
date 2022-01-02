def rev_sort_check(lst) -> bool:
    temp_list = lst[:]
    temp_list.sort(reverse=True)
    if(temp_list == lst):
        return True
    return False
