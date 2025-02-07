from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QWidget, QFrame, QPushButton


class TrackCard(QFrame):
    emitDelete = Signal(int)
    emitChooseCurrentTrack = Signal(dict)

    def __init__(self, track: dict, is_current:bool):
        super().__init__()
        self.track = track

        ### РАЗМЕТКА
        card_layout = QHBoxLayout()  #лэйаут всей карточки
        text_info_layout = QVBoxLayout()  #лэйаут для текстового блока

        image_block = QWidget()  #виджет картинки
        title_label = QLabel(self.track["title"])  #текст
        author_label = QLabel(self.track["author"])  #текст
        close_button = QPushButton('X') #крестик

        #заполняем лэйаут текста
        text_info_layout.addWidget(title_label)
        text_info_layout.addWidget(author_label)

        #заполняем лэйаут карточки
        card_layout.addWidget(image_block)
        card_layout.addLayout(text_info_layout)
        card_layout.addStretch()
        card_layout.addWidget(close_button)

        self.setLayout(card_layout) #вставляем в карточку - лэйаут карточки

        ### СТИЛИ
        card_layout.setSpacing(10)
        text_info_layout.setSpacing(0)

        image_block.setFixedSize(60, 60)
        title_label.setFixedHeight(20)
        author_label.setFixedHeight(20)

        image_block.setStyleSheet("border-radius: 10px; background: grey; border: none")
        title_label.setStyleSheet("font-weight: bold; font-size: 16px; border: none; background-color: transparent")
        author_label.setStyleSheet("font-size: 12px; border: none; background-color: transparent")
        close_button.setStyleSheet("font-weight: bold; font-size: 16px; margin-right: 10px")

        close_button.setCursor(Qt.PointingHandCursor)
        self.setCursor(Qt.PointingHandCursor)

        if is_current:
            self.setStyleSheet("background-color: white; border-radius: 20px; ")
        else:
            self.setStyleSheet("background-color: rgb(220, 220, 220); border-radius: 20px; ")

        ### ЛОГИКА
        close_button.clicked.connect(self.handle_delete_track)

    def handle_delete_track(self):
        self.emitDelete.emit(self.track["id"])

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.emitChooseCurrentTrack.emit(self.track)

