from PyQt5.QtGui import QPainter,QColor,QFont
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import Qt
import sys

class DrawText(QWidget):
    def __init__(self):
        super(DrawText, self).__init__()
        self.setWindowTitle("在窗口上绘制文本")
        self.resize(300,200)
        self.text="不想熬夜敲代码了"
    def paintEvent(self, event):
        # 创建QPainter对象
        painter=QPainter(self)
        painter.begin(self)
        print("aaa")
        painter.setPen(QColor(150,43,5))
        painter.setFont(QFont("SimSun",25))
        painter.drawText(event.rect(),Qt.AlignCenter,self.text)
        painter.end()

if __name__=='__main__':
    #创建QApplication类的实例
    app=QApplication(sys.argv)
    main=DrawText()
    main.show()
    sys.exit(app.exec_())