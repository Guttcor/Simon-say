# Form implementation generated from reading ui file 'd:\documentos\Programacion avanzada\proyectos\Practica 6\ventana_principal.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(453, 613)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.483318, y1:0.381, x2:0.438, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.636364 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(100, 10, 271, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color: rgb(0,0, 0);\n"
"font: 24pt \"Impact\";\n"
"border:40px;\n"
"font-color:rgb(255,0,0);\n"
"")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_3 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(110, 140, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setStyleSheet("background-color: rgb(0,0, 0);\n"
"font: 24pt \"Impact\";\n"
"border:40px;\n"
"font-color:rgb(255,0,0);\n"
"")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.boton_salirp = QtWidgets.QPushButton(parent=self.centralwidget)
        self.boton_salirp.setGeometry(QtCore.QRect(420, 0, 30, 31))
        self.boton_salirp.setMinimumSize(QtCore.QSize(10, 10))
        self.boton_salirp.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"font: 12pt \"Segoe UI\";")
        self.boton_salirp.setObjectName("boton_salirp")
        self.min_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.min_2.setGeometry(QtCore.QRect(330, 0, 30, 31))
        self.min_2.setMinimumSize(QtCore.QSize(10, 10))
        self.min_2.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"font: 12pt \"Segoe UI\";")
        self.min_2.setObjectName("min_2")
        self.normal = QtWidgets.QPushButton(parent=self.centralwidget)
        self.normal.setGeometry(QtCore.QRect(360, 0, 30, 31))
        self.normal.setMinimumSize(QtCore.QSize(10, 10))
        self.normal.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"font: 12pt \"Segoe UI\";")
        self.normal.setObjectName("normal")
        self.Salir = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Salir.setGeometry(QtCore.QRect(100, 370, 281, 61))
        self.Salir.setStyleSheet("QPushButton\n"
"{background-color: rgb(0,0, 0);\n"
"font: 24pt \"Impact\";\n"
"border:40px;\n"
"font-color:white;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgba(170,84,255,30);\n"
"border:40px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(170,84,255,90);\n"
"border:40px;\n"
"}")
        self.Salir.setObjectName("Salir")
        self.Xtream = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Xtream.setGeometry(QtCore.QRect(90, 290, 301, 61))
        self.Xtream.setStyleSheet("QPushButton\n"
"{background-color: rgb(0,0, 0);\n"
"font: 24pt \"Impact\";\n"
"border:40px;\n"
"font-color:white;\n"
"    color: rgb(255, 0, 0);\n"
" border: 3px solid #ff0512;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgba(255,0,0,30);\n"
"border:40px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,0,0,90);\n"
"border:40px;\n"
"}")
        self.Xtream.setObjectName("Xtream")
        self.Un_jugador = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Un_jugador.setGeometry(QtCore.QRect(90, 210, 301, 61))
        self.Un_jugador.setStyleSheet("QPushButton\n"
"{background-color: rgb(0,0, 0);\n"
"font: 24pt \"Impact\";\n"
"border:40px;\n"
"font-color:white;\n"
"color: rgb(17, 107, 191);\n"
" border: 3px solid #3502ff;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgba(0,0,255,30);\n"
"border:40px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(0,0,255,90);\n"
"border:40px;\n"
"}")
        self.Un_jugador.setObjectName("Un_jugador")
        self.max = QtWidgets.QPushButton(parent=self.centralwidget)
        self.max.setGeometry(QtCore.QRect(390, 0, 30, 31))
        self.max.setMinimumSize(QtCore.QSize(10, 10))
        self.max.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"font: 20pt \"Segoe UI\";")
        self.max.setObjectName("max")
        self.textBrowser_2 = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(100, 80, 271, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("background-color: rgb(0,0, 0);\n"
"font: 24pt \"Impact\";\n"
"border:40px;\n"
"font-color:rgb(255,0,0);\n"
"")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.Salir.raise_()
        self.textBrowser.raise_()
        self.textBrowser_3.raise_()
        self.boton_salirp.raise_()
        self.min_2.raise_()
        self.normal.raise_()
        self.Xtream.raise_()
        self.Un_jugador.raise_()
        self.max.raise_()
        self.textBrowser_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 453, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.boton_salirp.clicked.connect(MainWindow.close) # type: ignore
        self.min_2.clicked.connect(MainWindow.showMinimized) # type: ignore
        self.Salir.clicked.connect(MainWindow.close) # type: ignore
        self.normal.clicked.connect(MainWindow.showNormal) # type: ignore
        self.max.clicked.connect(MainWindow.showMaximized) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Impact\'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Welcome</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Impact\'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Game Modes</span></p></body></html>"))
        self.boton_salirp.setText(_translate("MainWindow", "x"))
        self.min_2.setText(_translate("MainWindow", "-"))
        self.normal.setText(_translate("MainWindow", "□"))
        self.Salir.setText(_translate("MainWindow", "Close"))
        self.Xtream.setText(_translate("MainWindow", "Xtream"))
        self.Un_jugador.setText(_translate("MainWindow", "1 player"))
        self.max.setText(_translate("MainWindow", "□"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Impact\'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Simon Says</span></p></body></html>"))
