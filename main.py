from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout

from screens.playlist import PlayList


#класс корня приложения
class RootWindow(QWidget):  #наследумся от QWidget
    def __init__(self, /):
        super().__init__()  #вызываем конструктор QWidget

        self.setWindowTitle('Музыкальный проигрыватель')
        self.resize(1000, 700)

        #синий блок
        blue_block = QWidget()
        blue_block.setStyleSheet('background-color: grey;')

        #лэйаут экрана
        layout = QHBoxLayout()

        _playlist_screen = PlayList()
        layout.addLayout(_playlist_screen)  #левый блок
        layout.addWidget(blue_block) #правый блок

        #добавляем лэйаут в рут
        self.setLayout(layout)


app = QApplication([])  #глобальный обработчик событий
window = RootWindow()  #корень приложения. экземпляр QWidget
window.show()  #показать корень
app.exec()  #что-то типа event loop
