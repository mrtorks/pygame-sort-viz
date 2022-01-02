import pygame
from draw_i import DrawInformation
from g_window import draw
from bub_sort import bubble_sort
from insert_sort import insertion_sort
from list_gen import generate_starting_list
from h_sort import heap_sort
from s_sort import shell_sort
pygame.init()


def main():
    run = True
    sorting = False
    ascending = True

    sorting_algo = bubble_sort
    sorting_algo_name = "Bubble Sort"
    sorting_algo_gen = None
    clock = pygame.time.Clock()
    n = 60
    min_val = 0
    max_val = 350
    lst = generate_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(1000, 900, lst)

    while run:
        clock.tick(120)
        if sorting:
            try:
                next(sorting_algo_gen)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info, sorting_algo_name, ascending)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                lst = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                sorting_algo_gen = sorting_algo(draw_info, ascending)
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            elif event.key == pygame.K_d and not sorting:
                ascending = False
            elif event.key == pygame.K_i and not sorting:
                sorting_algo = insertion_sort
                sorting_algo_name = "Insertion Sort"
            elif event.key == pygame.K_b and not sorting:
                sorting_algo = bubble_sort
                sorting_algo_name = "Bubble Sort"
            elif event.key == pygame.K_h and not sorting:
                sorting_algo = heap_sort
                sorting_algo_name = "Heap Sort"
            elif event.key == pygame.K_s and not sorting:
                sorting_algo = shell_sort
                sorting_algo_name = "Shell Sort"

    pygame.quit()


if __name__ == "__main__":
    main()
