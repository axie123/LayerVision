from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(900, 700))    
        self.setWindowTitle("NetView v2.0 UI") 

        # The main menu.
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Main Menu')
        self.nameLabel.move(40, 10)
        b1 = QPushButton('Train Model',self)
        b1.resize(300,32)
        b1.move(40, 50)
        b2 = QPushButton('Layer Visual Images',self)
        b2.resize(300,32)
        b2.move(40, 100)
        b3 = QPushButton('Layer Losses',self)
        b3.resize(300,32)
        b3.move(40, 150)
        b4 = QPushButton('Accuracy of Individual Classes',self)
        b4.resize(300,32)
        b4.move(40, 200)
        b5 = QPushButton('Weights and Biases of Each Layer',self) 
        b5.resize(300,32)
        b5.move(40, 250)
        b1.clicked.connect(self.train_test)
        
        # Training Conditions.
        self.e = QLabel(self)
        self.e.setText('Epochs')
        self.e.move(400, 50)
        self.epochs = QLineEdit(self)
        self.epochs.move(400, 80)
        self.epochs.resize(100, 32)
        self.tr = QLabel(self)
        self.tr.setText('Train Size')
        self.tr.move(520, 50)
        self.train_size = QLineEdit(self)
        self.train_size.move(520, 80)
        self.train_size.resize(100, 32)
        self.t = QLabel(self)
        self.t.setText('Test Size')
        self.t.move(640, 50)
        self.test_size = QLineEdit(self)
        self.test_size.move(640, 80)
        self.test_size.resize(100, 32)
        self.r = QLabel(self)
        self.r.setText('Learning Rate')
        self.r.move(760, 50)
        self.rate = QLineEdit(self)
        self.rate.move(760, 80)
        self.rate.resize(100, 32)
        self.p = QLabel(self)
        self.p.setText('Momentum')
        self.p.move(400, 140)
        self.mom = QLineEdit(self)
        self.mom.move(400, 170)
        self.mom.resize(100, 32)
        self.l = QLabel(self)
        self.l.setText('Log Interval')
        self.l.move(520, 140)
        self.log_int = QLineEdit(self)
        self.log_int.move(520, 170)
        self.log_int.resize(100, 32)
        self.s = QLabel(self)
        self.s.setText('Random Seed')
        self.s.move(640, 140)
        self.seed = QLineEdit(self)
        self.seed.move(640, 170)
        self.seed.resize(100, 32)

        # Analysis  Components:
        self.n = QLabel(self)
        self.n.setText('Network')
        self.n.move(400, 270)
        self.network = QLineEdit(self)
        self.network.move(400, 300)
        self.network.resize(200, 32)
        self.ls = QLabel(self)
        self.ls.setText('Loss Function')
        self.ls.move(620, 270)
        self.loss = QLineEdit(self)
        self.loss.move(620, 300)
        self.loss.resize(200, 32)
        self.o = QLabel(self)
        self.o.setText('Optimization')
        self.o.move(400, 350)
        self.method = QLineEdit(self)
        self.method.move(400, 380)
        self.method.resize(300, 32)
        self.ly = QLabel(self)
        self.ly.setText('Layer Number')
        self.ly.move(400, 430)
        self.layer = QLineEdit(self)
        self.layer.move(400, 460)
        self.layer.resize(100, 32)
        self.d = QLabel(self)
        self.d.setText('Data Results')
        self.d.move(520, 430)
        self.data = QLineEdit(self)
        self.data.move(520, 460)
        self.data.resize(250, 32)
        self.i = QLabel(self)
        self.i.setText('Image Pos.')
        self.i.move(400, 510)
        self.ith = QLineEdit(self)
        self.ith.move(400, 540)
        self.ith.resize(100, 32)

    def train_test(self):
        print('Code is in the other file.')
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )