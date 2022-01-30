# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mazeUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5.QtCore import*
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from a import AStar,Point,Map

class Ui_Form(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setObjectName("A*迷宫")
        self.resize(650, 530)
        self.number=0

        self.drawUI = DrawUI(self)
        self.drawUI.setObjectName("drawUI")
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.drawUI)
        self.widget = QWidget(self)
        self.widget.setGeometry(QRect(530, 30, 120, 411))
        self.widget.setObjectName("widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.setObstacleBtn = QPushButton(self.widget)
        self.setObstacleBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.setObstacleBtn.setObjectName("setObstacleBtn")
        self.verticalLayout.addWidget(self.setObstacleBtn)
        self.setStartBtn = QPushButton(self.widget)
        self.setStartBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.setStartBtn.setObjectName("setStartBtn")
        self.verticalLayout.addWidget(self.setStartBtn)
        self.setEndBtn = QPushButton(self.widget)
        self.setEndBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.setEndBtn.setObjectName("setEndBtn")
        self.verticalLayout.addWidget(self.setEndBtn)
        self.onceProgressBtn = QPushButton(self.widget)
        self.onceProgressBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.onceProgressBtn.setObjectName("onceProgressBtn")
        self.verticalLayout.addWidget(self.onceProgressBtn)
        self.finishAllBtn = QPushButton(self.widget)
        self.finishAllBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.finishAllBtn.setObjectName("finishAllBtn")
        self.verticalLayout.addWidget(self.finishAllBtn)
        self.reset = QPushButton(self.widget)
        self.reset.setCursor(QCursor(Qt.PointingHandCursor))
        self.reset.setObjectName("reset")
        self.verticalLayout.addWidget(self.reset)
        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)
    #     定义按钮信号
        self.setObstacleBtn.clicked.connect(self.addObstacle)
        self.setStartBtn.clicked.connect(self.addStart)
        self.setEndBtn.clicked.connect(self.setEnd)
        self.finishAllBtn.clicked.connect(self.startAll)
        self.onceProgressBtn.clicked.connect(self.startOnce)
        self.reset.clicked.connect(self.resetAll)
    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "A*迷宫"))
        self.setObstacleBtn.setText(_translate("Form", "设置障碍物"))
        self.setStartBtn.setText(_translate("Form", "设置起点"))
        self.setEndBtn.setText(_translate("Form", "设置终点"))
        self.onceProgressBtn.setText(_translate("Form", "单步运行"))
        self.finishAllBtn.setText(_translate("Form", "一次运行"))
        self.reset.setText(_translate("Form","重置"))

    # 以下为点击按钮执行的函数
    def addObstacle(self):
        self.drawUI.drawWhat=self.setObstacleBtn.objectName()
        print(self.setObstacleBtn.objectName())
    def addStart(self):
        self.drawUI.drawWhat=self.setStartBtn.objectName()
        print(self.setStartBtn.objectName())
    def setEnd(self):
        self.drawUI.drawWhat=self.setEndBtn.objectName()
        print(self.setEndBtn.objectName())
    def startOnce(self):
        print(self.onceProgressBtn.objectName())
        self.drawUI.drawWhat = self.onceProgressBtn.objectName()
        if(self.number==0):
            # self.drawUI.map.startBool = True
            self.drawUI.a_star = AStar(self.drawUI.map, self.drawUI.start, self.drawUI.end)
            self.number+=1
        open_set,close_set,path=self.drawUI.a_star.RunOnce()
        self.drawUI.open_set =open_set
        self.drawUI.close_set =close_set
        self.drawUI.path=path
        self.drawUI.update()
        if(len(path)>0):
            if (self.drawUI.showFinalMes == False):
                self.drawUI.showFinalMes = True
                mesBox = QMessageBox()
                mesBox.information(self, "提示", "已经找到最短路径", buttons=QMessageBox.Ok)
                mesBox.show()
    # 一次性进行
    def startAll(self):
        self.drawUI.drawWhat = self.finishAllBtn.objectName()
        if(self.drawUI.start!=None and self.drawUI.end!=None):
            self.drawUI.a_star = AStar(self.drawUI.map, self.drawUI.start, self.drawUI.end)
            self.drawUI.a_star.RunAll()
            self.drawUI.path = self.drawUI.a_star.path
            self.drawUI.open_set=self.drawUI.a_star.open_set.open_set
            self.drawUI.close_set=self.drawUI.a_star.close_set
            # 重绘
            self.drawUI.update()
            if (len(self.drawUI.path) > 0):
                if (self.drawUI.showFinalMes == False):
                    self.drawUI.showFinalMes = True
                    mesBox = QMessageBox()
                    mesBox.information(self, "提示", "已经找到最短路径", buttons=QMessageBox.Ok)
                    mesBox.show()
    # 重置函数
    def resetAll(self):
        self.drawUI.path=[]
        self.drawUI.close_set=[]
        self.drawUI.open_set=[]
        self.drawUI.start=None
        self.drawUI.end=None
        self.drawUI.obstacle=[]
        self.drawUI.drawWhat=""
        self.drawUI.a_star=None
        self.drawUI.startBool=False
        self.drawUI.endBool=False
        self.drawUI.startAll=False
        self.drawUI.update()
        self.number = 0
        self.drawUI.a_star=None
        self.drawUI.map.obstacle_points=[]
        self.drawUI.showFinalMes = False
