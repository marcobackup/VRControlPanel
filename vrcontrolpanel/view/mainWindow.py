import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from vrcontrolpanel.api.MQTT import MQTTClient


class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('resources/mainwindow.ui', self)
        self.setWindowIcon(QtGui.QIcon('resources/icon.png'))
        self.isConnected = False
        self.MQTTClient = MQTTClient(self.refreshRoverTelemetry)
        self.statusBar().showMessage('Broker connection status: ❌')
        self.buttonsHandler()

    def resetRoverTelemetry(self):
        self.velocityParam.setText('<strong>0.0 m/s</strong>')
        self.orientationParam.setText('<strong>0</strong>')
        self.steeringAngleParam.setText('<strong>0.0*</strong>')
        self.probesParam.setText('<strong>0</strong>')

    def buttonsHandler(self):
        self.MQTTConnectBtn.clicked.connect(self.MQTTConnection)
        self.publishBtn.clicked.connect(self.publish)
        self.actioninfo.triggered.connect(self.info)

    def MQTTConnection(self):
        MQTTAddress = self.MQTTAddress.text()
        try:
            ip = MQTTAddress.split(':')[0]
            port = MQTTAddress.split(':')[1]
            if not self.isConnected:
                if not self.MQTTClient.connect(ip, int(port)):
                    self.isConnected = True
                    self.statusBar().showMessage('Broker connection status: ✅')
                    self.MQTTAddress.setEnabled(False)
                    self.MQTTConnectBtn.setText('disconnect')
                    self.roverTelemetryBox.setEnabled(True)
                    self.LMAOInterfaceBox.setEnabled(True)
                    self.publishBtn.setEnabled(True)
                    self.MQTTClient.subscribe('VR/rover/control/velamount')
                    self.MQTTClient.subscribe('VR/rover/control/velangle')
                    self.MQTTClient.subscribe('VR/rover/feedback/velocity')
                    self.MQTTClient.subscribe('VR/rover/feedback/orientation')
                    self.MQTTClient.subscribe('VR/rover/feedback/steeringAngle')
                    self.MQTTClient.subscribe('VR/game/probes')
                    self.MQTTClient.start()
                else:
                    pass
            else:
                if not self.MQTTClient.disconnect():
                    self.isConnected = False
                    self.statusBar().showMessage('Broker connection status: ❌')
                    self.MQTTAddress.setEnabled(True)
                    self.MQTTConnectBtn.setText('connect')
                    self.roverTelemetryBox.setEnabled(False)
                    self.LMAOInterfaceBox.setEnabled(False)
                    self.publishBtn.setEnabled(False)
                    self.resetRoverTelemetry()
                    self.MQTTClient.stop()
        except:
            QtWidgets.QMessageBox.critical(self, 'Invalid address', 'Please, put a valid broker address (<ip:port>)')

    def publish(self):
        velocityAmount = self.velocityAmount.value()
        steeringAngleAmount = self.steeringAngleAmount.value()
        self.MQTTClient.publish('VR/rover/control/velamount', float(velocityAmount))
        self.MQTTClient.publish('VR/rover/control/velangle', float(steeringAngleAmount))

    def info(self):
        QtWidgets.QMessageBox.information(self, 'About', 'ARDITO control panel powered by python3.9!')

    def refreshRoverTelemetry(self, client, userdata, msg):
        if msg.topic is not None:
            data = msg.payload.decode('utf-8')
            if msg.topic == 'VR/rover/feedback/velocity':
                self.velocityParam.setText(f'<strong>{round(float(data), 3)} m/s</strong>')
            elif msg.topic == 'VR/rover/feedback/orientation':
                self.orientationParam.setText(f'<strong>{round(float(data), 3)}</strong>')
            elif msg.topic == 'VR/rover/feedback/steeringAngle':
                self.steeringAngleParam.setText(f'<strong>{round(float(data), 3)}°</strong>')
            # elif msg.topic == 'VR/game/probes':
             #    self.probesParam.setText(f'<strong>{data}</strong>')
            else:
                pass


app = QtWidgets.QApplication(sys.argv)
