# pypi.org
# cowsay
# pip enable to instal packages
# pip instal - "pip install cowsay"
# if import is not working - "where python"
# change in settings.json (user) defult path to Python

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("Hello, " + sys.argv[1])