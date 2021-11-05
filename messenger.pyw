from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_messenger(object):
    #==================== ОКНО МЕСЕНДЖЕРА ====================
    def setupUi(self, messenger):
        messenger.setObjectName("messenger")
        messenger.resize(700, 500)
        messenger.setFixedSize(700,500)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        messenger.setFont(font)
        messenger.setWindowIcon(QtGui.QIcon('icon.ico'))

        self.centralwidget = QtWidgets.QWidget(messenger)
        self.centralwidget.setObjectName("centralwidget")


        #==================== ПОЛЕ TO ====================
        self.to_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.to_edit.setGeometry(QtCore.QRect(130, 40, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.to_edit.setFont(font)
        self.to_edit.setObjectName("to_edit")


        #==================== КНОПКА SEND ====================
        self.send_button = QtWidgets.QPushButton(self.centralwidget)
        self.send_button.setGeometry(QtCore.QRect(130, 410, 441, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.send_button.setFont(font)
        self.send_button.setStyleSheet("font: 12pt \"Montserrat\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(27, 27, 27);\n"
                                        "")
        self.send_button.setCheckable(False)
        self.send_button.setAutoDefault(False)
        self.send_button.setFlat(False)
        self.send_button.setObjectName("send_button")


        #==================== ПОЛЕ SUBJECT ====================
        self.subject_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.subject_edit.setGeometry(QtCore.QRect(130, 90, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.subject_edit.setFont(font)
        self.subject_edit.setObjectName("subject_edit")


        #==================== ОКНО ДЛЯ СООБЩЕНИЯ ====================
        self.message_edit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.message_edit.setGeometry(QtCore.QRect(130, 150, 441, 241))
        self.message_edit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.message_edit.setObjectName("message_edit")
        messenger.setCentralWidget(self.centralwidget)

        self.retranslateUi(messenger)
        QtCore.QMetaObject.connectSlotsByName(messenger)


    #==================== НАЗВАНИЯ ====================
    def retranslateUi(self, messenger):
        _translate = QtCore.QCoreApplication.translate
        messenger.setWindowTitle("Messenger")
        self.to_edit.setPlaceholderText(_translate("messenger", "To"))
        self.send_button.setText(_translate("messenger", "Send"))
        self.subject_edit.setPlaceholderText(_translate("messenger", "Subject"))