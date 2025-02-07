from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QHBoxLayout, QPushButton


class FeatureButtonsLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()
        shuffle_btn = QPushButton()
        repeat_btn = QPushButton()
        prev_btn = QPushButton()
        pause_btn = QPushButton()
        next_btn = QPushButton()
        equalaizer_btn = QPushButton()
        volume_btn = QPushButton()

        shuffle_btn.setIcon(QIcon('assets/shuffle.svg'))
        repeat_btn.setIcon(QIcon('assets/repeat.svg'))
        prev_btn.setIcon(QIcon('assets/rewind.svg'))
        pause_btn.setIcon(QIcon('assets/pause.svg'))
        next_btn.setIcon(QIcon('assets/fast-forward.svg'))
        equalaizer_btn.setIcon(QIcon('assets/waves.svg'))
        volume_btn.setIcon(QIcon('assets/volume-2.svg'))

        ### РАЗМЕТКА
        btns = [
            shuffle_btn, repeat_btn, prev_btn, pause_btn, next_btn, equalaizer_btn, volume_btn
        ]

        for btn in btns:
            self.addWidget(btn)

        ### СТИЛИ
        large_btns = {prev_btn, pause_btn, next_btn}

        for btn in btns:
            btn.setCursor(Qt.PointingHandCursor)
            btn.setStyleSheet('background-color: transparent')

            if btn in large_btns:
                btn.setIconSize(QSize(32,32))
            else:
                btn.setIconSize(QSize(22,22))


        self.setSpacing(12)
        self.setAlignment(Qt.AlignCenter)

        ### ЛОГИКА

