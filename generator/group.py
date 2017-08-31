# -*- coding: utf-8 -*-
import os.path
import random
import string
import sys
import getopt
from model.group import Group
from fixture.excel import ExcelHelper


class GroupGenerator(object):
    def __init__(self, app):
        self.app = app
        self.n = 5
        self.path = "data"
        self.file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", self.path, "groups.xlsx")
        self.check_options()

    def random_group_name(self, prefix, maxlen):
        symbols = string.ascii_letters + string.digits + " " * 10
        return prefix + "".join([random.choice(symbols) for i in range(maxlen)])
x
    def check_options(self):
        try:
            opts, agrs = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
        except getopt.GetoptError as e:
            getopt.usage()
            sys.exit(2)
        for op, arg in opts:
            if op == "-n":
                self.n = int(arg)
            elif op == "-f":
                self.file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", self.path, arg)

    def prepare_storage(self):
        if not os.path.exists(os.path.join(os.getcwd(), "..", self.path)):
            os.mkdir(os.path.join("..", self.path))
        elif os.path.exists(self.file):
            os.remove(self.file)

    def check_if_storage_exists(self):
        return False if not os.path.exists(os.path.join(os.getcwd(), "..", self.path)) or not os.path.exists(self.file)\
            else True

    def get_groups_list(self):
        return [Group(name="")] + [Group(name=self.random_group_name("Group ", 10)) for i in range(self.n)]

    def make_and_save_data(self):
        with ExcelHelper() as excel:
            workbook = excel.new_workbook()
            sheet = workbook.ActiveSheet
            testdata = self.get_groups_list()

            for i in range(len(testdata)):
                sheet.Range("A%s" % (i + 1)).Value2 = testdata[i].name
            workbook.SaveAs(self.file)

    def generate(self):
        self.prepare_storage()
        self.make_and_save_data()

    def get_data_from_file(self):
        with ExcelHelper() as excel:
            result_list = []
            sheet = excel.open_workbook(self.file).ActiveSheet
            row = 0
            while True:
                gr_name = sheet.Range("A%s" % (row + 1)).Value2
                if not gr_name and not sheet.Range("A%s" % (row + 2)).Value2:
                    # break if two consequent cells have empty values
                    break
                row += 1
                result_list.append(gr_name)
        return result_list

    def read(self):
        return None if not self.check_if_storage_exists() else self.get_data_from_file()