from PySide6.QtWidgets import QFrame


class MainImage(QFrame):
    def __init__(self,):
        super().__init__()
        ### РАЗМЕТКА

        ### СТИЛИ
        self.setFixedSize(400, 400)
        self.setStyleSheet('background-color: grey')


        ### ЛОГИКА

