from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

def entrar():
    user = tela.login.text()
    password = tela.senha.text()
    if user == '' or password == '':
        QMessageBox.about(tela, 'Atenção', 'Preencha os campos solicitados!')
    elif user == 'admin' and password == '321':
        QMessageBox.about(tela, 'Atenção', 'Deseja salvar seus dados?')
        if tela.checkBox.isChecked():
            tela2.show()
            tela.close()
            #QMessageBox.about(tela, 'Usuário OK', 'Usuário aceito.')
    else:
        QMessageBox.about(tela, 'Atenção', 'Usuário e/ou senha inválido.')
    tela.login.setText("")
    tela.senha.setText("")

app = QtWidgets.QApplication([])
tela = uic.loadUi("acesso-reestrito.ui")
tela2 = uic.loadUi("bem-vindo.ui")
tela.botao.clicked.connect(entrar)
tela.show()
app.exec()
