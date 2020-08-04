from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialogButtonBox
import random

global msg
msg = None



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(332, 367)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(11, 50, 100, 100))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(111, 50, 100, 100))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(211, 50, 100, 100))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(11, 150, 100, 100))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(111, 150, 100, 100))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(211, 150, 100, 100))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(11, 250, 100, 100))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(111, 250, 100, 100))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(211, 250, 100, 100))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(21, 10, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(21, 30, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(131, 10, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(131, 30, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 20, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(220, 20, 71, 16))
        self.label_6.setObjectName("label_6")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(240, 10, 71, 41))
        self.pushButton_10.setObjectName("pushButton_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.move = 0
        self.comp_move = [self.comp_one,self.comp_two,self.comp_three,self.comp_four,self.comp_five,self.comp_six,self.comp_seven,self.comp_eight,self.comp_nine]
        self.board = [[5,5,5],
                    [5, 5, 5],
                    [5, 5, 5]]
        self.my_score = 0
        self.comp_score = 0
        self.draw = 0
        self.moves = 0

        self.pushButton.clicked.connect(self.one)
        self.pushButton_2.clicked.connect(self.two)
        self.pushButton_3.clicked.connect(self.three)
        self.pushButton_4.clicked.connect(self.four)
        self.pushButton_5.clicked.connect(self.five)
        self.pushButton_6.clicked.connect(self.six)
        self.pushButton_7.clicked.connect(self.seven)
        self.pushButton_8.clicked.connect(self.eight)
        self.pushButton_9.clicked.connect(self.nine)
        self.pushButton_10.clicked.connect(self.stats)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tic tac"))
        self.pushButton.setText(_translate("MainWindow", "_"))
        self.pushButton_2.setText(_translate("MainWindow", "_"))
        self.pushButton_3.setText(_translate("MainWindow", "_"))
        self.pushButton_4.setText(_translate("MainWindow", "_"))
        self.pushButton_5.setText(_translate("MainWindow", "_"))
        self.pushButton_6.setText(_translate("MainWindow", "_"))
        self.pushButton_7.setText(_translate("MainWindow", "_"))
        self.pushButton_8.setText(_translate("MainWindow", "_"))
        self.pushButton_9.setText(_translate("MainWindow", "_"))
        self.pushButton_10.setText(_translate("MainWindow", "Stats"))
        self.label.setText(_translate("MainWindow", "Your Score"))
        self.label_2.setText(_translate("MainWindow", "Computer Score"))
        self.label_3.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "Draw"))
        self.label_6.setText(_translate("MainWindow", "0"))


    def one(self):
        if self.pushButton.text()=='_':
            self.pushButton.setText("X")
            self.board[0][0]=1
            self.moves += 1
            self.pushButton.repaint()
            self.user_win()


    def two(self):
        if self.pushButton_2.text()=='_':
            self.pushButton_2.setText("X")
            self.board[0][1]=1
            self.moves += 1
            self.pushButton_2.repaint()
            self.user_win()


    def three(self):
        if self.pushButton_3.text()=='_':
            self.pushButton_3.setText("X")
            self.board[0][2]=1
            self.moves += 1
            self.pushButton_3.repaint()
            self.user_win()


    def four(self):
        if self.pushButton_4.text()=='_':
            self.pushButton_4.setText("X")
            self.board[1][0]=1
            self.moves += 1
            self.pushButton_4.repaint()
            self.user_win()


    def five(self):
        if self.pushButton_5.text()=='_':
            self.pushButton_5.setText("X")
            self.board[1][1]=1
            self.moves += 1
            self.pushButton_5.repaint()
            self.user_win()


    def six(self):
        if self.pushButton_6.text()=='_':
            self.pushButton_6.setText("X")
            self.board[1][2]=1
            self.moves += 1
            self.pushButton_6.repaint()
            self.user_win()


    def seven(self):
        if self.pushButton_7.text()=='_':
            self.pushButton_7.setText("X")
            self.board[2][0]=1
            self.moves += 1
            self.pushButton_7.repaint()
            self.user_win()


    def eight(self):
        if self.pushButton_8.text()=='_':
            self.pushButton_8.setText("X")
            self.board[2][1]=1
            self.moves += 1
            self.pushButton_8.repaint()
            self.user_win()


    def nine(self):
        if self.pushButton_9.text()=='_':
            self.pushButton_9.setText("X")
            self.board[2][2]=1
            self.moves += 1
            self.pushButton_9.repaint()
            self.user_win()


    def comp_one(self):
        if self.pushButton.text()=='_':
            self.pushButton.setText("O")
            self.board[0][0]=0
            self.pushButton.repaint()
            self.comp_win()
        else:
            self.comp_move.remove(self.comp_one)
            self.computer_pick()


    def comp_two(self):
        if self.pushButton_2.text()=='_':
            self.pushButton_2.setText("O")
            self.board[0][1]=0
            self.pushButton_2.repaint()
            self.comp_win()
        else:
            self.comp_move.remove(self.comp_two)
            self.computer_pick()


    def comp_three(self):
        if self.pushButton_3.text()=='_':
            self.pushButton_3.setText("O")
            self.board[0][2]=0
            self.pushButton_3.repaint()
            self.comp_win()
        else:
            self.comp_move.remove(self.comp_three)
            self.computer_pick()


    def comp_four(self):
        if self.pushButton_4.text()=='_':
            self.pushButton_4.setText("O")
            self.board[1][0]=0
            self.pushButton_4.repaint()
            self.comp_win()
        else:
            self.comp_move.remove(self.comp_four)
            self.computer_pick()


    def comp_five(self):
        if self.pushButton_5.text()=='_':
            self.pushButton_5.setText("O")
            self.board[1][1]=0
            self.pushButton_5.repaint()
            self.comp_win()
        else:
            self.comp_move.remove(self.comp_five)
            self.computer_pick()


    def comp_six(self):
        if self.pushButton_6.text()=='_':
            self.pushButton_6.setText("O")
            self.board[1][2]=0
            self.pushButton_6.repaint()
            self.comp_win()
        else:
            self.comp_move.remove(self.comp_six)
            self.computer_pick()


    def comp_seven(self):
        if self.pushButton_7.text()=='_':
            self.pushButton_7.setText("O")
            self.board[2][0]=0
            self.pushButton_7.repaint()
            self.comp_win()
        else:
            self.comp_move.remove(self.comp_seven)
            self.computer_pick()


    def comp_eight(self):
        if self.pushButton_8.text()=='_':
            self.pushButton_8.setText("O")
            self.board[2][1]=0
            self.pushButton_8.repaint()
            self.comp_win()
        else:
            self.comp_move.remove(self.comp_eight)
            self.computer_pick()


    def comp_nine(self):
        if self.pushButton_9.text()=='_':
            self.pushButton_9.setText("O")
            self.board[2][2]=0
            self.pushButton_9.repaint()
            self.comp_win()
        else:
            self.comp_move.remove(self.comp_nine)
            self.computer_pick()


    def computer_pick(self):
        if len(self.comp_move) > 0:
            move = random.choice(self.comp_move)
            move()
            if move in self.comp_move:
                self.comp_move.remove(move)
                self.moves += 1


    def check_draw(self):
        if self.moves == 9:
            msg = "It's a draw."
            self.draw += 1
            self.label_6.setText(str(self.draw))
            Dialog.show()
            ui1.label.setText(msg)


    def user_win(self):
        if self.board[0] == [1,1,1] or self.board[1] == [1,1,1] or self.board[2] == [1,1,1] or (self.board[0][0] == 1 and self.board[1][0] == 1 and self.board[2][0] == 1) or (self.board[0][1] == 1 and self.board[1][1] == 1 and self.board[2][1] == 1) or (self.board[0][2] == 1 and self.board[1][2] == 1 and self.board[2][2] == 1) or (self.board[0][0] == 1 and self.board[1][1] == 1 and self.board[2][2] == 1) or (self.board[0][2] == 1 and self.board[1][1] == 1 and self.board[2][0] == 1):
            msg = "You've won!"
            self.my_score += 1
            self.label_3.setText(str(self.my_score))
            Dialog.show()
            ui1.label.setText(msg)
        else:
            self.computer_pick()
            self.check_draw()


    def comp_win(self):
        if (self.board[0]==[0,0,0] or self.board[1]==[0,0,0] or self.board[2]==[0,0,0]) or (self.board[0][0] == 0 and self.board[1][0] == 0 and self.board[2][0] == 0) or (self.board[0][1] == 0 and self.board[1][1] == 0 and self.board[2][1] == 0) or (self.board[0][2] == 0 and self.board[1][2] == 0 and self.board[2][2] == 0) or (self.board[0][0] == 0 and self.board[1][1] == 0 and self.board[2][2] == 0) or (self.board[0][2] == 0 and self.board[1][1] == 0 and self.board[2][0] == 0):
            msg = "The computer has won. You've lost."
            self.comp_score += 1
            self.label_4.setText(str(self.comp_score))
            Dialog.show()
            ui1.label.setText(msg)
        else:
            self.check_draw()


    def game_restart(self):
        self.moves = 0
        Dialog.hide()
        self.pushButton.setText("_")
        self.pushButton_2.setText("_")
        self.pushButton_3.setText("_")
        self.pushButton_4.setText("_")
        self.pushButton_5.setText("_")
        self.pushButton_6.setText("_")
        self.pushButton_7.setText("_")
        self.pushButton_8.setText("_")
        self.pushButton_9.setText("_")
        self.board = [[5,5,5],
                    [5, 5, 5],
                    [5, 5, 5]]
        self.comp_move = [self.comp_one,self.comp_two,self.comp_three,self.comp_four,self.comp_five,self.comp_six,self.comp_seven,self.comp_eight,self.comp_nine]


    def exit(self):
        exit()


    def stats(self):
        self.total = self.comp_score+self.my_score+self.draw
        if self.total == 0:
            self.comp_perc = 0
            self.my_perc = 0
            self.draw_perc = 0
        else:
            self.comp_perc = self.comp_score / (self.total / 100)
            self.my_perc = self.my_score / (self.total / 100)
            self.draw_perc = self.draw / (self.total / 100)
        ui2.label.setText("You have played "+str(self.total)+" games")
        ui2.label_5.setText(str(format(self.my_perc,'.1f')))
        ui2.label_6.setText(str(format(self.comp_perc,'.1f')))
        ui2.label_7.setText(str(format(self.draw_perc,'.1f')))
        MainWindow1.show()



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(363, 100)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 60, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.button(QDialogButtonBox.Ok).setText("New Game")
        self.buttonBox.button(QDialogButtonBox.Cancel).setText("Exit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 341, 41))
        self.label.setObjectName("label")
        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(ui.game_restart)
        self.buttonBox.rejected.connect(ui.exit)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "End of game"))
        self.label.setText(_translate("Dialog", msg))



