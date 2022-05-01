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


if __name__ == "__main__":
    # QApplication.setStyle(QStyleFactory.create('Fusion'))
    app = QApplication([])
    app.setStyle('Fusion')

    sudoku = Sudoku()
    sudoku.ui.show()
    app.exec_()