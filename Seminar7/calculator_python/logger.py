import os


def write_log(some_str):
    open('history.txt', 'a').write(some_str + '\n')
