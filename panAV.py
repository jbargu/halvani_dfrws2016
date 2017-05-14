# -*- coding: utf-8 -*-

import getopt
import random
import sys
import time
import numpy as np

from evaluator import writeNameAndScore, normProbs
from Spatium import featureSelection, mergeToProfile, l1Distance
from WordDict import dictFromFile, getListListPANAndFoldersPAN, file_contents

from features_categories import *
from collections import Counter

print "Read panAV.py"

compNo = 5.0  # compare X times
randCompare = 3  # compare with Y random candidates
wLen = 200

random.seed(1811)


def processAll(aListOfFile):
    wLists = []
    for aFile in aListOfFile:
        texts = []
        for aText in aFile:
            texts.append(file_contents(aText))
        wLists.append(texts)
    return wLists


def processSamples(aListOfSamples):
    wLists = []
    for aSample in aListOfSamples:
        wLists.append(dictFromFile(aSample))
    return wLists


def phi_calculation(d, doc_questioned, feature):
    d_set = Counter(d.split())
    doc_questioned_set = Counter(doc_questioned.split())
    f_set = feature(d)

    final_set = []

    # TODO: Could be len(d.slit()) instead
    for (key, value) in doc_questioned_set.iteritems():
        f_count = sum([d_set[token] for token in f_set if d_set.has_key(token)])
        final_set.append(float(value)/(f_count - len(d.split())))

    return final_set

def dist(x, y):
    """ Distance between two feature vectors """
    return np.sum(abs(np.array(x) - np.array(y)))

def sim(x, y):
    """ Similarity between two feature vectors """
    return float(1)/(1+dist(x, y))


def runIt():
    myProbs = []
    myNewProbs = []
    t = 0.025
    import pdb
    for (known, unknown) in zip(allKnownDocs, allUnknownDocs):
        d_known = " ".join(known)
        d_unknown = " ".join(unknown)

        f_known = phi_calculation(d_known, d_unknown, f2)
        f_unknown = phi_calculation(d_unknown, d_unknown, f2)

        print dist(f_known, f_unknown)
        print sim(f_known, f_unknown)

        # print f_known
        # break

    # myProbs = normProbs(myProbs, t)
    # aName = "answers"
    # writeNameAndScore(foldersPAN, myProbs, outputFolder, aName)


if __name__ == '__main__':
    print "The module panAV.py was uploaded\n"
    startTime = time.clock()

    inputFolder = ""
    outputFolder = ""

    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:o:")
    except getopt.GetoptError:
        print "panAV.py -i <inputFolder> -o <outputFolder>"
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-i":
            inputFolder = arg
        elif opt == "-o":
            outputFolder = arg

    assert len(inputFolder) > 0
    print "Input folder is", inputFolder
    assert len(outputFolder) > 0
    print "Output folder is", outputFolder

    aListListPAN, foldersPAN = getListListPANAndFoldersPAN(inputFolder)

    allKnownDocs = processAll([x[:-1] for x in aListListPAN])
    allUnknownDocs = processSamples([x[-1] for x in aListListPAN])

    runIt()

    print "\n done in %.2fs" % (time.clock() - startTime)
