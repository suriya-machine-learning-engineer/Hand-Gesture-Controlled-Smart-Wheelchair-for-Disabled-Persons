


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import cv2
from commands import detect

class Ui_Form3(object):
    def setupUi(self, Form3):
        Form3.setObjectName("Form3")
        Form3.resize(800, 600)
        self.label = QtWidgets.QLabel(Form3)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("22.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Form3)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 851, 51))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")

        self.pushButton_2 = QtWidgets.QPushButton(Form3)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 410, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(219,112,147);\n"
"border-radius:20px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.hand)

        self.retranslateUi(Form3)
        QtCore.QMetaObject.connectSlotsByName(Form3)

    def retranslateUi(self, Form3):
        _translate = QtCore.QCoreApplication.translate
        Form3.setWindowTitle(_translate("Form3", "Form"))
        self.label_4.setText(_translate("Form3", "HAND GESTURE ANALYSIS "))

        self.pushButton_2.setText(_translate("Form3", "START"))

    def hand(self):
        detect()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form3 = QtWidgets.QWidget()
    ui = Ui_Form3()
    ui.setupUi(Form3)
    Form3.show()
    sys.exit(app.exec_())