class Stats(object):
    def setupUi(self, MainWindow1):
        MainWindow1.setObjectName("MainWindow1")
        MainWindow1.resize(211, 129)
        self.centralwidget = QtWidgets.QWidget(MainWindow1)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 161, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 131, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 151, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 70, 91, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(170, 30, 60, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(170, 50, 60, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(170, 70, 60, 16))
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 90, 191, 32))
        self.pushButton.setObjectName("pushButton")
        MainWindow1.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

        self.pushButton.clicked.connect(self.close)


    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("MainWindow1", "Stats"))
        self.label.setText(_translate("MainWindow1", "You have played 0 games"))
        self.label_2.setText(_translate("MainWindow1", "Your win rate (%):"))
        self.label_3.setText(_translate("MainWindow1", "Computer win rate (%):"))
        self.label_4.setText(_translate("MainWindow1", "Draw rate (%):"))
        self.label_5.setText(_translate("MainWindow1", "0"))
        self.label_6.setText(_translate("MainWindow1", "0"))
        self.label_7.setText(_translate("MainWindow1", "0"))
        self.pushButton.setText(_translate("MainWindow1", "Close"))


    def close(self):
        MainWindow1.hide()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('tic_tac_toe_l.png'))
    app2 = QtWidgets.QApplication(sys.argv)
    app3 = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow1 = QtWidgets.QMainWindow()
    Dialog = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui1 = Ui_Dialog()
    ui1.setupUi(Dialog)
    ui2 = Stats()
    ui2.setupUi(MainWindow1)
    MainWindow.show()
    Dialog.hide()
    MainWindow1.hide()
    sys.exit(app.exec_())
    sys.exit(app2.exec_())
    sys.exit(app3.exec_())
