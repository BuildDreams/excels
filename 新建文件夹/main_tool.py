
import sys
import os
from new_tools import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow,  QWidget, QMessageBox, \
    QInputDialog

from functions import *



class MyCalc(QWidget):
    """
    重写多进程逻辑
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)




    def yunxing(self, *args):
        """
        运行函数模块，自动调用Runthread类run函数
        :param args:
        :return:
        """

        print('运行函数')
        # print(len(args[2]))
        if args[0] == 0 and len(args[2]) != 0:#竖向连接函数
            self.myThread = Runthread(*args)
            # 6.接收信号并产生回调函数
            self.myThread.updata_date.connect(self.Display)
            self.myThread.start()
        elif args[0] == 1 :#横向连接函数
            try:
                print(args[2])
                for file in args[2]:
                    cols = Cols_name(file)
                item, okPressed = QInputDialog.getItem(self, "选择连接轴", "字段", cols, 4, True)  # 单选复选框，后面功能需要用到
                self.myThread = Runthread(item,*args)
            # 6.接收信号并产生回调函数
                self.myThread.updata_date.connect(self.Display)
                self.myThread.start()
            except:
                pass
                # QMessageBox.warning(self.ui, 'ERROR', '请选择文件/合并模式', QMessageBox.Yes, QMessageBox.Yes)

    # 7我是回调函数
    def Display(self, data):
        self.ui.show_files.clear()
        if data == 1:
            QMessageBox.information(self.ui, 'INFO', '合并完成', QMessageBox.Yes, QMessageBox.Yes)
        elif data == 2:
            print('异常处理')
            QMessageBox.warning(self.ui, 'ERROR', '请选择文件/合并模式/列名不存在', QMessageBox.Yes, QMessageBox.Yes)
        print('回调函数')
        return



# 进程模块
class Runthread(QtCore.QThread):
    """
    多进程模块
    """
    updata_date = QtCore.pyqtSignal(int)

    def __init__(self, *args):
        super(Runthread, self).__init__()
        self.singl = args
        print(args)
    def run(self):
        """
        将自动被调用
        :return: 具体调用函数，并且返回回调函数参数。
        """
        print('Run函数',self.singl)
        try:
            if self.singl[1] == 1:

                res = Start(self.singl[3], self.singl[2], self.singl[1],self.singl[0])
                print(res)
                self.updata_date.emit(1)
            elif self.singl[0] == 0 :
                print('横向合并')
                Start(self.singl[2], self.singl[1], self.singl[0], indexs='')

                self.updata_date.emit(1)
        except:
            print('EXCEPT============')
            self.updata_date.emit(2)
        print('运行完成')
        return





# 主入口
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    win = MyCalc()
    win.show()
    os.remove('mg.ico')
    sys.exit(app.exec_())