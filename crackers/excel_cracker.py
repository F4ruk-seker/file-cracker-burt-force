import os
import win32com.client

win32com.client.Dispatch('Excel.Application')
class ExcelCracker(object):
    def __init__(self,file_path):
        self.file_path = file_path
        self.__EXCEL_ENGINE = "win32com.client.Dispatch('Excel.Application')"

    def try_crack_password(self,password):
        try:
            print("excute")
            # wb = self.__EXCEL_ENGINE.Workbooks.Open(self.file_path, False, True, None)
            # ws = wb.Sheets(1)
            # ws.Unprotect(password)
            # print('Successfully Password: ', password)
            # self.__EXCEL_ENGINE.Quit()
        except:
            pass



exc = ExcelCracker("test")

