from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout


class FeatureLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()
        ## ДАННЫЕ, КОМПОНЕНТЫ
        toggle_playlist_btn = QPushButton('<-')
        track_image = QWidget()

        btn_layout = QHBoxLayout()
        center_info_layout = QVBoxLayout()

        ## РАЗМЕТКА
        btn_layout.addWidget(toggle_playlist_btn)
        center_info_layout.addWidget(track_image)

        self.addLayout(btn_layout)
        self.addLayout(center_info_layout)
        self.addStretch()

        ## СТИЛИ
        btn_layout.setAlignment(Qt.AlignLeft)
        center_info_layout.setAlignment(Qt.AlignCenter)

        toggle_playlist_btn.setMaximumWidth(40)
        toggle_playlist_btn.setMaximumHeight(40)
        track_image.setFixedSize(400, 400)

        track_image.setStyleSheet('background-color: grey')

        self.setAlignment(Qt.AlignCenter)

        ## ЛОГИКА
        toggle_playlist_btn.clicked.connect(self.notify_parent)

    def notify_parent(self):
        parent_widget = self.parentWidget()
        if parent_widget and hasattr(parent_widget, 'to_call_toggle'):
            parent_widget.to_call_toggle()


def layout_to_widget():
    w = QWidget()
    layout = FeatureLayout()
    w.setStyleSheet('background-color: rgba(0,0,0, 0.2)')
    w.setLayout(layout)
    return w
