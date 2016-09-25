#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import sys
import pprint


######################################################################
pp = pprint.PrettyPrinter(indent=4)

def analyze_fpath(fpath):
    """docstring for analyze_file"""
    # want to know the current path, filename, and filetype

    # get abspath 
    # TODO assert fname and maybe dirname
    #fname, fext = os.path.splitext(fpath)
    # split into components

    return (path,fname,check_extension(fext))


def check_extension(fext):
    """check to see if we know the extension type"""

    return fext_type


def make_mp3dir(path):
    """docstring for make_mp3dir"""

    return 


def convert(fpath):
    """Convert a file to mp3"""

    (path,fname,ext) = analyze_fpath(fpath)

    # use filename to rename a new file
    # use filetype to determine conversion action
    # use path to create a new mp3 dir in the path to hold the new files

    make_mp3dir(path)



    # TODO what to do about different types?
    # just flac and wav for now
    # output format always mp3

    ## copy to local and rename file

    ## convert to mp3

    ## rename to original with extension
    ## copy back to original directory



def main():

    convert('foo/bar.mp3')


######################################################################
if __name__ == '__main__':

    main()

