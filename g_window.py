import pygame
from g_list import draw_list
from benchmark import display_stats

pygame.init()


def draw(draw_info, algo_name, ascending):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    title = draw_info.FONT.render(
        f"Sorting Algorithm: {algo_name} - Sorting Order: {'Ascending' if ascending else 'Descending'}", 1, draw_info.GREEN)
    draw_info.window.blit(
        title, (draw_info.width/2 - title.get_width()/2, 5))

    controls = draw_info.FONT.render(
        "R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending ", 1, draw_info.WHITE)
    draw_info.window.blit(
        controls, (draw_info.width/2 - controls.get_width()/2, 35))

    sorting = draw_info.FONT.render(
        "I - Insertion Sort | B - Bubble Sort | H - Heap Sort | S - Shell Sort", 1, draw_info.BLACK)
    draw_info.window.blit(
        sorting, (draw_info.width/2 - sorting.get_width()/2, 65))

    #benchmark = draw_info.FONT.render(
    #    f"{display_stats()}", 1, draw_info.BLACK)
    #draw_info.window.blit(
    #    benchmark, (draw_info.width/2 - sorting.get_width()/2, 90))

    draw_list(draw_info)
    pygame.display.update()
