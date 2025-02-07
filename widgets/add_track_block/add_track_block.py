from random import random, randint

from PySide6.QtWidgets import QHBoxLayout, QPushButton
from PySide6.QtCore import Qt, Signal


class AddTrackBlock(QHBoxLayout):
    emitAddNewTrack = Signal(dict)

    def __init__(self):
        super().__init__()
        self.i = 0

        ## РАЗМЕТКА
        button = QPushButton('Добавить')
        button.setFixedSize(200, 50)
        button.setStyleSheet('background-color: black; border-radius: 10px; color: white; font-size: 16px; font-weight: bold')
        self.addWidget(button)

        ##  СТИЛИ
        self.setAlignment(button, Qt.AlignCenter)  # Выравнивание кнопки по центру

        ## ЛОГИКА
        button.clicked.connect(self.add_track)

    def add_track(self):
        rand = randint(1, 129929)
        new_track = {"id": rand, "title": f'Новый трек {rand}', "author": 'Новый автор'}
        self.emitAddNewTrack.emit(new_track)
