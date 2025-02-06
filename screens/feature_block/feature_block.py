from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout

class FeatureLayout(QVBoxLayout):
    emitTogglePlaylist = Signal()

    def __init__(self):
        super().__init__()
        toggle_playlist_button = QPushButton('<-')
        track_image = QWidget()

        self.addWidget(toggle_playlist_button)
        self.addWidget(track_image)

        self.addStretch()

        track_image.setFixedSize(400, 400)
        track_image.setStyleSheet('background-color: grey')

        toggle_playlist_button.clicked.connect(self.handle_toggle_playlist)

    def handle_toggle_playlist(self):
        self.emitTogglePlaylist.emit()


class FeatureWidget(QWidget):
    emitTogglePlaylist = Signal()

    def __init__(self):
        super().__init__()
        feature_layout = FeatureLayout()
        feature_layout.emitTogglePlaylist.connect(self.emitTogglePlaylist.emit)
        self.setLayout(feature_layout)
