from g_list import draw_list


def quick_sort(draw_info, ascending=True):
    lst = draw_info.lst

    yield from q_sort(draw_info, lst, ascending)


def q_sort(draw_info, arr, ascending):
    elements = len(arr)

    # Base case
    if elements < 2:
        return arr

    current_position = 0  # Position of the partitioning element

    for i in range(1, elements):  # Partitioning loop
        if(ascending):
            if arr[i] <= arr[0]:
                current_position += 1
                arr[i], arr[current_position] = arr[current_position], arr[i]
                draw_list(draw_info, {i - 1: draw_info.GREEN,
                                      i: draw_info.RED}, True)
                yield arr
        elif(not ascending):
            if arr[i] >= arr[0]:
                current_position += 1
                arr[i], arr[current_position] = arr[current_position], arr[i]
                draw_list(draw_info, {i - 1: draw_info.GREEN,
                                      i: draw_info.RED}, True)
                yield arr
    # Brings pivot to it's appropriate position
    arr[0], arr[current_position] = arr[current_position], arr[0]
    draw_list(draw_info, {i - 1: draw_info.GREEN,
                          i: draw_info.RED}, True)
    yield arr
    # Sorts the elements to the left of pivot
    left = yield from q_sort(draw_info, arr[0:current_position], ascending)
    # sorts the elements to the right of pivot
    right = yield from q_sort(draw_info, arr[current_position+1:elements], ascending)

    arr = left + [arr[current_position]] + \
        right  # Merging everything together

    draw_list(draw_info, {i - 1: draw_info.GREEN,
                          i: draw_info.RED}, True)
    yield arr
    print(arr)
    return arr
