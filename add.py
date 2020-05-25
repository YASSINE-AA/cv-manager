#!/usr/bin/env python3

from PySide2.QtWidgets import QMessageBox, QMainWindow, QLabel, QPushButton, QTableWidgetItem, QTableWidget, QApplication, QWidget, QLineEdit, QMenuBar, QStatusBar
from PySide2.QtGui import QFont
from PySide2.QtCore import QRect, QCoreApplication, QMetaObject
import sqlite3
from datetime import *


class Ui_Add_Window(object):
    def setupUi(self, Add_Window):
        Add_Window.setObjectName("Add_Window")
        Add_Window.resize(598, 276)
        Add_Window.setFixedSize(Add_Window.size())
        self.centralwidget = QWidget(Add_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.addTxt = QLineEdit(self.centralwidget)
        self.addTxt.setGeometry(QRect(20, 40, 551, 51))
        self.addTxt.setObjectName("addTxt")
        self.cv_file_name = QLineEdit(self.centralwidget)
        self.cv_file_name.setGeometry(QRect(20, 120, 551, 51))
        self.cv_file_name.setObjectName("cv_file_name")
        self.cv_file_name.setPlaceholderText("Example: file.docx")
        self.addBtn = QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QRect(20, 200, 551, 51))
        self.addBtn.setObjectName("addBtn")
        Add_Window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Add_Window)
        self.menubar.setGeometry(QRect(0, 0, 598, 22))
        self.menubar.setObjectName("menubar")
        Add_Window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Add_Window)
        self.statusbar.setObjectName("statusbar")
        Add_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Add_Window)
        QMetaObject.connectSlotsByName(Add_Window)

        self.addBtn.clicked.connect(self.Add)

    def retranslateUi(self, Add_Window):
        _translate = QCoreApplication.translate
        Add_Window.setWindowTitle(_translate("Add_Window", "Add"))
        self.addTxt.setPlaceholderText(_translate("Add_Window", "Add new CV"))
        self.addBtn.setText(_translate("Add_Window", "Add"))

    def Add(self):
        self.add_txt = self.addTxt.text()
        self.cv_filename_txt = self.cv_file_name.text()
        self.conn = sqlite3.connect('cv.db')
        self.cur = self.conn.cursor()
        # TODO: Fix the error system
        def error(error_message):
            error_msgbox = QMessageBox()
            error_msgbox.setIcon(QMessageBox.Information)
            error_msgbox.setWindowTitle("Oh no!")
            error_msgbox.setText("Error!")
            error_msgbox.setInformativeText(error_message)
            error_msgbox.setStandardButtons(QMessageBox.Close)
            error_msgbox.exec_()

        if self.add_txt == '' and self.cv_file_name == '':
            error("One or both text fields are empty.")
        if self.add_txt != '' and self.cv_file_name != '':
            if "." in self.cv_filename_txt:
                timeofcreation = datetime.now()
                self.cur.execute("INSERT INTO user (cvname, cvfilename, date) VALUES(?,?,?);", (str(self.add_txt), str(self.cv_filename_txt),str(timeofcreation)))
                self.conn.commit()
                added_msg = QMessageBox()
                added_msg.setIcon(QMessageBox.Information)
                added_msg.setText("Hooray!")
                added_msg.setWindowTitle("Success!")
                added_msg.setInformativeText("Your CV has been successfully added to the database.")
                added_msg.setStandardButtons(QMessageBox.Ok)
                added_msg.exec_()

            else:
                error("Add a valid filename")




if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Add_Window = QMainWindow()
    ui = Ui_Add_Window()
    ui.setupUi(Add_Window)
    Add_Window.show()
    sys.exit(app.exec_())

