#임경수  pyqt5 이용한 테스트 어플리케이션 제작에서 사용. 웹 어플리케이션 사용 후에는 사용하지 않음

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import second

form_class = uic.loadUiType('get_readey.ui')[0]

class Home(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.todiff.clicked.connect(self.to_menu)

    def to_menu(self):
        text = self.menu_box.currentText()
        if(text == '아키네이터'):
            self.newWindow = second.MyWindow(self)
            self.newWindow.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    home_window = Home()
    home_window.show()
    app.exec_()
