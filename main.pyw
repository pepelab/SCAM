import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5 import QtCore, QtGui, QtWidgets
from login import Ui_login
from messenger import Ui_messenger


#==================== ЗАПУСК LOGIN ====================
app = QtWidgets.QApplication(sys.argv)
login = QtWidgets.QMainWindow()
login_ui = Ui_login()
login_ui.setupUi(login)
login.show()


#==================== ЗАПУСК MESSENGER ====================
messenger = QtWidgets.QMainWindow()
messenger_ui = Ui_messenger()
messenger_ui.setupUi(messenger)


def open_messenger():
    login.close() 
    title_edit()
    messenger.show()

def title_edit():      # ИЗМЕНИТЬ ИМЯ MESSENGER НА EMAIL
    messenger.setWindowTitle(login_ui.email_edit.text())


#==================== ОТПРАВКА ====================
def email():
    addr_from = login_ui.email_edit.text()              # EMAIL
    password  = login_ui.password_edit.text()           # PASSWORD
    addr_to   = messenger_ui.to_edit.text()             # КОМУ
    subject   = messenger_ui.subject_edit.text()        # ТЕМА
    body      = messenger_ui.message_edit.toPlainText() # ТЕКСТ

    msg = MIMEMultipart()
    msg['From']    = addr_from
    msg['To']      = addr_to
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.starttls()                       
    server.login(addr_from, password)
    server.send_message(msg)
    server.quit()


#==================== КНОПКИ ====================
login_ui.login_button.clicked.connect(open_messenger)   # КНОПКА LOGIN
messenger_ui.send_button.clicked.connect(email)         # КНОПКА SEND


sys.exit(app.exec_())