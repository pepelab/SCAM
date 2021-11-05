from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login(object):
    #==================== ОКНО ЛОГИНА ====================
    def setupUi(self, login):
        login.setObjectName("login")
        login.setEnabled(True)
        login.resize(700, 500)
        login.setFixedSize(700,500)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        login.setFont(font)
        login.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        login.setWindowIcon(QtGui.QIcon('icon.ico'))

        self.centralwidget = QtWidgets.QWidget(login)
        self.centralwidget.setObjectName("centralwidget")


        #==================== КНОПКА LOGIN ====================
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(170, 290, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.login_button.setFont(font)
        self.login_button.setStyleSheet("font: 12pt \"Montserrat\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(27, 27, 27);\n"
                                        "")
        self.login_button.setCheckable(False)
        self.login_button.setAutoDefault(False)
        self.login_button.setFlat(False)
        self.login_button.setObjectName("login_button")


        #==================== SCAM ====================
        self.scam_name = QtWidgets.QLabel(self.centralwidget)
        self.scam_name.setGeometry(QtCore.QRect(270, 70, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.scam_name.setFont(font)
        self.scam_name.setObjectName("scam_name")


        #==================== ПОЛЕ ДЛЯ EMAIL ====================
        self.email_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.email_edit.setGeometry(QtCore.QRect(170, 170, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.email_edit.setFont(font)
        self.email_edit.setObjectName("email_edit")


        #==================== ПОЛЕ ДЛЯ PASSWORD ====================
        self.password_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_edit.setGeometry(QtCore.QRect(170, 230, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.password_edit.setFont(font)
        self.password_edit.setObjectName("password_edit")
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        
        login.setCentralWidget(self.centralwidget)
        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)


    #==================== НАЗВАНИЯ ====================
    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle("SCAM")
        self.login_button.setText(_translate("login", "Login"))
        self.scam_name.setText(_translate("login", "<html><head/><body><p align=\"center\">SCAM</p></body></html>"))
        self.email_edit.setPlaceholderText(_translate("login", "E-mail"))
        self.password_edit.setPlaceholderText(_translate("login", "Password"))