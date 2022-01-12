import curses
import ncursesui.Elements
from ncursesui.Utility import init_colors, put

MIN_COLOR = 10
MAX_COLOR = 250

def main(stdscr):
    curses.curs_set(0)
    init_colors()
    height, _ = stdscr.getmaxyx()
    for i in range(MIN_COLOR, MAX_COLOR):
        put(stdscr, i % height, (i // height) * 4, f'#{i}-black {i}')
    stdscr.getch()
curses.wrapper(main)