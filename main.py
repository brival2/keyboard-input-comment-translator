# -*- coding: utf-8 -*-
import json
import os
import string
import csv
import codecs
import numpy as np

# change the environment so that it accepts UTF-8
os.putenv('PYTHONIOENCODING', 'UTF-8')

# change the ID depending on which video you want
vidid = '8x9xoxB1DfI'
os.system('downloader.py --youtubeid '+ vidid + ' --output ' + vidid + '.json')

# get the path of the filename of the translation table
filename = (##PATHNAME##)

# read the translation able
with open(filename) as file:
    content = file.read().splitlines()

# make the dictionary
eng = []
translang = []

for a in content:
    c = a.decode('utf-8')
    eng.append(c[0])
    translang.append(c[2])

print 'eng'
print eng
print 'output language'
print translang

# print the dictionary
conv_dict = dict(zip(eng,translang))
print conv_dict

data = []

# translation function
def trans(to_trans):
    q = []
    translated = unicode('')
    for r in unicode(to_trans,'utf-8'):
        b = conv_dict.get(r)
        if b is not None:
            translated.join(b)
            q.append(b)
            translated.join(r)
        else:
            q.append(r)
    print 'translation:'
    return q

def conv_arr(arr):
    for i in arr:
        print i.encode('utf-8'),

# get the lines from the JSON file
commentfile = vidid + '.json'
with open(r'##PATHNAME##' + commentfile) as f:
    for line in f:
        data.append(json.loads(line))


# print out the translation
for a in data:
    s = unicode(a.values()[0]).encode('utf8')
    print(s)
    e = trans(s)
    y = conv_arr(e)
    print(y)
