#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pprint


######################################################################
pp = pprint.PrettyPrinter(indent=4)


def convert(path,fname):
    """docstring for convert"""

    # split into directory and fname
    # TODO assert fname and maybe dirname

    # TODO what to do about different types?
    # just flac and wav for now
    # output format always mp3

    ## copy to local and rename file

    ## convert to mp3

    ## rename to original with extension
    ## copy back to original directory



# TODO need a function to split paths into path/fname



def main():

    pp.pprint("start")


######################################################################
if __name__ == '__main__':

    main()

