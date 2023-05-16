from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from new import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import sys
import re
import shutil
import os



class TCParserBackEnd(QtWidgets.QWidget, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(MainWindow)
        self.textEdit_2.setStyleSheet("border: 1px solid black;")
        self.Browse_Button.clicked.connect(self.BUTTON_BROWSE_func)
        self.Generate_Button.clicked.connect(self.Generate_Button_func)





    def BUTTON_BROWSE_func(self):
        global ext
        global old_file_location
        global old_file_name
        extension = self.comboBox.itemText(self.comboBox.currentIndex())
        extension = str(extension)
        ext = str(extension)
        extension = 'File(*.'+ extension +')'
        global file_name
        file_name = QFileDialog.getOpenFileName(self, 'Open File', 'file', extension)
        file_name = file_name[0]
        old_file_name = os.path.basename(file_name)
        self.textEdit_2.setText(file_name)
########################################################## check if the file is in the same directory ##################
        condition = file_name.replace(os.path.basename(file_name),"")
        condition = condition[:-1]
        old_file_location = condition
        condition = condition.replace('/','\\')
        if condition == os.getcwd():
            pass
        else:
            shutil.move(file_name, os.getcwd())

########################################################################################################################



###############################################################################$$$$$$$$$$
###############################################################################$$$$$$$$$$
###############################################################################$$$$$$$$$$
    def generated_automatic(self):
        os.rename(os.path.basename(file_name), 'moved_file.'+ ext )
        img = Image.open('moved_file.'+ext)

        img.save("icon.ico", size = size)
        self.progressBar.setValue(100)

        ##  send the file back to its old location ####################
        os.rename(('moved_file.'+ext) , old_file_name)
        current_location = os.getcwd()
        current_location = current_location + "\\" + old_file_name
        current_location = current_location.replace('\\', '/')
        shutil.move(current_location, old_file_location)

        quit()

###############################################################################$$$$$$$$$$
###############################################################################$$$$$$$$$$
###############################################################################$$$$$$$$$$


    def Generate_Button_func(self):
        global size
        size = self.comboBox_2.itemText(self.comboBox.currentIndex())
        size = size.replace('[','(')
        size = size.replace(']', ')')
        size = size.replace(':', ',')
        size = '['+size+']'

        if self.textEdit_2.text() == "":
            QMessageBox.about(self, "Error Message", "Browse image first")
            quit()

        no_operation = 0
        text = self.input_name.toPlainText()
        if text == "":
            self.generated_automatic()

        first_letter = text[0].isalpha()
        ################################
        text = text.replace(" ","")  #remove space
        ################################
        if first_letter is True:
            no_operation += 1
        else:
            self.generated_automatic()
        ################################
        if (bool(re.match('^[a-zA-Z0-9]*$', text)) == True):
            no_operation += 1
        else:
            self.generated_automatic()
        ################################
        os.rename(os.path.basename(file_name), 'moved_file.' + ext)
        img = Image.open('moved_file.' + ext)
        img.save(text + ".ico" , size = size)
        ##  send the file back to its old location ####################
        os.rename(('moved_file.' + ext), old_file_name)
        current_location = os.getcwd()
        current_location = current_location + "\\" + old_file_name
        current_location = current_location.replace('\\', '/')
        shutil.move(current_location, old_file_location)
        #################################

        self.progressBar.setValue(100)
        quit()





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TCParserBackEnd()
    MainWindow.show()
    sys.exit(app.exec_())







