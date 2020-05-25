#!/usr/bin/env python3

import sqlite3
from PySide2.QtWidgets import QMessageBox, QMainWindow, QLabel, QPushButton, QTableWidgetItem, QTableWidget, QApplication, QWidget, QLineEdit, QMenuBar, QStatusBar
from PySide2.QtGui import QFont
from PySide2.QtCore import QRect, QCoreApplication, QMetaObject


class Ui_Delete_Window(object):
    def Show_Data(self):

        self.conn = sqlite3.connect("cv.db")
        self.query =('SELECT * FROM user')
        self.result = self.conn.execute(self.query)

        for self.row_num,self.row_data in enumerate(self.result):
            self.tableWidget.insertRow(self.row_num)
            for self.col_num,self.data in enumerate(self.row_data):
                self.tableWidget.setItem(self.row_num,self.col_num,QTableWidgetItem(str(self.data)))



    def setupUi(self, Delete_Window):
        font2 = QFont("Roboto", 16)
        Delete_Window.setObjectName("Delete_Window")
        Delete_Window.resize(685, 500)
        Delete_Window.setFixedSize(Delete_Window.size())
        self.centralwidget = QWidget(Delete_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QRect(10, 20, 661, 181))
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("listWidget")
        self.tableWidget.hideColumn(0)
        self.tableWidget.setColumnWidth( 1, 200)
        self.tableWidget.setColumnWidth( 2, 200)
        self.tableWidget.setColumnWidth( 3, 200)
        
        horizontal_names = ('hidden', 'CV Name', 'CV Filename', 'Date')
        self.tableWidget.setHorizontalHeaderLabels(horizontal_names)
        self.tableWidget.setFont(font2)
        self.numberEdit = QLineEdit(self.centralwidget)
        self.numberEdit.setGeometry(QRect(20, 240, 651, 41))
        self.numberEdit.setObjectName("numberEdit")
        self.deleteBtn = QPushButton(self.centralwidget)
        self.deleteBtn.setGeometry(QRect(20, 300, 651, 51))
        self.deleteBtn.setObjectName("deleteBtn")
        self.delete_allBtn = QPushButton(self.centralwidget)
        self.delete_allBtn.setGeometry(QRect(20, 420, 651, 51))
        self.delete_allBtn.setObjectName("delete_allBtn")
        self.delete_allBtn.clicked.connect(self.Delete_All)
        self.delete_allBtn.setStyleSheet("background-color: red; color: white")
        Delete_Window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Delete_Window)
        self.menubar.setGeometry(QRect(0, 0, 685, 22))
        self.menubar.setObjectName("menubar")
        Delete_Window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Delete_Window)
        self.statusbar.setObjectName("statusbar")
        Delete_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Delete_Window)
        QMetaObject.connectSlotsByName(Delete_Window)

        self.Show_Data()

        self.deleteBtn.clicked.connect(self.Delete)


    def retranslateUi(self, Delete_Window):
        _translate = QCoreApplication.translate
        Delete_Window.setWindowTitle(_translate("Delete_Window", "Delete"))
        self.numberEdit.setPlaceholderText(_translate("Delete_Window", "Enter the number of an entry you want to delete."))
        self.deleteBtn.setText(_translate("Delete_Window", "Delete"))
        self.delete_allBtn.setText(_translate("Delete_Window", "Delete All"))

    def Delete(self):
        self.number = int(self.numberEdit.text())
        deleted_msgbox = QMessageBox()
        deleted_msgbox.setIcon(QMessageBox.Information)
        #deleted_msgbox.setWindowTitle("")
        deleted_msgbox.setText(f"You're about to delete entry {self.number}")
        deleted_msgbox.setInformativeText("You can't reverse this, are you sure you want to proceed?")
        deleted_msgbox.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        result = deleted_msgbox.exec_()
        if result == QMessageBox.Yes:
            self.conn = sqlite3.connect("cv.db")
            self.cur = self.conn.cursor()
            self.query = ('DELETE FROM user WHERE id = "%s"'%self.number)
            self.cur.execute(self.query)
            self.conn.commit()

    def Delete_All(self):
        deleted_all_msgbox = QMessageBox()
        deleted_all_msgbox.setIcon(QMessageBox.Information)
        deleted_all_msgbox.setWindowTitle("Caution")
        deleted_all_msgbox.setText("You're about to delete All of your entries.")
        deleted_all_msgbox.setInformativeText("You can't reverse this, are you sure you want to proceed?")
        deleted_all_msgbox.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        result = deleted_all_msgbox.exec_()
        if result == QMessageBox.Yes:
            self.conn = sqlite3.connect("cv.db")
            self.cur = self.conn.cursor()
            self.cur.execute('DELETE FROM user',);
            self.conn.commit()
            print("all deleted.")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Delete_Window = QMainWindow()
    ui = Ui_Delete_Window()
    ui.setupUi(Delete_Window)
    Delete_Window.show()
    sys.exit(app.exec_())

