#!/usr/bin/python
import sys
from pyparsing import *

graph = []

def mkGraph(str, location, tokens):
    syns = [i.strip().replace('\n' , ' ') for i in tokens[0].split('     ') if i.strip()]
    for s in syns:
        graph.append([x.split(',') for x in s.split(';')])
    print graph



head = "%" + OneOrMore(CharsNotIn("%")) + "%"
entry = Combine("#" + Word(alphanums) + ".") + Combine(Word(alphas) + OneOrMore(CharsNotIn(","))) + OneOrMore(CharsNotIn("#")).setParseAction(mkGraph)
entry.setResultsName('entry')
entries = OneOrMore(entry)

# entry.setParseAction(lambda s,l,t: mkEntry)

entries.parseString(open(sys.argv[1]).read())


