import os
import sys
import PyPDF2
import fileinput


# base = os.getcwd()
# file_path = os.path.join(base,"test.pdf")
# file = PyPDF2.PdfReader("test.pdf")
# file.encrypt(user_password="pars")

class PDFCracker:
    def __init__(self,file_path):
        self.file_path = file_path
        self.__ENGINE = PyPDF2.PdfReader

    def check_file_status(self):
        if os.path.isfile(self.file_path):
            pass
        else:
            raise "dosya bulunamadı"

    def try_password_crack(self,password):
        status = self.__ENGINE(self.file_path)
        if status.is_encrypted:
            pass
        else:
            raise

class pdf_cracker_file_already_decrypt(Exception):
    pass

pdf = PDFCracker("test.pdf")
pdf.try_password_crack("252525")