# -*- coding: utf-8 -*-
import os.path
import random
import string
import sys
import getopt
import time
from model.group import Group


import clr
clr.AddReferenceByName('Microsoft.Office.Interop.Excel, Version=15.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c, processorArchitecture=MSIL')
from Microsoft.Office.Interop import Excel


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


try:
    opts, agrs = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as e:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.xlsx"

for op, arg in opts:
    if op == "-n":
        n = int(arg)
    elif op == "-f":
        f = arg

testdata = [Group(name="")] + [
    Group(name=random_string("Name", 10))
    for count in range(n)
]

file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
if not os.path.exists(os.path.join(os.getcwd(), "..", "data")):
    os.mkdir("../data")
elif os.path.exists(os.path.join(os.getcwd(), "data", "groups.xlsx")):
    os.remove(os.getcwd(), "data", "groups.xlsx")

excel = Excel.ApplicationClass()
excel.Visible = True

workbook = excel.Workbooks.Add()
sheet = workbook.ActiveSheet

for i in range(len(testdata)):
    sheet.Range("A%s" % (i + 1)).Value2 = testdata[i].name
workbook.SaveAs(file_name)

time.sleep(3)
excel.Quit()
