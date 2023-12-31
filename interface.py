from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(888, 313)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QtCore.QSize(888, 313))
        mainWindow.setMaximumSize(QtCore.QSize(888, 313))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        mainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 921, 301))
        self.frame.setStyleSheet("background-color: rgb(0, 0, 127);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 411, 251))
        self.groupBox.setStyleSheet("font: 75 14pt \"Ebrima\";\n"
"background-color: rgb(221, 255, 249);")
        self.groupBox.setObjectName("groupBox")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(50, 30, 281, 31))
        self.label_7.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"text-decoration: underline;\n"
"background-color: rgb(200, 197, 173);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 130, 31, 41))
        self.label_8.setStyleSheet("font: 12pt \"Yu Gothic UI\";")
        self.label_8.setObjectName("label_8")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 31, 20))
        self.label_2.setStyleSheet("font: 12pt \"Yu Gothic UI\";")
        self.label_2.setObjectName("label_2")
        self.x = QtWidgets.QLineEdit(self.groupBox)
        self.x.setGeometry(QtCore.QRect(40, 80, 41, 20))
        self.x.setStyleSheet("font: 12pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.x.setObjectName("x")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 110, 31, 21))
        self.label_6.setStyleSheet("font: 12pt \"Yu Gothic UI\";")
        self.label_6.setObjectName("label_6")
        self.y = QtWidgets.QLabel(self.groupBox)
        self.y.setGeometry(QtCore.QRect(40, 110, 131, 21))
        self.y.setStyleSheet("font: 12pt \"Yu Gothic UI\";")
        self.y.setObjectName("y")
        self.vvod = QtWidgets.QPushButton(self.groupBox)
        self.vvod.setGeometry(QtCore.QRect(10, 180, 101, 31))
        self.vvod.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-color: black;\n"
"")
        self.vvod.setObjectName("vvod")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(170, 70, 231, 61))
        self.textEdit.setStyleSheet("font: 11pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.clear_btn = QtWidgets.QPushButton(self.groupBox)
        self.clear_btn.setGeometry(QtCore.QRect(140, 180, 111, 31))
        self.clear_btn.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-color: black;")
        self.clear_btn.setObjectName("clear_btn")
        self.label_bug = QtWidgets.QLabel(self.groupBox)
        self.label_bug.setGeometry(QtCore.QRect(220, 140, 121, 31))
        self.label_bug.setStyleSheet("font: 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 0, 0);\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-color: black;")
        self.label_bug.setObjectName("label_bug")
        self.n = QtWidgets.QLabel(self.groupBox)
        self.n.setGeometry(QtCore.QRect(40, 130, 20, 41))
        self.n.setStyleSheet("font: 12pt \"Yu Gothic UI\";")
        self.n.setObjectName("n")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(430, 20, 441, 251))
        self.groupBox_2.setStyleSheet("font: 75 14pt \"Ebrima\";\n"
"background-color: rgb(255, 249, 198);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(20, 30, 191, 21))
        self.label.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"text-decoration: underline;")
        self.label.setObjectName("label")
        self.material = QtWidgets.QComboBox(self.groupBox_2)
        self.material.setGeometry(QtCore.QRect(20, 60, 141, 22))
        self.material.setStyleSheet("font: 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.material.setObjectName("material")
        self.material.addItem("")
        self.material.addItem("")
        self.material.addItem("")
        self.material.addItem("")
        self.material.addItem("")
        self.material.addItem("")
        self.material.addItem("")
        self.material.addItem("")
        self.material.addItem("")
        self.material.addItem("")
        self.material.addItem("")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(160, 100, 20, 21))
        self.label_5.setStyleSheet("font: 12pt \"Yu Gothic UI\";")
        self.label_5.setObjectName("label_5")
        self.d_z = QtWidgets.QLineEdit(self.groupBox_2)
        self.d_z.setGeometry(QtCore.QRect(44, 100, 41, 20))
        self.d_z.setStyleSheet("font: 12pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.d_z.setObjectName("d_z")
        self.m_z = QtWidgets.QLineEdit(self.groupBox_2)
        self.m_z.setGeometry(QtCore.QRect(114, 100, 41, 20))
        self.m_z.setStyleSheet("font: 12pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.m_z.setObjectName("m_z")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(14, 100, 21, 20))
        self.label_3.setStyleSheet("font: 12pt \"Yu Gothic UI\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(94, 100, 16, 16))
        self.label_4.setStyleSheet("font: 12pt \"Yu Gothic UI\";")
        self.label_4.setObjectName("label_4")
        self.result = QtWidgets.QPushButton(self.groupBox_2)
        self.result.setGeometry(QtCore.QRect(30, 150, 121, 31))
        self.result.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-color: black;")
        self.result.setObjectName("result")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(220, 25, 131, 31))
        self.label_10.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(220, 115, 131, 31))
        self.label_9.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.label_9.setObjectName("label_9")
        self.vivod_1 = QtWidgets.QTextEdit(self.groupBox_2)
        self.vivod_1.setGeometry(QtCore.QRect(220, 50, 201, 51))
        self.vivod_1.setStyleSheet("font: 12pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.vivod_1.setObjectName("vivod_1")
        self.vivod_2 = QtWidgets.QTextEdit(self.groupBox_2)
        self.vivod_2.setGeometry(QtCore.QRect(220, 140, 201, 51))
        self.vivod_2.setStyleSheet("font: 12pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.vivod_2.setObjectName("vivod_2")
        self.label_bug_result = QtWidgets.QLabel(self.groupBox_2)
        self.label_bug_result.setEnabled(True)
        self.label_bug_result.setGeometry(QtCore.QRect(70, 199, 271, 31))
        self.label_bug_result.setStyleSheet("font: 75 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 0, 0);\n"
"border-style: outset;\n"
"border-width:1px;\n"
"border-color: black;")
        self.label_bug_result.setObjectName("label_bug_result")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 888, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Решение задачи теории упругости для плоскости с круговым отверстием"))
        self.groupBox.setTitle(_translate("mainWindow", "Задайте вектор напряженности:"))
        self.label_7.setText(_translate("mainWindow", "Fn = X + iY - вектор напряжения"))
        self.label_8.setText(_translate("mainWindow", "n ="))
        self.label_2.setText(_translate("mainWindow", "X ="))
        self.label_6.setText(_translate("mainWindow", "Y ="))
        self.y.setText(_translate("mainWindow", "abs(sqrt(1-X^2))"))
        self.vvod.setText(_translate("mainWindow", "Добавить"))
        self.clear_btn.setText(_translate("mainWindow", "Очистить"))
        self.label_bug.setText(_translate("mainWindow", "Введите X!"))
        self.n.setText(_translate("mainWindow", "0"))
        self.groupBox_2.setTitle(_translate("mainWindow", "Расчеты"))
        self.label.setText(_translate("mainWindow", "Материал пластины:"))
        self.material.setItemText(0, _translate("mainWindow", "Алюминий"))
        self.material.setItemText(1, _translate("mainWindow", "Вольфрам"))
        self.material.setItemText(2, _translate("mainWindow", "Германий"))
        self.material.setItemText(3, _translate("mainWindow", "Дюралюминий"))
        self.material.setItemText(4, _translate("mainWindow", "Иридий"))
        self.material.setItemText(5, _translate("mainWindow", "Латунь"))
        self.material.setItemText(6, _translate("mainWindow", "Медь"))
        self.material.setItemText(7, _translate("mainWindow", "Свинец"))
        self.material.setItemText(8, _translate("mainWindow", "Олово"))
        self.material.setItemText(9, _translate("mainWindow", "Серебро"))
        self.material.setItemText(10, _translate("mainWindow", "Сталь"))
        self.label_5.setText(_translate("mainWindow", "i"))
        self.label_3.setText(_translate("mainWindow", "Z = "))
        self.label_4.setText(_translate("mainWindow", "+"))
        self.result.setText(_translate("mainWindow", "Результат"))
        self.label_10.setText(_translate("mainWindow", "Напряжение"))
        self.label_9.setText(_translate("mainWindow", "Смещение"))
        self.label_bug_result.setText(_translate("mainWindow", "Задайте параметры Z!"))
