# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tools.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!
ALL_FILES = []
BTN_ID = ''
LEFT_FILES =[]
RIGHT_FILES = []
To_A =1
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QAction, QMenu,QButtonGroup, QMessageBox,QInputDialog
import sys
from show_sheetname import main,jion_left_right,cols_name
import os

class Ui_Dialog(QWidget):
    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(1116, 738)
        self.cwd = os.getcwd()

        self.y_outer = QtWidgets.QRadioButton(Dialog)
        self.y_outer.setGeometry(QtCore.QRect(170, 90, 89, 16))
        self.y_outer.setObjectName("y_outer")

        self.y_inner = QtWidgets.QRadioButton(Dialog)
        self.y_inner.setGeometry(QtCore.QRect(170, 150, 89, 16))
        self.y_inner.setObjectName("y_inner")

        self.y_jions = QtWidgets.QPushButton(Dialog)
        self.y_jions.setGeometry(QtCore.QRect(40, 110, 75, 23))
        self.y_jions.setObjectName("y_jions")

        self.x_left = QtWidgets.QRadioButton(Dialog)
        self.x_left.setGeometry(QtCore.QRect(170, 340, 89, 16))
        self.x_left.setObjectName("x_left")

        self.x_inner = QtWidgets.QRadioButton(Dialog)
        self.x_inner.setGeometry(QtCore.QRect(170, 310, 89, 16))
        self.x_inner.setObjectName("x_inner")

        self.x_outer = QtWidgets.QRadioButton(Dialog)
        self.x_outer.setGeometry(QtCore.QRect(170, 270, 89, 16))
        self.x_outer.setObjectName("x_outer")

        self.x_right = QtWidgets.QRadioButton(Dialog)
        self.x_right.setGeometry(QtCore.QRect(170, 370, 89, 16))
        self.x_right.setObjectName("x_right")

        self.y_text = QtWidgets.QTextBrowser(Dialog)
        self.y_text.setGeometry(QtCore.QRect(300, 40, 711, 161))
        self.y_text.setObjectName("y_text")

        self.down_left_text = QtWidgets.QTextBrowser(Dialog)
        self.down_left_text.setGeometry(QtCore.QRect(300, 240, 330, 171))
        self.down_left_text.setObjectName("down_left_text")

        self.down_right_text = QtWidgets.QTextBrowser(Dialog)
        self.down_right_text.setGeometry(QtCore.QRect(680, 240, 330, 171))
        self.down_right_text.setObjectName("down_right_text")

        self.x_jions = QtWidgets.QPushButton(Dialog)
        self.x_jions.setGeometry(QtCore.QRect(40, 300, 75, 23))
        self.x_jions.setObjectName("x_jions")

        self.files_up = QtWidgets.QPushButton(Dialog)
        self.files_up.setGeometry(QtCore.QRect(560, 10, 75, 23))
        self.files_up.setObjectName("files_up")

        self.files_down_left = QtWidgets.QPushButton(Dialog)
        self.files_down_left.setGeometry(QtCore.QRect(460, 210, 75, 23))
        self.files_down_left.setObjectName("files_down")

        self.files_down_right = QtWidgets.QPushButton(Dialog)
        self.files_down_right.setGeometry(QtCore.QRect(800, 210, 75, 23))
        self.files_down_right.setObjectName("files_down")

        self.bg1 = QButtonGroup()
        self.bg1.addButton(self.y_outer, 11)
        self.bg1.addButton(self.y_inner, 21)

        self.bg2 = QButtonGroup()
        self.bg2.addButton(self.x_inner, 11)
        self.bg2.addButton(self.x_left, 21)
        self.bg2.addButton(self.x_outer, 31)
        self.bg2.addButton(self.x_right, 41)

        self.msgBox = QMessageBox()

        self.files_up.clicked.connect(lambda :self.btn_chose_files(1))
        self.files_down_left.clicked.connect(lambda :self.btn_chose_files(2))
        self.files_down_right.clicked.connect(lambda :self.btn_chose_files(3))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.y_outer.setText(_translate("Dialog", "全集"))
        self.y_inner.setText(_translate("Dialog", "交集"))
        self.y_jions.setText(_translate("Dialog", "纵向合并"))

        self.x_left.setText(_translate("Dialog", "左连接"))
        self.x_inner.setText(_translate("Dialog", "交集"))

        self.x_outer.setText(_translate("Dialog", "全集"))
        self.x_right.setText(_translate("Dialog", "右连接"))
        self.x_jions.setText(_translate("Dialog", "横向合并"))
        self.files_up.setText(_translate("Dialog", "文件1"))
        self.files_down_left.setText(_translate("Dialog", "左表文件"))
        self.files_down_right.setText(_translate("Dialog", "右表文件"))

        self.y_jions.clicked.connect(lambda: Dialog.yunxing(1, ))
        self.x_jions.clicked.connect(lambda: Dialog.yunxing(2, ))
        self.bg1.buttonClicked.connect(self.chose_types)
        self.bg2.buttonClicked.connect(self.chose_types)

