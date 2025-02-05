from PySide6.QtWidgets import QVBoxLayout, QWidget, QPushButton
from PySide6.QtCore import Signal


class FeatureBlock(QWidget):
    emitTogglePlaylist = Signal()

    def __init__(self):
        super().__init__()
        ### ПЕРЕМЕННЫЕ
        feature_block_layout = QVBoxLayout()
        toggle_playlist_button = QPushButton('<-')

        ### ВЕРСТКА
        feature_block_layout.addWidget(toggle_playlist_button)

        self.setLayout(feature_block_layout)

        ### ЛОГИКА
        toggle_playlist_button.clicked.connect(self.handle_toggle_playlist)

        ### СТИЛИ


    def handle_toggle_playlist(self):
        self.emitTogglePlaylist.emit()







