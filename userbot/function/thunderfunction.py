# Copyright (C) By @StarkGang And @ZeltraxRockz
# Powered By @Nemo_Projects
import random
import string


# String Finder
def stark_finder(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