#选择文件模块
    def btn_chose_files(self,id):
        print(self)
        files, filetype = QFileDialog.getOpenFileNames(self,
                                                       "选择文件",
                                                       self.cwd,  # 起始路径'
                                                      "Excle (*.xlsx);;")
        for file in files:
            if id ==1:
                self.y_text.append(file)
                ALL_FILES.append(file)
            elif id == 2:
                self.down_left_text.append(file)
                LEFT_FILES.append(file)
                cols = cols_name(LEFT_FILES[0])
                self.getChoice(cols)

            elif id == 3:
                self.down_right_text.append(file)
                RIGHT_FILES.append(files)

    def getChoice(self,cols):  # Get item/choice
        print(cols)
        items = ("Red", "Blue", "Green")
        item, okPressed = QInputDialog.getItem(self, "Get item", "Color:", cols, 1, False)
        if okPressed and item:
            return item

    def chose_types(self):
        sender = self.sender()
        global BTN_ID
        global To_A
        if sender == self.bg1:
            To_A = 0
            if self.bg1.checkedId() == 11:

                BTN_ID = 'outer'

            elif self.bg1.checkedId() == 21:
                BTN_ID = 'inner'
        if sender == self.bg2:
            To_A = 1
            if self.bg2.checkedId() == 11:
                BTN_ID = 'inner'
            elif self.bg2.checkedId() == 21:
                BTN_ID = 'left'
            elif self.bg2.checkedId() == 31:
                BTN_ID = 'outer'
                self.getChoice()
                # QMessageBox.question(self, 'waring', '输入索引列',
                #              QMessageBox.Yes, QMessageBox.Yes)
            elif self.bg2.checkedId() == 41:
                BTN_ID = 'right'




class MyCalc(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def yunxing(self, *args):
        self.myThread = Runthread(*args)

        # 6.接收信号并产生回调函数
        self.myThread.updata_date.connect(self.Display)

        self.myThread.start()

        # 7我是回调函数

    def Display(self, data):
        pass

#进程模块
class Runthread(QtCore.QThread):
    updata_date = QtCore.pyqtSignal(str)

    def __init__(self, *args):

        super(Runthread, self).__init__()
        self.st = args

    def run(self):

        if self.st[0] == 1:
            print(ALL_FILES)
            #main(files,chose_type,TO,indexs):
            #jion_sheets(file,chose_type,filename,TO,indexs):
            indexs =""
            main(ALL_FILES,BTN_ID,To_A,indexs=indexs)
        elif self.st[0] == 2:
            indexs = "这是indexs"
            jion_left_right(LEFT_FILES,RIGHT_FILES,indexs,BTN_ID)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    win = MyCalc()
    win.show()
    sys.exit(app.exec_())