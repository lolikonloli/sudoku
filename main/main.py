from asyncio.windows_events import NULL
import math

from PySide2.QtWidgets import QApplication, QMessageBox, QStyleFactory, QLCDNumber
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QTimer, QDateTime
import loguru
import numpy as np
from numpy import random
import PySide2
import os

from loguru import logger


dirname = os.path.dirname(PySide2.__file__) 
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path



class Sudoku():
    def __init__(self):
        #从文件中加载UI定义
        qfile_states = QFile("E:\\text\sudoku\\2\sudoku\pyside2\main.ui")
        qfile_states.open(QFile.ReadOnly)
        qfile_states.close()
        self.ui = QUiLoader().load(qfile_states)            #加载窗口

        #属性
        self.num_states = []
        self.difficulty = 1
        self.used_time = 0
        self.check_flag = 0
        

        #绑定
        self.push_button_connects()
        self.ui.bt_start.clicked.connect(self.start_game)
        self.ui.bt_set_dif.clicked.connect(self.set_difficulty)
        self.lcd_init()

        
    #输入数字绑定
    def push_button_connects(self):
        self.ui.n011.textChanged.connect(self.read_nums)
        self.ui.n012.textChanged.connect(self.read_nums)
        self.ui.n013.textChanged.connect(self.read_nums)
        self.ui.n014.textChanged.connect(self.read_nums)
        self.ui.n015.textChanged.connect(self.read_nums)
        self.ui.n016.textChanged.connect(self.read_nums)
        self.ui.n017.textChanged.connect(self.read_nums)
        self.ui.n018.textChanged.connect(self.read_nums)
        self.ui.n019.textChanged.connect(self.read_nums)

        self.ui.n021.textChanged.connect(self.read_nums)
        self.ui.n022.textChanged.connect(self.read_nums)
        self.ui.n023.textChanged.connect(self.read_nums)
        self.ui.n024.textChanged.connect(self.read_nums)
        self.ui.n025.textChanged.connect(self.read_nums)
        self.ui.n026.textChanged.connect(self.read_nums)
        self.ui.n027.textChanged.connect(self.read_nums)
        self.ui.n028.textChanged.connect(self.read_nums)
        self.ui.n029.textChanged.connect(self.read_nums)

        self.ui.n031.textChanged.connect(self.read_nums)
        self.ui.n032.textChanged.connect(self.read_nums)
        self.ui.n033.textChanged.connect(self.read_nums)
        self.ui.n034.textChanged.connect(self.read_nums)
        self.ui.n035.textChanged.connect(self.read_nums)
        self.ui.n036.textChanged.connect(self.read_nums)
        self.ui.n037.textChanged.connect(self.read_nums)
        self.ui.n038.textChanged.connect(self.read_nums)
        self.ui.n039.textChanged.connect(self.read_nums)

        self.ui.n041.textChanged.connect(self.read_nums)
        self.ui.n042.textChanged.connect(self.read_nums)
        self.ui.n043.textChanged.connect(self.read_nums)
        self.ui.n044.textChanged.connect(self.read_nums)
        self.ui.n045.textChanged.connect(self.read_nums)
        self.ui.n046.textChanged.connect(self.read_nums)
        self.ui.n047.textChanged.connect(self.read_nums)
        self.ui.n048.textChanged.connect(self.read_nums)
        self.ui.n049.textChanged.connect(self.read_nums)

        self.ui.n051.textChanged.connect(self.read_nums)
        self.ui.n052.textChanged.connect(self.read_nums)
        self.ui.n053.textChanged.connect(self.read_nums)
        self.ui.n054.textChanged.connect(self.read_nums)
        self.ui.n055.textChanged.connect(self.read_nums)
        self.ui.n056.textChanged.connect(self.read_nums)
        self.ui.n057.textChanged.connect(self.read_nums)
        self.ui.n058.textChanged.connect(self.read_nums)
        self.ui.n059.textChanged.connect(self.read_nums)

        self.ui.n061.textChanged.connect(self.read_nums)
        self.ui.n062.textChanged.connect(self.read_nums)
        self.ui.n063.textChanged.connect(self.read_nums)
        self.ui.n064.textChanged.connect(self.read_nums)
        self.ui.n065.textChanged.connect(self.read_nums)
        self.ui.n066.textChanged.connect(self.read_nums)
        self.ui.n067.textChanged.connect(self.read_nums)
        self.ui.n068.textChanged.connect(self.read_nums)
        self.ui.n069.textChanged.connect(self.read_nums)

        self.ui.n071.textChanged.connect(self.read_nums)
        self.ui.n072.textChanged.connect(self.read_nums)
        self.ui.n073.textChanged.connect(self.read_nums)
        self.ui.n074.textChanged.connect(self.read_nums)
        self.ui.n075.textChanged.connect(self.read_nums)
        self.ui.n076.textChanged.connect(self.read_nums)
        self.ui.n077.textChanged.connect(self.read_nums)
        self.ui.n078.textChanged.connect(self.read_nums)
        self.ui.n079.textChanged.connect(self.read_nums)

        self.ui.n081.textChanged.connect(self.read_nums)
        self.ui.n082.textChanged.connect(self.read_nums)
        self.ui.n083.textChanged.connect(self.read_nums)
        self.ui.n084.textChanged.connect(self.read_nums)
        self.ui.n085.textChanged.connect(self.read_nums)
        self.ui.n086.textChanged.connect(self.read_nums)
        self.ui.n087.textChanged.connect(self.read_nums)
        self.ui.n088.textChanged.connect(self.read_nums)
        self.ui.n089.textChanged.connect(self.read_nums)

        self.ui.n091.textChanged.connect(self.read_nums)
        self.ui.n092.textChanged.connect(self.read_nums)
        self.ui.n093.textChanged.connect(self.read_nums)
        self.ui.n094.textChanged.connect(self.read_nums)
        self.ui.n095.textChanged.connect(self.read_nums)
        self.ui.n096.textChanged.connect(self.read_nums)
        self.ui.n097.textChanged.connect(self.read_nums)
        self.ui.n098.textChanged.connect(self.read_nums)
        self.ui.n099.textChanged.connect(self.read_nums)

    #读取所有数字
    def read_nums_tools(self):
        temp_list = []
        temp_list.append(self.ui.n011.text())
        temp_list.append(self.ui.n012.text())
        temp_list.append(self.ui.n013.text())
        temp_list.append(self.ui.n014.text())
        temp_list.append(self.ui.n015.text())
        temp_list.append(self.ui.n016.text())
        temp_list.append(self.ui.n017.text())
        temp_list.append(self.ui.n018.text())
        temp_list.append(self.ui.n019.text())

        temp_list.append(self.ui.n021.text())
        temp_list.append(self.ui.n022.text())
        temp_list.append(self.ui.n023.text())
        temp_list.append(self.ui.n024.text())
        temp_list.append(self.ui.n025.text())
        temp_list.append(self.ui.n026.text())
        temp_list.append(self.ui.n027.text())
        temp_list.append(self.ui.n028.text())
        temp_list.append(self.ui.n029.text())

        temp_list.append(self.ui.n031.text())
        temp_list.append(self.ui.n032.text())
        temp_list.append(self.ui.n033.text())
        temp_list.append(self.ui.n034.text())
        temp_list.append(self.ui.n035.text())
        temp_list.append(self.ui.n036.text())
        temp_list.append(self.ui.n037.text())
        temp_list.append(self.ui.n038.text())
        temp_list.append(self.ui.n039.text())

        temp_list.append(self.ui.n041.text())
        temp_list.append(self.ui.n042.text())
        temp_list.append(self.ui.n043.text())
        temp_list.append(self.ui.n044.text())
        temp_list.append(self.ui.n045.text())
        temp_list.append(self.ui.n046.text())
        temp_list.append(self.ui.n047.text())
        temp_list.append(self.ui.n048.text())
        temp_list.append(self.ui.n049.text())

        temp_list.append(self.ui.n051.text())
        temp_list.append(self.ui.n052.text())
        temp_list.append(self.ui.n053.text())
        temp_list.append(self.ui.n054.text())
        temp_list.append(self.ui.n055.text())
        temp_list.append(self.ui.n056.text())
        temp_list.append(self.ui.n057.text())
        temp_list.append(self.ui.n058.text())
        temp_list.append(self.ui.n059.text())

        temp_list.append(self.ui.n061.text())
        temp_list.append(self.ui.n062.text())
        temp_list.append(self.ui.n063.text())
        temp_list.append(self.ui.n064.text())
        temp_list.append(self.ui.n065.text())
        temp_list.append(self.ui.n066.text())
        temp_list.append(self.ui.n067.text())
        temp_list.append(self.ui.n068.text())
        temp_list.append(self.ui.n069.text())

        temp_list.append(self.ui.n071.text())
        temp_list.append(self.ui.n072.text())
        temp_list.append(self.ui.n073.text())
        temp_list.append(self.ui.n074.text())
        temp_list.append(self.ui.n075.text())
        temp_list.append(self.ui.n076.text())
        temp_list.append(self.ui.n077.text())
        temp_list.append(self.ui.n078.text())
        temp_list.append(self.ui.n079.text())

        temp_list.append(self.ui.n081.text())
        temp_list.append(self.ui.n082.text())
        temp_list.append(self.ui.n083.text())
        temp_list.append(self.ui.n084.text())
        temp_list.append(self.ui.n085.text())
        temp_list.append(self.ui.n086.text())
        temp_list.append(self.ui.n087.text())
        temp_list.append(self.ui.n088.text())
        temp_list.append(self.ui.n089.text())

        temp_list.append(self.ui.n091.text())
        temp_list.append(self.ui.n092.text())
        temp_list.append(self.ui.n093.text())
        temp_list.append(self.ui.n094.text())
        temp_list.append(self.ui.n095.text())
        temp_list.append(self.ui.n096.text())
        temp_list.append(self.ui.n097.text())
        temp_list.append(self.ui.n098.text())
        temp_list.append(self.ui.n099.text())

        return temp_list

    #槽-读取
    def read_nums(self):
        self.num_states = self.read_nums_tools()
        # logger.debug(self.num_states)
        self.int_num_state = []
        if(None not in self.num_states):
            for i in range(81):
                self.int_num_state.append(int(self.num_states[i]))
        self.check()

    #槽-开始游戏
    def start_game(self):
        self.lcd_timer.start(1000)
        self.used_time = 0
        self.create_sudu()


    #显示倒计时
    def show_lcd_time(self):
        self.used_time = self.used_time + 1
        minute = self.used_time / 60
        second = self.used_time % 60
        self.temp_time = str("%02d:%02d"%(minute, second))
        self.ui.lcd.display(self.temp_time)

    #槽-读取难度
    def set_difficulty(self):
        try:
            self.difficulty = int(self.ui.word_dif.text())
            if(self.difficulty < 0 or self.difficulty > 4):
                QMessageBox.information(self.ui, '信息', '请输入1~4的数字')
                self.ui.word_dif.clear()
        except:
            QMessageBox.information(self.ui, '信息', '请输入数字')
            self.ui.word_dif.clear()
        # logger.debug("clicked_set_difficulty; value is : {}".format(self.difficulty))

    #液晶屏初始化
    def lcd_init(self):
        self.ui.lcd.setSegmentStyle(QLCDNumber.Flat)
        self.ui.lcd.setDigitCount(5)
        self.ui.lcd.display("00:00")

        self.lcd_timer = QTimer()
        self.lcd_timer.timeout.connect(self.show_lcd_time)

    def create_sudu(self):  # 用于产生数独答案
        shudu = np.zeros((9, 9), dtype=int)  # 产生全0数组备用
        while (sum(sum(shudu[:, :])) != 405):  # 判断数独答案是否正确，简单了点，但很实用
            n = 1
            A = np.zeros((9, 9), dtype=int)
            a = [x for x in range(1, 10)]  # 产生1-9数组备用
            b = [x for x in range(1, 10)]
            random.shuffle(b)  # 产生随机1-9数组，作为数独第一行
            A[0, :] = b  # 赋值
            for i in range(1, 9):  # 开始填数
                for j in range(0, 9):
                    x = A[i, :]  # 取出所在行
                    y = A[:, j]  # 取出所在列
                    if 0 <= j and j < 3:
                        z = A[:, 0:3]
                    elif 3 <= j and j < 6:
                        z = A[:, 3:6]
                    else:
                        z = A[:, 6:9]
                    if 0 <= i and i < 3:
                        z = z[0:3, :]
                    elif 3 <= i and i < 6:
                        z = z[3:6, :]
                    else:
                        z = z[6:9, :]  # 取出所在宫

                    x_pos = np.nonzero(x)[0]  # 取出行，列，宫的所有非零值
                    X = np.zeros((len(x_pos)), dtype=int)
                    for p in range(0, len(x_pos)):
                        X[p] = x[x_pos[p]]

                    y_pos = np.nonzero(y)[0]
                    Y = np.zeros((len(y_pos)), dtype=int)
                    for p in range(0, len(y_pos)):
                        Y[p] = y[y_pos[p]]

                    z_pos = np.transpose(np.nonzero(z))
                    Z = np.zeros((len(z_pos)), dtype=int)
                    for p in range(0, len(z_pos)):
                        m = z_pos[p, 0]
                        n = z_pos[p, 1]
                        Z[p] = z[m, n]

                    t = list(set(X).union(set(Y)))
                    t = list(set(t).union(set(Z)))  # 所有非零值取并集，

                    n = list(set(a).difference(set(t)))  # 并集和a取差集，判断哪些数还可以填

                    try:
                        L = len(n)  # 判断是否还有备选数
                    except BaseException as e:
                        L = 0
                    r = random.random()
                    h = math.ceil(r * L)  # 备选数中随机选择一个
                    try:
                        A[i, j] = n[h - 1]  # 进行赋值
                    except BaseException as e:
                        n = 2  # 报错则说明之前的填数有误
                        break
                if n == 2:
                    break
            if n == 2:
                continue  # 重新开始循环
            shudu = A  # 81个数全部正确，则赋值

        for k in range(0, 9):
            b = [x for x in range(0, 9)]
            random.shuffle(b)
            for m in range(0, self.difficulty):
                shudu[k, b[m]] = 0

        new_shudu = []
        for i in range(9):
            for j in range(9):
                new_shudu.append(shudu[i][j])

        for i in range(81):
            if(new_shudu[i] == 0):
                new_shudu[i] = " "
        self.set_num(new_shudu)
        
    def set_num(self, state_list):
        self.ui.n011.setText(str(state_list[0]))
        self.ui.n012.setText(str(state_list[1]))
        self.ui.n013.setText(str(state_list[2]))
        self.ui.n014.setText(str(state_list[3]))
        self.ui.n015.setText(str(state_list[4]))
        self.ui.n016.setText(str(state_list[5]))
        self.ui.n017.setText(str(state_list[6]))
        self.ui.n018.setText(str(state_list[7]))
        self.ui.n019.setText(str(state_list[8]))

        self.ui.n021.setText(str(state_list[9]))
        self.ui.n022.setText(str(state_list[10]))
        self.ui.n023.setText(str(state_list[11]))
        self.ui.n024.setText(str(state_list[12]))
        self.ui.n025.setText(str(state_list[13]))
        self.ui.n026.setText(str(state_list[14]))
        self.ui.n027.setText(str(state_list[15]))
        self.ui.n028.setText(str(state_list[16]))
        self.ui.n029.setText(str(state_list[17]))

        self.ui.n031.setText(str(state_list[18]))
        self.ui.n032.setText(str(state_list[19]))
        self.ui.n033.setText(str(state_list[20]))
        self.ui.n034.setText(str(state_list[21]))
        self.ui.n035.setText(str(state_list[22]))
        self.ui.n036.setText(str(state_list[23]))
        self.ui.n037.setText(str(state_list[24]))
        self.ui.n038.setText(str(state_list[25]))
        self.ui.n039.setText(str(state_list[26]))

        self.ui.n041.setText(str(state_list[27]))
        self.ui.n042.setText(str(state_list[28]))
        self.ui.n043.setText(str(state_list[29]))
        self.ui.n044.setText(str(state_list[30]))
        self.ui.n045.setText(str(state_list[31]))
        self.ui.n046.setText(str(state_list[32]))
        self.ui.n047.setText(str(state_list[33]))
        self.ui.n048.setText(str(state_list[34]))
        self.ui.n049.setText(str(state_list[35]))

        self.ui.n051.setText(str(state_list[36]))
        self.ui.n052.setText(str(state_list[37]))
        self.ui.n053.setText(str(state_list[38]))
        self.ui.n054.setText(str(state_list[39]))
        self.ui.n055.setText(str(state_list[40]))
        self.ui.n056.setText(str(state_list[41]))
        self.ui.n057.setText(str(state_list[42]))
        self.ui.n058.setText(str(state_list[43]))
        self.ui.n059.setText(str(state_list[44]))

        self.ui.n061.setText(str(state_list[45]))
        self.ui.n062.setText(str(state_list[46]))
        self.ui.n063.setText(str(state_list[47]))
        self.ui.n064.setText(str(state_list[48]))
        self.ui.n065.setText(str(state_list[49]))
        self.ui.n066.setText(str(state_list[50]))
        self.ui.n067.setText(str(state_list[51]))
        self.ui.n068.setText(str(state_list[52]))
        self.ui.n069.setText(str(state_list[53]))

        self.ui.n071.setText(str(state_list[54]))
        self.ui.n072.setText(str(state_list[55]))
        self.ui.n073.setText(str(state_list[56]))
        self.ui.n074.setText(str(state_list[57]))
        self.ui.n075.setText(str(state_list[58]))
        self.ui.n076.setText(str(state_list[59]))
        self.ui.n077.setText(str(state_list[60]))
        self.ui.n078.setText(str(state_list[61]))
        self.ui.n079.setText(str(state_list[62]))

        self.ui.n081.setText(str(state_list[63]))
        self.ui.n082.setText(str(state_list[64]))
        self.ui.n083.setText(str(state_list[65]))
        self.ui.n084.setText(str(state_list[66]))
        self.ui.n085.setText(str(state_list[67]))
        self.ui.n086.setText(str(state_list[68]))
        self.ui.n087.setText(str(state_list[69]))
        self.ui.n088.setText(str(state_list[70]))
        self.ui.n089.setText(str(state_list[71]))

        self.ui.n091.setText(str(state_list[72]))
        self.ui.n092.setText(str(state_list[73]))
        self.ui.n093.setText(str(state_list[74]))
        self.ui.n094.setText(str(state_list[75]))
        self.ui.n095.setText(str(state_list[76]))
        self.ui.n096.setText(str(state_list[77]))
        self.ui.n097.setText(str(state_list[78]))
        self.ui.n098.setText(str(state_list[79]))
        self.ui.n099.setText(str(state_list[80]))

    def check(self):
        result_num=np.array(self.int_num_state).reshape(9,9) 
        if sum(sum(result_num[:,:])) == 405:
            self.flag = 1
            self.show_message()
        else:
            self.flag = 2
            self.show_message()

    def show_message(self):
        if self.flag == 1:
            QMessageBox.information(self.ui, '恭喜', '您已经成功破解此题,用时'+self.temp_time)
        elif self.flag == 2:
            QMessageBox.warning(self.ui, '失败', '解题错误,用时'+self.temp_time+"请继续答题")


if __name__ == "__main__":
    # QApplication.setStyle(QStyleFactory.create('Fusion'))
    app = QApplication([])
    app.setStyle('Fusion')

    sudoku = Sudoku()
    sudoku.ui.show()
    app.exec_()