import curses
from curses import wrapper


def main(stdscr):
    stdscr.clear()
    stdscr.reflesh()


wrapper(main)
