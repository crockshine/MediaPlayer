from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout


class AboutTrackLayout(QVBoxLayout):
    def __init__(self, title: str, author: str):
        super().__init__()
        title_label = QLabel(title)
        author_label = QLabel(author)

        title_layout = QHBoxLayout()
        author_layout = QHBoxLayout()

        ### РАЗМЕТКА
        title_layout.addWidget(title_label)
        author_layout.addWidget(author_label)

        self.addLayout(title_layout)
        self.addLayout(author_layout)

        ### СТИЛИ
        title_label.setStyleSheet('font-size: 16px; font-weight: bold; background-color: transparent')
        author_label.setStyleSheet('font-size: 12px; opacity: 0.5; background-color: transparent')
        self.setSpacing(0)
        title_layout.setAlignment(Qt.AlignCenter)
        author_layout.setAlignment(Qt.AlignCenter)

        ### ЛОГИКА

