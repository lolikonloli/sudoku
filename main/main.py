from PySide2.QtWidgets import QApplication,QMessageBox,QStyleFactory
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile

import PySide2
import os

from loguru import logger



dirname = os.path.dirname(PySide2.__file__) 
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path



class Sudoku():
    def __init__(self):
        #从文件中加载UI定义
        qfile_states = QFile("./pyside2/main.ui")
        qfile_states.open(QFile.ReadOnly)
        qfile_states.close()
        self.ui = QUiLoader().load(qfile_states)            #加载窗口

        #属性
        self.num_states = []
        self.difficulty = 1

        #绑定
        self.push_button_connects()
        self.ui.bt_start.clicked.connect(self.start_game)
        self.ui.bt_set_dif.clicked.connect(self.set_difficulty)
        

        
    #输入绑定
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

    #读取
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

    #读取
    def read_nums(self):
        self.num_states = self.read_nums_tools()
        # logger.debug(self.num_states)

    def start_game(self):
        logger.debug("clicked_start_game")

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


    


if __name__ == "__main__":
    # QApplication.setStyle(QStyleFactory.create('Fusion'))
    app = QApplication([])
    app.setStyle('Fusion')

    sudoku = Sudoku()
    sudoku.ui.show()
    app.exec_()