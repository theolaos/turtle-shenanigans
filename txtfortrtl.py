from turtle import *

def read_fil_for_trtl(s,tr):
    t = open(s, 'r')
    lines = []
    lines = t.readlines()
    for i in range(len(lines)):
        if i == 0:
            tr.pu()
        tr.goto(float(lines[i][0 : lines[i].find(' ')]) , float(lines[i][lines[i].find(' ') : len(lines[i])]))
        if i == 0:
            tr.pd()
    t.close()

def write_txt(s,tuplee):
    t = open(s, 'w+')

    for i in range(len(tuplee)):  
        t.write(str(tuplee[i][0]) + ' ' + str(tuplee[i][1])+'\n')
    t.close()

def writ_simpfil(a,j):
    tuplee = []
    s = open(a, 'r')
    tuplee = s.readlines()

    t = open(j, 'w+')
    i = 0
    while i < len(tuplee):
        t.write(str(tuplee[i]))
        i += 4
    t.write(str(tuplee[len(tuplee)-1]))
    s.close()
    t.close()