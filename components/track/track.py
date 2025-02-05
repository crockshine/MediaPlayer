from PySide6.QtCore import Signal
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QWidget, QFrame, QPushButton


class TrackCard(QFrame):
    emitDelete = Signal(int)

    def __init__(self, id_of_track, title, author):
        super().__init__()
        self.id = id_of_track

        ### РАЗМЕТКА
        card_layout = QHBoxLayout()  #лэйаут всей карточки
        text_info_layout = QVBoxLayout()  #лэйаут для текстового блока

        image_block = QWidget()  #виджет картинки
        title_label = QLabel(title)  #текст
        author_label = QLabel(author)  #текст
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
        title_label.setStyleSheet("font-weight: bold; font-size: 16px; border: none")
        author_label.setStyleSheet("font-size: 12px; border: none")
        close_button.setStyleSheet("font-weight: bold; font-size: 16px; margin-right: 10px")

        self.setStyleSheet("background-color: white; border-radius: 20px; ")

        ### ЛОГИКА
        close_button.clicked.connect(self.handle_delete_track)

    def handle_delete_track(self):
        self.emitDelete.emit(self.id)
