from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox, QRadioButton, QHBoxLayout, QGroupBox, QButtonGroup
from random import shuffle
from random import randint
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
que = QLabel('Какой национальности не существует?')
main_win.resize(400, 200)
Buttn = QPushButton('Ответить')
RadioGroupBox = QGroupBox('Варианты ответа')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

RadioGroupBox.hide()
AnsGroupBox = QGroupBox('Результат теста')
Result = QLabel('Правильно/Неправильно')
Correct = QLabel('Правлиьный ответ')

layout_res = QVBoxLayout()
layout_res.addWidget(Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(Correct, alignment=(Qt.AlignHCenter))
AnsGroupBox.setLayout(layout_res)

main_layout1 = QHBoxLayout()
main_layout2 = QHBoxLayout()
main_layout3 = QHBoxLayout()
main_layout1.addWidget(que, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
main_layout2.addWidget(RadioGroupBox)
main_layout2.addWidget(AnsGroupBox)
main_layout3.addStretch(1)
main_layout3.addWidget(Buttn, stretch=2)
main_layout3.addStretch(1)

super_main_layout = QVBoxLayout()

super_main_layout.addLayout(main_layout1, stretch=2)
super_main_layout.addLayout(main_layout2, stretch=8)
super_main_layout.addStretch(1)
super_main_layout.addLayout(main_layout3, stretch=1)
super_main_layout.addStretch(1)
main_win.setLayout(super_main_layout)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    Buttn.setText('Следующий вопрос')

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    Buttn.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)


answers =[rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    que.setText(q.question)
    Correct.setText(q.right_answer)
    show_question()

questions_list = []
questions_list.append(Question('Выбери перевод слова переменная', 'variable', 'variation', 'changing', 'variant'))
questions_list.append(Question('Какой национальности не существует?', 'Смурфы', 'Энцы', 'Чулымцы', 'Алеуты'))
questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Испанский', 'Итальянский', 'Бразильский'))



def show_correct(res):
    Result.setText(res)
    show_result()


def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print(f'Рейтинг: {main_win.score/main_win.total*100}%')

def next_question():
    print(f'Статистика\n-Всего вопросов: {main_win.total}\n-Правильных ответов: {main_win.score}')
    if len(questions_list) > 0:
        cur_question = randint(0, len(questions_list) - 1)
        q = questions_list[cur_question]
        ask(q)
        questions_list.pop(cur_question)
    else:
        victory_win = QMessageBox()
        victory_win.setText('ВЫ ОТВЕТИЛИ НА ВСЕ ВОПРОСЫ')
        victory_win.exec_()

def click_OK():
    if Buttn.text() == 'Ответить':
        check_answer()
    else:
        next_question()

main_win.total = 0
main_win.score = 0
Buttn.clicked.connect(click_OK)
next_question()                
main_win.show()
app.exec_()