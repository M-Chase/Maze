import math

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

class Drawpoints(QWidget):
    def __init__(self):
        super(Drawpoints,self).__init__()
        self.resize(700,500)
        self.setWindowTitle("在窗口上绘制正弦曲线")
        self.pos_xy = []
    def mouseReleaseEvent(self, QMouseEvent):
        print(QMouseEvent.x(),QMouseEvent.y())
        pos_tmp = (QMouseEvent.pos().x(), QMouseEvent.pos().y())
        # pos_tmp添加到self.pos_xy中
        self.pos_xy.append(pos_tmp)
        self.update()

    def paintEvent(self, QPaintEvent):
        painter=QPainter()
        painter.begin(self)
        painter.setPen(Qt.blue)
        size=self.size()
        for pos_tmp in self.pos_xy:
            painter.fillRect(pos_tmp[0]-20, pos_tmp[1]-20,40 ,40 ,Qt.blue)
        for i in range(11):
            y=50*i
            painter.drawLine(0,y,500,y)
        for i in range(11):
            x=50*i
            painter.drawLine(x,0,x,500)
        # for i in range(1000):
        #     x=100*(-1+2.0*i/1000)+size.width()/2.0
        #     y=-50*math.sin((x-size.width()/2.0)*math.pi/50)+size.height()/2.0
        #     painter.drawPoint(x,y)

        painter.end()

if __name__=='__main__':
    #创建QApplication类的实例
    app=QApplication(sys.argv)
    main=Drawpoints()
    main.show()
    sys.exit(app.exec_())