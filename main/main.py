from PySide2.QtWidgets import QApplication,QMessageBox,QStyleFactory
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile

import PySide2
import os

dirname = os.path.dirname(PySide2.__file__) 
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path



class Sudoku():
    def __init__(self):
        #从文件中加载UI定义
        qfile_states = QFile("./pyside2/main.ui")
        qfile_states.open(QFile.ReadOnly)
        qfile_states.close()
        '''
        从UI定义中动态创建一个相应的窗口文件
        里面的控件对象也成为窗口对象的属性了
        '''
        self.ui = QUiLoader().load(qfile_states)            #加载窗口

        self.push_button_connects()

        

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


    def read_nums(self):
        print("clicked")



if __name__ == "__main__":
    # QApplication.setStyle(QStyleFactory.create('Fusion'))
    app = QApplication([])
    app.setStyle('Fusion')

    sudoku = Sudoku()
    sudoku.ui.show()
    app.exec_()