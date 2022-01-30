import sys
from PyQt5.QtWidgets import  QApplication,QWidget
if __name__=='__main__':
    #创建QApplication类的实例
    app=QApplication(sys.argv)
    #创建窗口
    w=QWidget()
    w.resize(300,300)
    w.move(300,300)
    w.setWindowTitle("第一个pyqt桌面应用")
    w.show()

    #进入程序的主循环，并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())