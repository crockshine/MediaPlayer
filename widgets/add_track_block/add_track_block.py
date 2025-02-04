from PySide6.QtWidgets import QHBoxLayout, QPushButton
from PySide6.QtCore import Qt, Signal


class AddTrackBlock(QHBoxLayout):
    emitAddNewTrack = Signal(int, str, str)

    def __init__(self):
        super().__init__()
        self.i = 0

        ## РАЗМЕТКА
        button = QPushButton('Добавить')
        button.setFixedSize(200, 50)
        button.setStyleSheet('background-color: black; border-radius: 20px; color: white; font-size: 16px; font-weight: bold')
        self.addWidget(button)

        ##  СТИЛИ
        self.setAlignment(button, Qt.AlignCenter)  # Выравнивание кнопки по центру

        ## ЛОГИКА
        button.clicked.connect(self.add_track)

    def add_track(self):
        self.i += 1
        self.emitAddNewTrack.emit(self.i, f'Новый трек{self.i}', 'Новый автор')
