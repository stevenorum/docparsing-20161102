#!/usr/bin/env python

import sys

fname = sys.argv[1]
oname = fname[:fname.rfind(".")] + ".csv"

with open(fname, "r") as file:
    lines = file.readlines()

lines = [l.strip() for l in lines if l.strip()]
correct_lines = [lines[0]]
lines = lines[1:] # first line of this file is just fine

num_rows = len([l for l in lines if l.endswith("...")])
build_lines = lines[0:num_rows]
lines = lines[num_rows:]
for i in range(len(lines)):
	build_lines[i%num_rows] = build_lines[i%num_rows] + " " + lines[i]
lines = correct_lines + build_lines

new_lines = []

for line in lines:
	pieces = line.split("... ")
	key = pieces[0].strip(".").strip()
	values = pieces[1].replace(",","").replace("...","?").split(" ")
	new_lines += [",".join([key]+values)]
with open(oname, "w") as file:
	file.write("\n".join(new_lines) + "\n")