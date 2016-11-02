#!/usr/bin/env python

import sys

fname = sys.argv[1]
oname = fname[:fname.rfind(".")] + ".csv"

with open(fname, "r") as file:
    lines = file.readlines()

lines = [l.strip() for l in lines if l.strip()]

new_lines = []
for line in lines:
	pieces = line.split("... ")
	key = pieces[0].strip(".").strip().replace(",","")
	values = pieces[1].replace(",","").replace("...","?").split(" ")
	new_lines += [",".join([key]+values)]
with open(oname, "w") as file:
	file.write("\n".join(new_lines) + "\n")