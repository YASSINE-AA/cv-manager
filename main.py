#!/usr/bin/env python3
import sqlite3
from PySide2.QtWidgets import QMessageBox, QMainWindow, QLabel, QPushButton, QTableWidgetItem, QTableWidget, QApplication, QWidget, QLineEdit, QMenuBar, QStatusBar
from PySide2.QtGui import QFont, Qt
from PySide2.QtCore import QRect, QCoreApplication, QMetaObject
import add
import delete
import settings


# Connects to database
conn = sqlite3.connect("cv.db")
cur = conn.cursor()
cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='user' ''')

# Checks if table "user" exists and if it does it skips these lines of code
if not cur.fetchone()[0] == 1:
    cur.execute("CREATE TABLE user(name)")
    addColumn = "ALTER TABLE user ADD COLUMN cvname varchar(32)"
    cur.execute(addColumn)
    addColumn2 = "ALTER TABLE user ADD COLUMN cvfilename varchar(32)"
    cur.execute(addColumn2)
    addColumn3 = "ALTER TABLE user ADD COLUMN date varchar(32)"
    cur.execute(addColumn3)
    conn.commit()


class Ui_Main_Window():

    def Show_Data(self):
        self.conn = sqlite3.connect("cv.db")
        self.query =('SELECT * FROM user')
        self.result = self.conn.execute(self.query)
        self.listWidget.setRowCount(0)
        self.listWidget.setColumnWidth( 1, 200)
        self.listWidget.setColumnWidth( 2, 200)
        self.listWidget.setColumnWidth( 3, 200)

        for self.row_num,self.row_data in enumerate(self.result):
            self.listWidget.insertRow(self.row_num)

            for self.col_num,self.data in enumerate(self.row_data):
                self.listWidget.setItem(self.row_num,self.col_num,QTableWidgetItem(str(self.data)))


    def setupUi(self, Main_Window):

        def about_fn():
            about_msgbox = QMessageBox()
            about_msgbox.setWindowTitle("About")
            about_msgbox.setIcon(QMessageBox.Information)
            about_msgbox.setText(f"CV Collector {settings.version}")
            about_msgbox.setInformativeText(f'''
CV Collector is an app that lets you store your CVs in a secure and lightweight sqlite3 database.
{settings.special_text}.
            ''')
            about_msgbox.setStandardButtons(QMessageBox.Close)
            about_msgbox.exec_()
        font1 = QFont("Roboto", 20)
        font2 = QFont("Roboto", 16)
        Main_Window.setObjectName("Main_Window")
        Main_Window.resize(700, 535)
        Main_Window.setFixedSize(Main_Window.size())
        self.centralwidget = QWidget(Main_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.search = QLineEdit(self.centralwidget)
        self.search.setGeometry(QRect(60, 30, 460, 50))
        self.search.setFont(font1)
        self.search.setPlaceholderText("Search..")

        menuBar = QMenuBar(self.centralwidget)
        Help = menuBar.addMenu("Help")
        About = Help.addAction("About")
        About.triggered.connect(about_fn)
        self.addBtn = QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QRect(20, 90, 191, 41))
        self.addBtn.setObjectName("addBtn")
        self.deleteBtn = QPushButton(self.centralwidget)
        self.deleteBtn.setGeometry(QRect(245, 90, 191, 41))
        self.deleteBtn.setObjectName("deleteBtn")
        self.showBtn = QPushButton(self.centralwidget)
        self.showBtn.setGeometry(QRect(470, 90, 191, 41))
        self.showBtn.setObjectName("showBtn")
        self.listWidget = QTableWidget(self.centralwidget)
        self.listWidget.setGeometry(QRect(20, 150, 661, 350))
        self.listWidget.setRowCount(20)
        self.listWidget.setColumnCount(4)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.hideColumn(0)
        horizontal_names = ('hidden', 'CV Name', 'CV Filename', 'Date')
        self.listWidget.setHorizontalHeaderLabels(horizontal_names)
        self.listWidget.setColumnWidth( 1, 200)
        self.listWidget.setColumnWidth( 2, 200)
        self.listWidget.setColumnWidth( 3, 200)
        self.listWidget.setFont(font2)

        def initialize():
            self.Show_Data()
        initialize()

        def search_fn():
            columnOfInterest = 1
            valueOfInterest = self.search.text()
            for rowIndex in range(self.listWidget.rowCount()):
                item = self.listWidget.item(rowIndex, columnOfInterest)
                if self.search.text() in item.text():
                    self.listWidget.setRowHidden(rowIndex, False)
                else:
                    self.listWidget.setRowHidden(rowIndex, True)


        self.searchBtn = QPushButton(self.centralwidget)
        self.searchBtn.setGeometry(QRect(530, 30, 100, 50))
        self.searchBtn.setObjectName("addBtn")
        self.searchBtn.clicked.connect(search_fn)

        Main_Window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Main_Window)
        self.menubar.setGeometry(QRect(0, 0, 723, 22))
        self.menubar.setObjectName("menubar")
        Main_Window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Main_Window)
        self.statusbar.setObjectName("statusbar")
        Main_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Main_Window)
        QMetaObject.connectSlotsByName(Main_Window)
        self.showBtn.clicked.connect(self.Show_Data)

        self.addBtn.clicked.connect(self.Add)
        self.deleteBtn.clicked.connect(self.Delete)

    def retranslateUi(self, Main_Window):
        _translate = QCoreApplication.translate
        Main_Window.setWindowTitle(_translate("Main_Window", "CV Collector"))
        self.addBtn.setText(_translate("Main_Window", "Add CV"))
        self.deleteBtn.setText(_translate("Main_Window", "Delete CV"))
        self.showBtn.setText(_translate("Main_Window", "Update List"))
        self.searchBtn.setText(_translate("Main_Window", "search"))

    def Add(self):
        self.Add_Window = QMainWindow()
        self.Add_Window_Ui = add.Ui_Add_Window()
        self.Add_Window_Ui.setupUi(self.Add_Window)
        self.Add_Window.show()

    def Delete(self):
        self.Delete_Window = QMainWindow()
        self.Delete_Window_Ui = delete.Ui_Delete_Window()
        self.Delete_Window_Ui.setupUi(self.Delete_Window)
        self.Delete_Window.show()






if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    Main_Window = QMainWindow()
    ui = Ui_Main_Window()
    ui.setupUi(Main_Window)
    Main_Window.show()
    sys.exit(app.exec_())

