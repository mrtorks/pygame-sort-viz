from g_list import draw_list
from rs_check import rev_sort_check


def heapify_asc(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify_asc(arr, n, largest)

# The main function to sort an array of given size


def heapify_desc(arr, n, i):
    smallest = i  # Initialize smallest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # If left child is smaller than root
    if l < n and arr[l] < arr[smallest]:
        smallest = l

    # If right child is smaller than
    # smallest so far
    if r < n and arr[r] < arr[smallest]:
        smallest = r

    # If smallest is not root
    if smallest != i:
        (arr[i],
         arr[smallest]) = (arr[smallest],
                           arr[i])

        # Recursively heapify the affected
        # sub-tree
        heapify_desc(arr, n, smallest)





def heap_sort(draw_info, ascending=True):
    lst = draw_info.lst
    sorted_list = all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
    rev_sorted_list = rev_sort_check(lst)
    if(ascending and not sorted_list):
        # Build a maxheap.
        for i in range(int(len(lst)/2) - 1, -1, -1):
            heapify_asc(lst, len(lst), i)

        # One by one extract elements
        for i in range(len(lst)-1, 0, -1):
            lst[i], lst[0] = lst[0], lst[i]  # swap
            heapify_asc(lst, i, 0)
            draw_list(draw_info, {i - 1: draw_info.GREEN,
                                  i: draw_info.RED}, True)
            yield True

    elif(not ascending and not rev_sorted_list):
        for i in range(int(len(lst) / 2) - 1, -1, -1):
            heapify_desc(lst, len(lst), i)

    # One by one extract an element
    # from heap
        for i in range(len(lst)-1, -1, -1):

            # Move current root to end #
            lst[0], lst[i] = lst[i], lst[0]

            # call max heapify on the reduced heap
            heapify_desc(lst, i, 0)
            draw_list(draw_info, {i - 1: draw_info.GREEN,
                                  i: draw_info.RED}, True)
            yield True

    return lst
