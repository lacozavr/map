import sys
import requests
import io
from PyQt5 import uic, QtGui, QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QApplication


class Map(QMainWindow):
    def __init__(self):
        super(Map, self).__init__()
        uic.loadUi('E:/map.UI', self)
        #это
        self.s = 'Широта:'
        self.d = 'Долгота:'
        self.m = 'Масштаб:'
        self.pushButton.clicked.connect(self.search)
        self.x = ''
        self.y = ''
        self.mas_1 = ''
        self.mas_2 = ''
        self.shirota.setText(self.s)
        self.dolgota.setText(self.d)
        self.aaaa.setText(self.m)
        self.vid.addItem('Схема')
        self.vid.addItem('Спутник')
        self.vid.addItem('Гибрид')
        self.vids = {'Схема': 'map',
                     'Спутник': 'sat',
                     'Гибрид': 'skl'}
        self.vid.currentTextChanged.connect(self.search)


    def search(self):
        if self.pushButton.sender():
            self.x = self.shir.text()
            self.y = self.dolg.text()
            self.mas_1 = self.m_1.text()
            self.mas_2 = self.m_2.text()
        #это
        self.shirota.setText(self.s + f' {self.x}')
        self.dolgota.setText(self.d + f' {self.y}')
        self.aaaa.setText(self.m + f' {self.mas_1} X {self.mas_2}')

        api_server = f"https://static-maps.yandex.ru/1.x/?ll={self.x},{self.y}" \
                     f"&spn={self.mas_1},{self.mas_2}&l={self.vids[self.vid.currentText()]}"
        response = requests.get(api_server)
        if response:
            with open('map.png', 'wb') as file:
                file.write(response.content)
            pixmap = QtGui.QPixmap('map.png')
            self.map.setPixmap(pixmap)

    def keyPressEvent(self, event):
        #это
        if event.key() == 56:
            self.y = str(int(self.y) + 1)
            self.search()
        elif event.key() == 50:
            self.y = str(int(self.y) - 1)
            self.search()
        elif event.key() == 52:
            self.x = str(int(self.x) - 1)
            self.search()
        elif event.key() == 54:
            self.x = str(int(self.x) + 1)
            self.search()
        elif event.key() == 16777238:
            self.mas_1 = str(int(self.mas_1) + 1)
            self.mas_2 = str(int(self.mas_2) + 1)
            self.search()
        elif event.key() == 16777239:
            self.mas_1 = str(int(self.mas_1) - 1)
            self.mas_2 = str(int(self.mas_2) - 1)
            self.search()



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Map()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
