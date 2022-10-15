import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic


class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('resources/mainwindow.ui', self)
        self.statusBar().showMessage('Broker connection status: OFFLINE')
        self.buttonsHandler()

    def buttonsHandler(self):
        self.MQTTConnectBtn.clicked.connect(self.MQTTConnection)

    def MQTTConnection(self):
        MQTTAddress = self.MQTTAddress.text()
        ip = MQTTAddress.split(':')[0]
        port = MQTTAddress.split(':')[1]

app = QtWidgets.QApplication(sys.argv)
