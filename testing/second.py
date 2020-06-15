#임경수  pyqt5 이용한 테스트 어플리케이션 제작에서 사용. 웹 어플리케이션 사용 후에는 사용하지 않음

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import webbrowser

form_class = uic.loadUiType('testing.ui')[0]
no_texts = ['dodo','and','goodbye','gyungsu', 'dodo']
yes_texts = ['no','yes','chengju', 'browser','damage']

class MyWindow(QMainWindow, form_class):
    no_count = 1
    yes_count = 0
    prog = 0

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.nobutton.clicked.connect(self.no_clicked)
        self.yesbutton.clicked.connect(self.yes_clicked)
        self.progress.setValue(self.prog)
        self.textfield.setText(no_texts[0])

    def check_percentage(self):
        if self.prog >= 100:
            webbrowser.open("www.naver.com")

    def no_clicked(self):
        if self.no_count < len(no_texts):
            self.textfield.setText(no_texts[self.no_count])
            self.no_count += 1
            self.prog += 5
            self.progress.setValue(self.prog)
            self.check_percentage()
        else:
            self.no_count = 0
            self.textfield.setText(no_texts[self.no_count])
            self.prog += 5
            self.progress.setValue(self.prog)
            self.check_percentage()

    def yes_clicked(self):
        if self.yes_count < len(yes_texts):
            self.textfield.setText(yes_texts[self.yes_count])
            self.yes_count += 1
            self.prog += 5
            self.progress.setValue(self.prog)
            self.check_percentage()
        else:
            self.yes_count = 0
            self.textfield.setText(yes_texts[self.yes_count])
            self.prog += 5
            self.progress.setValue(self.prog)
            self.check_percentage()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
