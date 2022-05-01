# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(964, 650)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(3, 3, 901, 600))
        self.all = QGridLayout(self.layoutWidget)
        self.all.setObjectName(u"all")
        self.all.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.all.setContentsMargins(0, 0, 0, 0)
        self.num = QGridLayout()
        self.num.setObjectName(u"num")
        self.num.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.n032 = QLineEdit(self.layoutWidget)
        self.n032.setObjectName(u"n032")
        self.n032.setMinimumSize(QSize(60, 60))
        self.n032.setMaximumSize(QSize(60, 60))
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font.setPointSize(20)
        self.n032.setFont(font)
        self.n032.setFocusPolicy(Qt.WheelFocus)
        self.n032.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n032, 2, 1, 1, 1)

        self.n031 = QLineEdit(self.layoutWidget)
        self.n031.setObjectName(u"n031")
        self.n031.setMinimumSize(QSize(60, 60))
        self.n031.setMaximumSize(QSize(60, 60))
        self.n031.setFont(font)
        self.n031.setFocusPolicy(Qt.WheelFocus)
        self.n031.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n031, 2, 0, 1, 1)

        self.n063 = QLineEdit(self.layoutWidget)
        self.n063.setObjectName(u"n063")
        self.n063.setMinimumSize(QSize(60, 60))
        self.n063.setMaximumSize(QSize(60, 60))
        self.n063.setFont(font)
        self.n063.setFocusPolicy(Qt.WheelFocus)
        self.n063.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n063, 5, 2, 1, 1)

        self.n024 = QLineEdit(self.layoutWidget)
        self.n024.setObjectName(u"n024")
        self.n024.setMinimumSize(QSize(60, 60))
        self.n024.setMaximumSize(QSize(60, 60))
        self.n024.setFont(font)
        self.n024.setFocusPolicy(Qt.WheelFocus)
        self.n024.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n024, 1, 3, 1, 1)

        self.n093 = QLineEdit(self.layoutWidget)
        self.n093.setObjectName(u"n093")
        self.n093.setMinimumSize(QSize(60, 60))
        self.n093.setMaximumSize(QSize(60, 60))
        self.n093.setFont(font)
        self.n093.setFocusPolicy(Qt.WheelFocus)
        self.n093.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n093, 8, 2, 1, 1)

        self.n013 = QLineEdit(self.layoutWidget)
        self.n013.setObjectName(u"n013")
        self.n013.setMinimumSize(QSize(60, 60))
        self.n013.setMaximumSize(QSize(60, 60))
        self.n013.setFont(font)
        self.n013.setFocusPolicy(Qt.WheelFocus)
        self.n013.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n013, 0, 2, 1, 1)

        self.n077 = QLineEdit(self.layoutWidget)
        self.n077.setObjectName(u"n077")
        self.n077.setMinimumSize(QSize(60, 60))
        self.n077.setMaximumSize(QSize(60, 60))
        self.n077.setFont(font)
        self.n077.setFocusPolicy(Qt.WheelFocus)
        self.n077.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n077, 6, 6, 1, 1)

        self.n076 = QLineEdit(self.layoutWidget)
        self.n076.setObjectName(u"n076")
        self.n076.setMinimumSize(QSize(60, 60))
        self.n076.setMaximumSize(QSize(60, 60))
        self.n076.setFont(font)
        self.n076.setFocusPolicy(Qt.WheelFocus)
        self.n076.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n076, 6, 5, 1, 1)

        self.n096 = QLineEdit(self.layoutWidget)
        self.n096.setObjectName(u"n096")
        self.n096.setMinimumSize(QSize(60, 60))
        self.n096.setMaximumSize(QSize(60, 60))
        self.n096.setFont(font)
        self.n096.setFocusPolicy(Qt.WheelFocus)
        self.n096.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n096, 8, 5, 1, 1)

        self.n016 = QLineEdit(self.layoutWidget)
        self.n016.setObjectName(u"n016")
        self.n016.setMinimumSize(QSize(60, 60))
        self.n016.setMaximumSize(QSize(60, 60))
        self.n016.setFont(font)
        self.n016.setFocusPolicy(Qt.WheelFocus)
        self.n016.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n016, 0, 5, 1, 1)

        self.n092 = QLineEdit(self.layoutWidget)
        self.n092.setObjectName(u"n092")
        self.n092.setMinimumSize(QSize(60, 60))
        self.n092.setMaximumSize(QSize(60, 60))
        self.n092.setFont(font)
        self.n092.setFocusPolicy(Qt.WheelFocus)
        self.n092.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n092, 8, 1, 1, 1)

        self.n084 = QLineEdit(self.layoutWidget)
        self.n084.setObjectName(u"n084")
        self.n084.setMinimumSize(QSize(60, 60))
        self.n084.setMaximumSize(QSize(60, 60))
        self.n084.setFont(font)
        self.n084.setFocusPolicy(Qt.WheelFocus)
        self.n084.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n084, 7, 3, 1, 1)

        self.n053 = QLineEdit(self.layoutWidget)
        self.n053.setObjectName(u"n053")
        self.n053.setMinimumSize(QSize(60, 60))
        self.n053.setMaximumSize(QSize(60, 60))
        self.n053.setFont(font)
        self.n053.setFocusPolicy(Qt.WheelFocus)
        self.n053.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n053, 4, 2, 1, 1)

        self.n086 = QLineEdit(self.layoutWidget)
        self.n086.setObjectName(u"n086")
        self.n086.setMinimumSize(QSize(60, 60))
        self.n086.setMaximumSize(QSize(60, 60))
        self.n086.setFont(font)
        self.n086.setFocusPolicy(Qt.WheelFocus)
        self.n086.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n086, 7, 5, 1, 1)

        self.n099 = QLineEdit(self.layoutWidget)
        self.n099.setObjectName(u"n099")
        self.n099.setMinimumSize(QSize(60, 60))
        self.n099.setMaximumSize(QSize(60, 60))
        self.n099.setFont(font)
        self.n099.setFocusPolicy(Qt.WheelFocus)
        self.n099.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n099, 8, 8, 1, 1)

        self.n058 = QLineEdit(self.layoutWidget)
        self.n058.setObjectName(u"n058")
        self.n058.setMinimumSize(QSize(60, 60))
        self.n058.setMaximumSize(QSize(60, 60))
        self.n058.setFont(font)
        self.n058.setFocusPolicy(Qt.WheelFocus)
        self.n058.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n058, 4, 7, 1, 1)

        self.n029 = QLineEdit(self.layoutWidget)
        self.n029.setObjectName(u"n029")
        self.n029.setMinimumSize(QSize(60, 60))
        self.n029.setMaximumSize(QSize(60, 60))
        self.n029.setFont(font)
        self.n029.setFocusPolicy(Qt.WheelFocus)
        self.n029.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n029, 1, 8, 1, 1)

        self.n069 = QLineEdit(self.layoutWidget)
        self.n069.setObjectName(u"n069")
        self.n069.setMinimumSize(QSize(60, 60))
        self.n069.setMaximumSize(QSize(60, 60))
        self.n069.setFont(font)
        self.n069.setFocusPolicy(Qt.WheelFocus)
        self.n069.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n069, 5, 8, 1, 1)

        self.n036 = QLineEdit(self.layoutWidget)
        self.n036.setObjectName(u"n036")
        self.n036.setMinimumSize(QSize(60, 60))
        self.n036.setMaximumSize(QSize(60, 60))
        self.n036.setFont(font)
        self.n036.setFocusPolicy(Qt.WheelFocus)
        self.n036.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n036, 2, 5, 1, 1)

        self.n066 = QLineEdit(self.layoutWidget)
        self.n066.setObjectName(u"n066")
        self.n066.setMinimumSize(QSize(60, 60))
        self.n066.setMaximumSize(QSize(60, 60))
        self.n066.setFont(font)
        self.n066.setFocusPolicy(Qt.WheelFocus)
        self.n066.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n066, 5, 5, 1, 1)

        self.n081 = QLineEdit(self.layoutWidget)
        self.n081.setObjectName(u"n081")
        self.n081.setMinimumSize(QSize(60, 60))
        self.n081.setMaximumSize(QSize(60, 60))
        self.n081.setFont(font)
        self.n081.setFocusPolicy(Qt.WheelFocus)
        self.n081.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n081, 7, 0, 1, 1)

        self.n039 = QLineEdit(self.layoutWidget)
        self.n039.setObjectName(u"n039")
        self.n039.setMinimumSize(QSize(60, 60))
        self.n039.setMaximumSize(QSize(60, 60))
        self.n039.setFont(font)
        self.n039.setFocusPolicy(Qt.WheelFocus)
        self.n039.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n039, 2, 8, 1, 1)

        self.n025 = QLineEdit(self.layoutWidget)
        self.n025.setObjectName(u"n025")
        self.n025.setMinimumSize(QSize(60, 60))
        self.n025.setMaximumSize(QSize(60, 60))
        self.n025.setFont(font)
        self.n025.setFocusPolicy(Qt.WheelFocus)
        self.n025.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n025, 1, 4, 1, 1)

        self.n074 = QLineEdit(self.layoutWidget)
        self.n074.setObjectName(u"n074")
        self.n074.setMinimumSize(QSize(60, 60))
        self.n074.setMaximumSize(QSize(60, 60))
        self.n074.setFont(font)
        self.n074.setFocusPolicy(Qt.WheelFocus)
        self.n074.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n074, 6, 3, 1, 1)

        self.n051 = QLineEdit(self.layoutWidget)
        self.n051.setObjectName(u"n051")
        self.n051.setMinimumSize(QSize(60, 60))
        self.n051.setMaximumSize(QSize(60, 60))
        self.n051.setFont(font)
        self.n051.setFocusPolicy(Qt.WheelFocus)
        self.n051.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n051, 4, 0, 1, 1)

        self.n018 = QLineEdit(self.layoutWidget)
        self.n018.setObjectName(u"n018")
        self.n018.setMinimumSize(QSize(60, 60))
        self.n018.setMaximumSize(QSize(60, 60))
        self.n018.setFont(font)
        self.n018.setFocusPolicy(Qt.WheelFocus)
        self.n018.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n018, 0, 7, 1, 1)

        self.n011 = QLineEdit(self.layoutWidget)
        self.n011.setObjectName(u"n011")
        self.n011.setMinimumSize(QSize(60, 60))
        self.n011.setMaximumSize(QSize(60, 60))
        self.n011.setFont(font)
        self.n011.setFocusPolicy(Qt.WheelFocus)
        self.n011.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n011, 0, 0, 1, 1)

        self.n064 = QLineEdit(self.layoutWidget)
        self.n064.setObjectName(u"n064")
        self.n064.setMinimumSize(QSize(60, 60))
        self.n064.setMaximumSize(QSize(60, 60))
        self.n064.setFont(font)
        self.n064.setFocusPolicy(Qt.WheelFocus)
        self.n064.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n064, 5, 3, 1, 1)

        self.n033 = QLineEdit(self.layoutWidget)
        self.n033.setObjectName(u"n033")
        self.n033.setMinimumSize(QSize(60, 60))
        self.n033.setMaximumSize(QSize(60, 60))
        self.n033.setFont(font)
        self.n033.setFocusPolicy(Qt.WheelFocus)
        self.n033.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n033, 2, 2, 1, 1)

        self.n042 = QLineEdit(self.layoutWidget)
        self.n042.setObjectName(u"n042")
        self.n042.setMinimumSize(QSize(60, 60))
        self.n042.setMaximumSize(QSize(60, 60))
        self.n042.setFont(font)
        self.n042.setFocusPolicy(Qt.WheelFocus)
        self.n042.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n042, 3, 1, 1, 1)

        self.n091 = QLineEdit(self.layoutWidget)
        self.n091.setObjectName(u"n091")
        self.n091.setMinimumSize(QSize(60, 60))
        self.n091.setMaximumSize(QSize(60, 60))
        self.n091.setFont(font)
        self.n091.setFocusPolicy(Qt.WheelFocus)
        self.n091.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n091, 8, 0, 1, 1)

        self.n035 = QLineEdit(self.layoutWidget)
        self.n035.setObjectName(u"n035")
        self.n035.setMinimumSize(QSize(60, 60))
        self.n035.setMaximumSize(QSize(60, 60))
        self.n035.setFont(font)
        self.n035.setFocusPolicy(Qt.WheelFocus)
        self.n035.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n035, 2, 4, 1, 1)

        self.n019 = QLineEdit(self.layoutWidget)
        self.n019.setObjectName(u"n019")
        self.n019.setMinimumSize(QSize(60, 60))
        self.n019.setMaximumSize(QSize(60, 60))
        self.n019.setFont(font)
        self.n019.setFocusPolicy(Qt.WheelFocus)
        self.n019.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n019, 0, 8, 1, 1)

        self.n089 = QLineEdit(self.layoutWidget)
        self.n089.setObjectName(u"n089")
        self.n089.setMinimumSize(QSize(60, 60))
        self.n089.setMaximumSize(QSize(60, 60))
        self.n089.setFont(font)
        self.n089.setFocusPolicy(Qt.WheelFocus)
        self.n089.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n089, 7, 8, 1, 1)

        self.n048 = QLineEdit(self.layoutWidget)
        self.n048.setObjectName(u"n048")
        self.n048.setMinimumSize(QSize(60, 60))
        self.n048.setMaximumSize(QSize(60, 60))
        self.n048.setFont(font)
        self.n048.setFocusPolicy(Qt.WheelFocus)
        self.n048.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n048, 3, 7, 1, 1)

        self.n085 = QLineEdit(self.layoutWidget)
        self.n085.setObjectName(u"n085")
        self.n085.setMinimumSize(QSize(60, 60))
        self.n085.setMaximumSize(QSize(60, 60))
        self.n085.setFont(font)
        self.n085.setFocusPolicy(Qt.WheelFocus)
        self.n085.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n085, 7, 4, 1, 1)

        self.n075 = QLineEdit(self.layoutWidget)
        self.n075.setObjectName(u"n075")
        self.n075.setMinimumSize(QSize(60, 60))
        self.n075.setMaximumSize(QSize(60, 60))
        self.n075.setFont(font)
        self.n075.setFocusPolicy(Qt.WheelFocus)
        self.n075.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n075, 6, 4, 1, 1)

        self.n034 = QLineEdit(self.layoutWidget)
        self.n034.setObjectName(u"n034")
        self.n034.setMinimumSize(QSize(60, 60))
        self.n034.setMaximumSize(QSize(60, 60))
        self.n034.setFont(font)
        self.n034.setFocusPolicy(Qt.WheelFocus)
        self.n034.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n034, 2, 3, 1, 1)

        self.n047 = QLineEdit(self.layoutWidget)
        self.n047.setObjectName(u"n047")
        self.n047.setMinimumSize(QSize(60, 60))
        self.n047.setMaximumSize(QSize(60, 60))
        self.n047.setFont(font)
        self.n047.setFocusPolicy(Qt.WheelFocus)
        self.n047.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n047, 3, 6, 1, 1)

        self.n097 = QLineEdit(self.layoutWidget)
        self.n097.setObjectName(u"n097")
        self.n097.setMinimumSize(QSize(60, 60))
        self.n097.setMaximumSize(QSize(60, 60))
        self.n097.setFont(font)
        self.n097.setFocusPolicy(Qt.WheelFocus)
        self.n097.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n097, 8, 6, 1, 1)

        self.n055 = QLineEdit(self.layoutWidget)
        self.n055.setObjectName(u"n055")
        self.n055.setMinimumSize(QSize(60, 60))
        self.n055.setMaximumSize(QSize(60, 60))
        self.n055.setFont(font)
        self.n055.setFocusPolicy(Qt.WheelFocus)
        self.n055.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n055, 4, 4, 1, 1)

        self.n072 = QLineEdit(self.layoutWidget)
        self.n072.setObjectName(u"n072")
        self.n072.setMinimumSize(QSize(60, 60))
        self.n072.setMaximumSize(QSize(60, 60))
        self.n072.setFont(font)
        self.n072.setFocusPolicy(Qt.WheelFocus)
        self.n072.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n072, 6, 1, 1, 1)

        self.n068 = QLineEdit(self.layoutWidget)
        self.n068.setObjectName(u"n068")
        self.n068.setMinimumSize(QSize(60, 60))
        self.n068.setMaximumSize(QSize(60, 60))
        self.n068.setFont(font)
        self.n068.setFocusPolicy(Qt.WheelFocus)
        self.n068.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n068, 5, 7, 1, 1)

        self.n054 = QLineEdit(self.layoutWidget)
        self.n054.setObjectName(u"n054")
        self.n054.setMinimumSize(QSize(60, 60))
        self.n054.setMaximumSize(QSize(60, 60))
        self.n054.setFont(font)
        self.n054.setFocusPolicy(Qt.WheelFocus)
        self.n054.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n054, 4, 3, 1, 1)

        self.n038 = QLineEdit(self.layoutWidget)
        self.n038.setObjectName(u"n038")
        self.n038.setMinimumSize(QSize(60, 60))
        self.n038.setMaximumSize(QSize(60, 60))
        self.n038.setFont(font)
        self.n038.setFocusPolicy(Qt.WheelFocus)
        self.n038.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n038, 2, 7, 1, 1)

        self.n056 = QLineEdit(self.layoutWidget)
        self.n056.setObjectName(u"n056")
        self.n056.setMinimumSize(QSize(60, 60))
        self.n056.setMaximumSize(QSize(60, 60))
        self.n056.setFont(font)
        self.n056.setFocusPolicy(Qt.WheelFocus)
        self.n056.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n056, 4, 5, 1, 1)

        self.n037 = QLineEdit(self.layoutWidget)
        self.n037.setObjectName(u"n037")
        self.n037.setMinimumSize(QSize(60, 60))
        self.n037.setMaximumSize(QSize(60, 60))
        self.n037.setFont(font)
        self.n037.setFocusPolicy(Qt.WheelFocus)
        self.n037.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n037, 2, 6, 1, 1)

        self.n061 = QLineEdit(self.layoutWidget)
        self.n061.setObjectName(u"n061")
        self.n061.setMinimumSize(QSize(60, 60))
        self.n061.setMaximumSize(QSize(60, 60))
        self.n061.setFont(font)
        self.n061.setFocusPolicy(Qt.WheelFocus)
        self.n061.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n061, 5, 0, 1, 1)

        self.n065 = QLineEdit(self.layoutWidget)
        self.n065.setObjectName(u"n065")
        self.n065.setMinimumSize(QSize(60, 60))
        self.n065.setMaximumSize(QSize(60, 60))
        self.n065.setFont(font)
        self.n065.setFocusPolicy(Qt.WheelFocus)
        self.n065.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n065, 5, 4, 1, 1)

        self.n059 = QLineEdit(self.layoutWidget)
        self.n059.setObjectName(u"n059")
        self.n059.setMinimumSize(QSize(60, 60))
        self.n059.setMaximumSize(QSize(60, 60))
        self.n059.setFont(font)
        self.n059.setFocusPolicy(Qt.WheelFocus)
        self.n059.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n059, 4, 8, 1, 1)

        self.n087 = QLineEdit(self.layoutWidget)
        self.n087.setObjectName(u"n087")
        self.n087.setMinimumSize(QSize(60, 60))
        self.n087.setMaximumSize(QSize(60, 60))
        self.n087.setFont(font)
        self.n087.setFocusPolicy(Qt.WheelFocus)
        self.n087.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n087, 7, 6, 1, 1)

        self.n044 = QLineEdit(self.layoutWidget)
        self.n044.setObjectName(u"n044")
        self.n044.setMinimumSize(QSize(60, 60))
        self.n044.setMaximumSize(QSize(60, 60))
        self.n044.setFont(font)
        self.n044.setFocusPolicy(Qt.WheelFocus)
        self.n044.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n044, 3, 3, 1, 1)

        self.n082 = QLineEdit(self.layoutWidget)
        self.n082.setObjectName(u"n082")
        self.n082.setMinimumSize(QSize(60, 60))
        self.n082.setMaximumSize(QSize(60, 60))
        self.n082.setFont(font)
        self.n082.setFocusPolicy(Qt.WheelFocus)
        self.n082.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n082, 7, 1, 1, 1)

        self.n012 = QLineEdit(self.layoutWidget)
        self.n012.setObjectName(u"n012")
        self.n012.setMinimumSize(QSize(60, 60))
        self.n012.setMaximumSize(QSize(60, 60))
        self.n012.setFont(font)
        self.n012.setFocusPolicy(Qt.WheelFocus)
        self.n012.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n012, 0, 1, 1, 1)

        self.n062 = QLineEdit(self.layoutWidget)
        self.n062.setObjectName(u"n062")
        self.n062.setMinimumSize(QSize(60, 60))
        self.n062.setMaximumSize(QSize(60, 60))
        self.n062.setFont(font)
        self.n062.setFocusPolicy(Qt.WheelFocus)
        self.n062.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n062, 5, 1, 1, 1)

        self.n067 = QLineEdit(self.layoutWidget)
        self.n067.setObjectName(u"n067")
        self.n067.setMinimumSize(QSize(60, 60))
        self.n067.setMaximumSize(QSize(60, 60))
        self.n067.setFont(font)
        self.n067.setFocusPolicy(Qt.WheelFocus)
        self.n067.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n067, 5, 6, 1, 1)

        self.n022 = QLineEdit(self.layoutWidget)
        self.n022.setObjectName(u"n022")
        self.n022.setMinimumSize(QSize(60, 60))
        self.n022.setMaximumSize(QSize(60, 60))
        self.n022.setFont(font)
        self.n022.setFocusPolicy(Qt.WheelFocus)
        self.n022.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n022, 1, 1, 1, 1)

        self.n017 = QLineEdit(self.layoutWidget)
        self.n017.setObjectName(u"n017")
        self.n017.setMinimumSize(QSize(60, 60))
        self.n017.setMaximumSize(QSize(60, 60))
        self.n017.setFont(font)
        self.n017.setFocusPolicy(Qt.WheelFocus)
        self.n017.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n017, 0, 6, 1, 1)

        self.n045 = QLineEdit(self.layoutWidget)
        self.n045.setObjectName(u"n045")
        self.n045.setMinimumSize(QSize(60, 60))
        self.n045.setMaximumSize(QSize(60, 60))
        self.n045.setFont(font)
        self.n045.setFocusPolicy(Qt.WheelFocus)
        self.n045.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n045, 3, 4, 1, 1)

        self.n073 = QLineEdit(self.layoutWidget)
        self.n073.setObjectName(u"n073")
        self.n073.setMinimumSize(QSize(60, 60))
        self.n073.setMaximumSize(QSize(60, 60))
        self.n073.setFont(font)
        self.n073.setFocusPolicy(Qt.WheelFocus)
        self.n073.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n073, 6, 2, 1, 1)

        self.n049 = QLineEdit(self.layoutWidget)
        self.n049.setObjectName(u"n049")
        self.n049.setMinimumSize(QSize(60, 60))
        self.n049.setMaximumSize(QSize(60, 60))
        self.n049.setFont(font)
        self.n049.setFocusPolicy(Qt.WheelFocus)
        self.n049.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n049, 3, 8, 1, 1)

        self.n094 = QLineEdit(self.layoutWidget)
        self.n094.setObjectName(u"n094")
        self.n094.setMinimumSize(QSize(60, 60))
        self.n094.setMaximumSize(QSize(60, 60))
        self.n094.setFont(font)
        self.n094.setFocusPolicy(Qt.WheelFocus)
        self.n094.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n094, 8, 3, 1, 1)

        self.n057 = QLineEdit(self.layoutWidget)
        self.n057.setObjectName(u"n057")
        self.n057.setMinimumSize(QSize(60, 60))
        self.n057.setMaximumSize(QSize(60, 60))
        self.n057.setFont(font)
        self.n057.setFocusPolicy(Qt.WheelFocus)
        self.n057.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n057, 4, 6, 1, 1)

        self.n046 = QLineEdit(self.layoutWidget)
        self.n046.setObjectName(u"n046")
        self.n046.setMinimumSize(QSize(60, 60))
        self.n046.setMaximumSize(QSize(60, 60))
        self.n046.setFont(font)
        self.n046.setFocusPolicy(Qt.WheelFocus)
        self.n046.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n046, 3, 5, 1, 1)

        self.n043 = QLineEdit(self.layoutWidget)
        self.n043.setObjectName(u"n043")
        self.n043.setMinimumSize(QSize(60, 60))
        self.n043.setMaximumSize(QSize(60, 60))
        self.n043.setFont(font)
        self.n043.setFocusPolicy(Qt.WheelFocus)
        self.n043.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n043, 3, 2, 1, 1)

        self.n078 = QLineEdit(self.layoutWidget)
        self.n078.setObjectName(u"n078")
        self.n078.setMinimumSize(QSize(60, 60))
        self.n078.setMaximumSize(QSize(60, 60))
        self.n078.setFont(font)
        self.n078.setFocusPolicy(Qt.WheelFocus)
        self.n078.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n078, 6, 7, 1, 1)

        self.n071 = QLineEdit(self.layoutWidget)
        self.n071.setObjectName(u"n071")
        self.n071.setMinimumSize(QSize(60, 60))
        self.n071.setMaximumSize(QSize(60, 60))
        self.n071.setFont(font)
        self.n071.setFocusPolicy(Qt.WheelFocus)
        self.n071.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n071, 6, 0, 1, 1)

        self.n021 = QLineEdit(self.layoutWidget)
        self.n021.setObjectName(u"n021")
        self.n021.setMinimumSize(QSize(60, 60))
        self.n021.setMaximumSize(QSize(60, 60))
        self.n021.setFont(font)
        self.n021.setFocusPolicy(Qt.WheelFocus)
        self.n021.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n021, 1, 0, 1, 1)

        self.n027 = QLineEdit(self.layoutWidget)
        self.n027.setObjectName(u"n027")
        self.n027.setMinimumSize(QSize(60, 60))
        self.n027.setMaximumSize(QSize(60, 60))
        self.n027.setFont(font)
        self.n027.setFocusPolicy(Qt.WheelFocus)
        self.n027.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n027, 1, 6, 1, 1)

        self.n098 = QLineEdit(self.layoutWidget)
        self.n098.setObjectName(u"n098")
        self.n098.setMinimumSize(QSize(60, 60))
        self.n098.setMaximumSize(QSize(60, 60))
        self.n098.setFont(font)
        self.n098.setFocusPolicy(Qt.WheelFocus)
        self.n098.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n098, 8, 7, 1, 1)

        self.n041 = QLineEdit(self.layoutWidget)
        self.n041.setObjectName(u"n041")
        self.n041.setMinimumSize(QSize(60, 60))
        self.n041.setMaximumSize(QSize(60, 60))
        self.n041.setFont(font)
        self.n041.setFocusPolicy(Qt.WheelFocus)
        self.n041.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n041, 3, 0, 1, 1)

        self.n083 = QLineEdit(self.layoutWidget)
        self.n083.setObjectName(u"n083")
        self.n083.setMinimumSize(QSize(60, 60))
        self.n083.setMaximumSize(QSize(60, 60))
        self.n083.setFont(font)
        self.n083.setFocusPolicy(Qt.WheelFocus)
        self.n083.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n083, 7, 2, 1, 1)

        self.n014 = QLineEdit(self.layoutWidget)
        self.n014.setObjectName(u"n014")
        self.n014.setMinimumSize(QSize(60, 60))
        self.n014.setMaximumSize(QSize(60, 60))
        self.n014.setFont(font)
        self.n014.setFocusPolicy(Qt.WheelFocus)
        self.n014.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n014, 0, 3, 1, 1)

        self.n015 = QLineEdit(self.layoutWidget)
        self.n015.setObjectName(u"n015")
        self.n015.setMinimumSize(QSize(60, 60))
        self.n015.setMaximumSize(QSize(60, 60))
        self.n015.setFont(font)
        self.n015.setFocusPolicy(Qt.WheelFocus)
        self.n015.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n015, 0, 4, 1, 1)

        self.n088 = QLineEdit(self.layoutWidget)
        self.n088.setObjectName(u"n088")
        self.n088.setMinimumSize(QSize(60, 60))
        self.n088.setMaximumSize(QSize(60, 60))
        self.n088.setFont(font)
        self.n088.setFocusPolicy(Qt.WheelFocus)
        self.n088.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n088, 7, 7, 1, 1)

        self.n023 = QLineEdit(self.layoutWidget)
        self.n023.setObjectName(u"n023")
        self.n023.setMinimumSize(QSize(60, 60))
        self.n023.setMaximumSize(QSize(60, 60))
        self.n023.setFont(font)
        self.n023.setFocusPolicy(Qt.WheelFocus)
        self.n023.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n023, 1, 2, 1, 1)

        self.n079 = QLineEdit(self.layoutWidget)
        self.n079.setObjectName(u"n079")
        self.n079.setMinimumSize(QSize(60, 60))
        self.n079.setMaximumSize(QSize(60, 60))
        self.n079.setFont(font)
        self.n079.setFocusPolicy(Qt.WheelFocus)
        self.n079.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n079, 6, 8, 1, 1)

        self.n095 = QLineEdit(self.layoutWidget)
        self.n095.setObjectName(u"n095")
        self.n095.setMinimumSize(QSize(60, 60))
        self.n095.setMaximumSize(QSize(60, 60))
        self.n095.setFont(font)
        self.n095.setFocusPolicy(Qt.WheelFocus)
        self.n095.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n095, 8, 4, 1, 1)

        self.n052 = QLineEdit(self.layoutWidget)
        self.n052.setObjectName(u"n052")
        self.n052.setMinimumSize(QSize(60, 60))
        self.n052.setMaximumSize(QSize(60, 60))
        self.n052.setFont(font)
        self.n052.setFocusPolicy(Qt.WheelFocus)
        self.n052.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n052, 4, 1, 1, 1)

        self.n028 = QLineEdit(self.layoutWidget)
        self.n028.setObjectName(u"n028")
        self.n028.setMinimumSize(QSize(60, 60))
        self.n028.setMaximumSize(QSize(60, 60))
        self.n028.setFont(font)
        self.n028.setFocusPolicy(Qt.WheelFocus)
        self.n028.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n028, 1, 7, 1, 1)

        self.n026 = QLineEdit(self.layoutWidget)
        self.n026.setObjectName(u"n026")
        self.n026.setMinimumSize(QSize(60, 60))
        self.n026.setMaximumSize(QSize(60, 60))
        self.n026.setFont(font)
        self.n026.setFocusPolicy(Qt.WheelFocus)
        self.n026.setAlignment(Qt.AlignCenter)

        self.num.addWidget(self.n026, 1, 5, 1, 1)


        self.all.addLayout(self.num, 0, 0, 1, 1)

        self.con = QGridLayout()
        self.con.setObjectName(u"con")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.word_dif = QLineEdit(self.layoutWidget)
        self.word_dif.setObjectName(u"word_dif")
        self.word_dif.setMinimumSize(QSize(100, 60))
        self.word_dif.setMaximumSize(QSize(100, 60))
        self.word_dif.setFont(font)

        self.horizontalLayout.addWidget(self.word_dif)

        self.bt_set_dif = QToolButton(self.layoutWidget)
        self.bt_set_dif.setObjectName(u"bt_set_dif")
        self.bt_set_dif.setMinimumSize(QSize(100, 60))
        self.bt_set_dif.setMaximumSize(QSize(100, 60))
        font1 = QFont()
        font1.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font1.setPointSize(10)
        self.bt_set_dif.setFont(font1)

        self.horizontalLayout.addWidget(self.bt_set_dif)


        self.con.addLayout(self.horizontalLayout, 3, 1, 1, 1)

        self.bt_start = QPushButton(self.layoutWidget)
        self.bt_start.setObjectName(u"bt_start")
        self.bt_start.setMinimumSize(QSize(93, 60))
        self.bt_start.setFont(font1)

        self.con.addWidget(self.bt_start, 2, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.con.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.con.addItem(self.verticalSpacer, 4, 1, 1, 1)

        self.lcd = QLCDNumber(self.layoutWidget)
        self.lcd.setObjectName(u"lcd")
        self.lcd.setMinimumSize(QSize(0, 60))
        self.lcd.setMaximumSize(QSize(16777215, 60))

        self.con.addWidget(self.lcd, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.con.addItem(self.horizontalSpacer, 2, 0, 1, 1)


        self.all.addLayout(self.con, 0, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.n069.setText("")
        self.n059.setText("")
        self.word_dif.setText(QCoreApplication.translate("Form", u"1", None))
        self.bt_set_dif.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e\u96be\u5ea6", None))
        self.bt_start.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
    # retranslateUi

