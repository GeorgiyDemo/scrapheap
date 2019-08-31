"""
    Создание PDF-файла книги c библиo oнлaйн
"""

import requests
import os

from PyPDF2 import PdfFileWriter, PdfFileReader
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF

URL = ""
PDF_FILE = "OUTPUT.pdf"

cookies = {
    "__atssc":"",
    "__atuvc": "",
    "__atuvs": "",
    "__cfduid": "",
    "_fbp":"",
    "_ga":"",
    "_gat_UA-39193361-1":"",
    "_gid":"",
    "_ym_d":"",
    "_ym_isad":"",
    "_ym_uid":"",
    "_ym_visorc_42398809":"",
    "jv_enter_ts_0avhLAO4rv":"",
    "jv_pages_count_0avhLAO4rv":"",
    "jv_visits_count_0avhLAO4rv":"",
    "laravel_session":"",
    "popupDisplayWebinarsGuest":"",
    "popupDisplayWebinarsNonGuest":"",
}

def merger(input_paths):
    pdf_writer = PdfFileWriter()
 
    for path in input_paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
 
    with open(PDF_FILE, 'wb') as fh:
        pdf_writer.write(fh)

    print("Создали PDF <3")

class FileProcessing(object):
    def __init__(self, number):
        self.result = "processing"
        self.number = number
        self.get_book()
        self.to_pdf()
    
    def get_book(self):
        print(URL+self.number)
        r = requests.get(URL+self.number, allow_redirects=True, cookies=cookies)
        open("file"+self.number+".svg", 'wb').write(r.content)

    def to_pdf(self):
        try:
            drawing = svg2rlg("file"+self.number+".svg")
            renderPDF.drawToFile(drawing, "file"+self.number+".pdf")
        except AttributeError:
            print("Страницы закончились")
            self.result = "ready"

class MainClass(object):
    def __init__(self):
        self.main()

    def main(self):
        pdf_filelist = []
        page_number = 1
        while True:
            obj = FileProcessing(str(page_number))
            if obj.result == "ready":
                break
            pdf_filelist.append("file"+str(page_number)+".pdf")
            page_number += 1
        merger(pdf_filelist)

if __name__ == "__main__":
    MainClass()