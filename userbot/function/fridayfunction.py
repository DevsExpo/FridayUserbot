# Copyright (C) By @Hackintush
# Powered By @Hackintush
import random
import string
import os
import re
import shlex
import asyncio
from typing import Tuple, List, Optional

# String Finder
def stark_finder(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


# Id Generator
def id_generator(size=64, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))

