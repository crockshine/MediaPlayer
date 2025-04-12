from random import random, randint

from PySide6.QtWidgets import QHBoxLayout, QPushButton, QFileDialog
from PySide6.QtCore import Qt, Signal
import os
from utils import read_mp3


def get_substring_before_last_dot(fp):
    file_name = os.path.basename(fp)
    last_dot_index = file_name.rfind('.')  # макс вхождение
    if last_dot_index != -1:
        return file_name[:last_dot_index]
    return file_name

def validation_data(data, field_type, default):
    return data[str(field_type)] \
        if data[str(field_type)] is not None and len(data[str(field_type)]) > 0\
        else default

class AddTrackBlock(QHBoxLayout):
    emitAddNewTrack = Signal(dict)

    def __init__(self):
        super().__init__()

        ## РАЗМЕТКА
        button = QPushButton('Добавить')
        self.addWidget(button)

        ##  СТИЛИ
        self.setAlignment(button, Qt.AlignCenter)  # Выравнивание кнопки по центру
        button.setStyleSheet(
            'background-color: black; border-radius: 10px; color: white; font-size: 16px; font-weight: bold')
        button.setFixedSize(200, 50)

        ## ЛОГИКА
        button.clicked.connect(self.add_track)

    def add_track(self):
        file_path, _ = QFileDialog.getOpenFileName(
            None, "Выберите аудиофайл", "", "Audio Files (*.mp3 *.wav *.flac *.ogg)"
        )
        _, file_extension = os.path.splitext(file_path)
        if file_path:

            default_title = get_substring_before_last_dot(file_path)

            # TODO сделать проверку сигнатуры , а не по формату

            if file_extension == '.mp3':
                mp3_track_data = read_mp3(file_path)
                rand = randint(1, 129929)
                new_track = {
                    "id": rand,
                    "title": validation_data(mp3_track_data, "title", default_title),
                    "author": validation_data(mp3_track_data, "author", 'Автор не найден'),
                    "source": file_path
                }

                self.emitAddNewTrack.emit(new_track)
