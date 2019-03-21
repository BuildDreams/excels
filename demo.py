# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!
import os
import sys
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QAction, QMenu
from show_sheetname import show_sheet_name,jion_sheets

class Ui_Dialog(QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1088, 746)

        self.cwd = os.getcwd()

        self.left = QtWidgets.QPushButton(Dialog)
        self.left.setGeometry(QtCore.QRect(60, 40, 100, 23))
        self.left.setObjectName("left")

        self.right = QtWidgets.QPushButton(Dialog)
        self.right.setGeometry(QtCore.QRect(70, 300, 100, 23))
        self.right.setObjectName("right")

        self.left_name_left = QtWidgets.QPushButton(Dialog)
        self.left_name_left.setGeometry(QtCore.QRect(300, 5, 75, 23))
        self.left_name_left.setObjectName("left_name")

        self.left_text = QtWidgets.QTextBrowser(Dialog)
        self.left_text.setGeometry(QtCore.QRect(160, 30, 300, 100))
        self.left_text.setObjectName("right_text")

        self.left_text_right = QtWidgets.QTextBrowser(Dialog)
        self.left_text_right.setGeometry(QtCore.QRect(500, 30, 500, 100))
        self.left_text_right.setObjectName("right_text")

        self.left_name_right = QtWidgets.QPushButton(Dialog)
        self.left_name_right.setGeometry(QtCore.QRect(700, 5, 75, 23))
        self.left_name_right.setObjectName("left_name_right")

        self.jion_sheet = QtWidgets.QPushButton(Dialog)
        self.jion_sheet.setGeometry(QtCore.QRect(700, 150, 150, 30))
        self.jion_sheet.setObjectName("jion_sheet")

        self.right_text = QtWidgets.QTextBrowser(Dialog)
        self.right_text.setGeometry(QtCore.QRect(160, 300, 500, 100))
        self.right_text.setObjectName("show_res")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.left.setText(_translate("Dialog", "查看源文件sheet"))
        self.right.setText(_translate("Dialog", "目标文件"))
        self.left_name_left.setText(_translate("Dialog", "当前文件"))
        self.left_name_right.setText(_translate("Dialog", "当前sheet"))
        self.jion_sheet.setText(_translate("Dialog", "合并当前sheet文件"))
        # -----------------------------------------------------------------------------
        self.left.clicked.connect(self.slot_btn_chooseMutiFile)
        self.jion_sheet.clicked.connect(lambda: Dialog.yunxing(1,Dialog))

        #----------------------------------样式
        self.left_text.setStyleSheet('border: 2px solid  red ')
        self.left_text_right.setStyleSheet('border: 2px solid  red ')
        self.right_text.setStyleSheet('border: 2px solid  red ')
        self.left_name_right.setStyleSheet('border:none')
        self.left_name_left.setStyleSheet('border:none')
        self.jion_sheet.setStyleSheet('line-height:24px')
    # 选择文件
    def slot_btn_chooseMutiFile(self):
        self.left_text.clear()
        self.left_text_right.clear()
        print(self)
        files, filetype = QFileDialog.getOpenFileNames(self,
                                                       "选择文件",
                                                       self.cwd,  # 起始路径'
                                                       "Excle (*.xlsx);;")

        if len(files) == 0:
            return
        for file in files:
            print(file)
            all_sheet_name = show_sheet_name(file=file)
            print(all_sheet_name)
            self.left_text.append(file)
            self.left_text.append('-'*45)
            self.left_text_right.append(",".join(all_sheet_name))
            self.left_text_right.append('-' * 78)



    # def jion_sheets(self):
    #
    #     self.left_text.clear()
    #     self.left_text_right.clear()
    #     print(self)
    #     files, filetype = QFileDialog.getOpenFileNames(self,
    #                                                    "选择文件",
    #                                                    self.cwd,  # 起始路径'
    #                                                    "Excle (*.xlsx);;")
    #
    #     if len(files) == 0:
    #         return
    #     space_data_frame = pd.DataFrame()
    #     for file in files:
    #         all_sheet_name = show_sheet_name(file=file)
    #         self.left_text.append(file)
    #         self.left_text.append('-'*48)
    #         self.left_text_right.append(",".join(all_sheet_name))
    #         self.left_text_right.append('-' * 80)
    #         space_data_frame = jion_sheets(file,sheet_names=all_sheet_name,datas=space_data_frame)
    #     space_data_frame.to_excel('./res.xlsx')



class MyCalc(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        #############################################################################
        #设置系统托盘
        # minimizeAction = QAction("Mi&nimize", self, triggered=self.hide)
        # maximizeAction = QAction("Ma&ximize", self, triggered=self.showMaximized)
        # restoreAction = QAction("&还原", self, triggered=self.showNormal)
        # quitAction = QAction("&退出", self, triggered=QApplication.instance().quit)  # 退出APP
        # self.trayMenu = QMenu(self)
        # self.trayMenu.addAction(minimizeAction)
        # self.trayMenu.addAction(maximizeAction)
        # self.trayMenu.addAction(restoreAction)
        # self.trayMenu.addSeparator()
        # self.trayMenu.addAction(quitAction)
        # self.ui.tray.setContextMenu(self.trayMenu)


    def yunxing(self, *args):

        self.myThread = Runthread(*args)

        # 6.接收信号并产生回调函数
        self.myThread.updata_date.connect(self.Display)

        self.myThread.start()

    # 7我是回调函数
    def Display(self, data):
        pass

class Runthread(QtCore.QThread):
    updata_date = QtCore.pyqtSignal(str)

    def __init__(self, *args):

        super(Runthread, self).__init__()
        self.st = args

    def run(self):
        if self.st[0] == 1:
            print('0000')
            self.run_jion_sheets()
        elif self.st[0] == 2:
            self.run_mongo()



    def run_jion_sheets(self):
        pass
        # print(dir(self.st[1]))

        # self.st[1].clear()
        # # self.ui.left_text_right.clear()
        # print(self.ui)
        print(Ui_Dialog())
        files, filetype = QFileDialog.getOpenFileNames(parent=QFileDialog,caption= "选择文件",
                                                       directory =  self.cwd,  # 起始路径'
                                                       initialFilter = "Excle (*.xlsx);;")
        #
        # if len(files) == 0:
        #     return
        # space_data_frame = pd.DataFrame()
        # for file in files:
        #     all_sheet_name = show_sheet_name(file=file)
        #     self.left_text.append(file)
        #     self.left_text.append('-' * 48)
        #     self.left_text_right.append(",".join(all_sheet_name))
        #     self.left_text_right.append('-' * 80)
        #     space_data_frame = jion_sheets(file, sheet_names=all_sheet_name, datas=space_data_frame)
        # space_data_frame.to_excel('./res.xlsx')

if __name__ == "__main__":
    import sys

    # app = QtWidgets.QApplication(sys.argv)
    # widget = QtWidgets.QWidget()
    # ui = Ui_Dialog()
    # ui.setupUi(widget)
    # widget.show()
    # sys.exit(app.exec_())
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    # MainWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
    # MainWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
    # MainWindow.setWindowFlags(Qt::FramelessWindowHint)
    win = MyCalc()
    win.show()

    # ui = Ui_Dialog()
    # ui.setupUi(MainWindow)
    # MainWindow.show()

    sys.exit(app.exec_())
