import cProfile
import re


def display_stats():
    benchmark = cProfile.run('re.compile("sorting_algo(draw_info, ascending)")')
    return benchmark