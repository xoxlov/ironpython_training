# -*- coding: utf-8 -*-


class ExcelHelper(object):
    def __init__(self):
        import clr
        clr.AddReferenceByName("Microsoft.Office.Interop.Excel, Version=15.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c, processorArchitecture=MSIL")
        from Microsoft.Office.Interop import Excel
        self.Excel = Excel
        self.excel = None

    def new_workbook(self):
        return self.excel.Workbooks.Add()

    def open_workbook(self, filename):
        return self.excel.Workbooks.Open(filename)

    def __enter__(self):
        self.excel = self.Excel.ApplicationClass()
        self.excel.Visible = True
        # This method redefinition is required according to the PEP 343 to use the class in 'with .. as' constructions
        return self

    def __exit__(self, type, value, traceback):
        # This method redefinition is required according to the PEP 343 to use the class in 'with .. as' constructions
        self.excel.Quit()
