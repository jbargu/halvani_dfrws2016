# -*- coding: utf-8 -*-

import os
import re

from collections import Counter

print "Read WordDict.py"

def preprocess(s):
    regex = re.compile(r"\d+")
    s_new = regex.sub(' ', s)
    regex = re.compile(r"\s+")
    s_new = regex.sub(' ', s_new)

    return s_new

def file_contents(aFileName):
    with open(aFileName) as inFile:
        listsOfWords = preprocess(inFile.read())
    return listsOfWords

def dictFromFile(aFileName):
    with open(aFileName) as inFile:
        listsOfWords = inFile.read().split()
    return Counter(listsOfWords)


def getListListPANAndFoldersPAN(aPath):
    aListListPAN = []
    foldersPAN = []

    for d in os.listdir(aPath):
        aListPAN = []
        if os.path.isfile(aPath + "/" + d):
            continue
        foldersPAN.append(d)
        for f in os.listdir(aPath + "/" + d + "/"):
            aListPAN.append(aPath + "/" + d + "/" + f)
        aListListPAN.append(sorted(aListPAN))
    foldersPAN, aListListPAN = zip(*sorted(zip(foldersPAN, aListListPAN)))

    return aListListPAN, foldersPAN