class DrawUI(QWidget):
    def __init__(self,parent=Ui_Form):
        super(DrawUI,self).__init__()
        self.resize(650,530)
        self.obstacle = []
        self.start=None
        self.end=None
        self.mapBlock=[]
        self.startBool=False
        self.endBool=False
        self.drawWhat=""
        self.initBlock()
        self.map=Map()
        self.startAll=False
        self.open_set=[]
        self.close_set=[]
        self.path=[]
        self.a_star=None
        self.showFinalMes=False
    def initBlock(self):
        for i in range(11):
            for j in range(11):
                point=Point(i,j)
                self.mapBlock.append(point)
    def mouseReleaseEvent(self, QMouseEvent):
        print(QMouseEvent.x(),QMouseEvent.y())
        if(self.drawWhat=="setObstacleBtn"):
            pos_tmp = Point(int(QMouseEvent.pos().x()/50), int(QMouseEvent.pos().y()/50))
            self.obstacle.append(pos_tmp)
            self.map.obstacle_points.append(pos_tmp)
            self.update()
        if (self.drawWhat == "setStartBtn"):
            if(self.startBool==False):
                # 增加起点
                start = Point(int(QMouseEvent.pos().x()/50), int(QMouseEvent.pos().y()/50))
                start.cost=0
                start.beforeCost=0
                start.afterCost=0
                self.start=start
                self.update()
                self.startBool =True
            else:
        #         提示只能添加一个起点
                print("只能添加一个起点")
                mesBox=QMessageBox()
                mesBox.warning(self,"提示","只能设置一个起点",buttons=QMessageBox.Ok)
                mesBox.show()
        if (self.drawWhat == "setEndBtn"):
            if(self.endBool==False):
                # 增加终点
                end = Point(int(QMouseEvent.pos().x()/50), int(QMouseEvent.pos().y()/50))
                self.end=end
                self.update()
                self.endBool=True
            else:
                #         提示只能添加一个终点
                print("只能添加一个终点")
                mesBox = QMessageBox()
                mesBox.warning(self, "提示", "只能设置一个终点", buttons=QMessageBox.Ok)
                mesBox.show()

    def paintEvent(self, QPaintEvent):
        painter=QPainter()
        # 开始画图
        painter.begin(self)
        painter.setPen(Qt.blue)
        size=self.size()
        # 画障碍物
        for pos_tmp in self.obstacle:
            painter.fillRect(pos_tmp.x*50, pos_tmp.y*50,50 ,50 ,Qt.black)
        # 画起点
        if(self.start!=None):
            painter.fillRect(self.start.x*50, self.start.y*50, 50, 50, Qt.green)
        # 画终点
        if(self.end!=None):
            painter.fillRect(self.end.x*50, self.end.y*50, 50, 50, Qt.red)
        # 画边界
        for i in range(11):
            y=50*i
            painter.drawLine(0,y,500,y)
        for i in range(11):
            x=50*i
            painter.drawLine(x,0,x,500)
        #     画路线
        if(len(self.path)>0):
            for p in self.path[0:-1]:
                if((p!=self.start)and(p!=self.end)):
                    painter.fillRect(p.x*50,p.y*50,50,50,Qt.yellow)
                    beforeCostStr = round(float(p.beforeCost), 1)
                    afterCostStr = round(float(p.afterCost), 1)
                    totalCostStr = round(float(p.cost), 1)
                    painter.setPen(Qt.red)
                    painter.setFont(QFont("SimSun", 8))
                    painter.drawText(p.x * 50 + 3, p.y * 50 + 12, str(beforeCostStr))
                    painter.drawText(p.x * 50 + 3, p.y * 50 + 42, str(afterCostStr))
                    painter.drawText(p.x * 50 + 27, p.y * 50 + 12, str(totalCostStr))
        # 画openset
        if(len(self.open_set)>0):
            for p in self.open_set:
                if ((p not in self.path) and(p!=self.start)and(p!=self.end)):
                    painter.fillRect(p.x*50,p.y*50,50,50,Qt.blue)
                    beforeCostStr = round(float(p.beforeCost), 1)
                    afterCostStr = round(float(p.afterCost), 1)
                    totalCostStr = round(float(p.cost), 1)
                    painter.setPen(Qt.white)
                    painter.setFont(QFont("SimSun", 8))
                    painter.drawText(p.x * 50 + 3, p.y * 50 + 12, str(beforeCostStr))
                    painter.drawText(p.x * 50 + 3, p.y * 50 + 42, str(afterCostStr))
                    painter.drawText(p.x * 50 + 27, p.y * 50 + 12, str(totalCostStr))
        # 画closeset
        if (len(self.close_set) > 0):
            # painter.setBrush(QColor(0, 0, 255, 127))
            for p in self.close_set:
                if((p not in self.path) and(p!=self.start)and(p!=self.end)):
                    painter.fillRect(p.x * 50, p.y * 50, 50, 50, Qt.darkBlue)
                    beforeCostStr=round(float(p.beforeCost),1)
                    afterCostStr=round(float(p.afterCost),1)
                    totalCostStr=round(float(p.cost),1)
                    painter.setPen(Qt.white)
                    painter.setFont(QFont("SimSun", 8))
                    painter.drawText(p.x*50+3,p.y*50+12,str(beforeCostStr))
                    painter.drawText(p.x*50+3,p.y*50+42,str(afterCostStr))
                    painter.drawText(p.x*50+27,p.y*50+12,str(totalCostStr))
        painter.end()

if __name__=='__main__':
    #创建QApplication类的实例
    app=QApplication(sys.argv)
    main=Ui_Form()
    main.show()
    sys.exit(app.exec_())