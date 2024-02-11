import sys
import requests
import io
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication


class Map(QMainWindow):
    def __init__(self):
        super(Map, self).__init__()
        uic.loadUi('E:/map.UI', self)
        self.pushButton.clicked.connect(self.search)

    def search(self):
        api_server = f"https://static-maps.yandex.ru/1.x/?ll={self.shir.text()},{self.dolg.text()}" \
                     f"&spn={self.m_1.text()},{self.m_2.text()}&l=map"
        response = requests.get(api_server)
        if response:
            with open('map.png', 'wb') as file:
                file.write(response.content)
            pixmap = QtGui.QPixmap('map.png')
            self.map.setPixmap(pixmap)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Map()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())