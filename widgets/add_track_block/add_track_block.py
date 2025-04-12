from random import randint

from PySide6.QtWidgets import QHBoxLayout, QPushButton, QFileDialog
from PySide6.QtCore import Qt, Signal
import os
import mutagen
from mutagen import FileType, MutagenError

from widgets.utils import get_audio_metadata


def get_substring_before_last_dot(fp):
    file_name = os.path.basename(fp)
    last_dot_index = file_name.rfind('.')  # макс вхождение
    if last_dot_index != -1:
        return file_name[:last_dot_index]
    return file_name

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
            'background-color: black; '
            'border-radius: 10px; '
            'color: white; '
            'font-size: 16px; '
            'font-weight: bold'
        )
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
            print(file_path)
            # TODO сделать проверку сигнатуры , а не по формату
            [artist, title] = get_audio_metadata(file_path, 'Неизвестен', fallback_title = default_title)

            new_track = {
                        "id": randint(1, 129929),
                        "title": title,
                        "author": artist,
                        "source": file_path
            }
            self.emitAddNewTrack.emit(new_track)
