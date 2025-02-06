from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout


class FeatureLayout(QVBoxLayout):
    emitTogglePlaylist = Signal()

    def __init__(self):
        super().__init__()
        toggle_playlist_btn = QPushButton('<-')
        track_image = QWidget()

        btn_layout = QHBoxLayout()
        center_info_layout = QVBoxLayout()

        btn_layout.addWidget(toggle_playlist_btn)
        center_info_layout.addWidget(track_image)

        self.addLayout(btn_layout)
        self.addLayout(center_info_layout)

        self.addStretch()

        btn_layout.setAlignment(Qt.AlignLeft)

        toggle_playlist_btn.setMaximumWidth(40)
        toggle_playlist_btn.setMaximumHeight(40)

        track_image.setFixedSize(400, 400)
        track_image.setStyleSheet('background-color: grey')
        self.setAlignment(Qt.AlignCenter)
        toggle_playlist_btn.clicked.connect(self.handle_toggle_playlist)

    def handle_toggle_playlist(self):
        self.emitTogglePlaylist.emit()


class FeatureWidget(QWidget):
    emitTogglePlaylist = Signal()

    def __init__(self):
        super().__init__()
        feature_layout = FeatureLayout()
        feature_layout.emitTogglePlaylist.connect(self.emitTogglePlaylist.emit)
        self.setLayout(feature_layout)
