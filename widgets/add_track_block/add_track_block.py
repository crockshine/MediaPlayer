from random import random, randint

from PySide6.QtWidgets import QHBoxLayout, QPushButton, QFileDialog
from PySide6.QtCore import Qt, Signal
import os
from utils import read_mp3


class AddTrackBlock(QHBoxLayout):
    emitAddNewTrack = Signal(dict)

    def __init__(self):
        super().__init__()

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
        file_path, _ = QFileDialog.getOpenFileName(
            None, "Выберите аудиофайл", "", "Audio Files (*.mp3 *.wav *.flac)"
        )
        _, file_extension = os.path.splitext(file_path)
        if file_path:
            if file_extension == '.mp3':
                mp3_track_data = read_mp3(file_path)
                rand = randint(1, 129929)
                new_track = {"id": rand, "title": mp3_track_data["title"], "author": mp3_track_data["author"], "source": file_path}
                self.emitAddNewTrack.emit(new_track)

        
