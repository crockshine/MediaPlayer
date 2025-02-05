from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout

from screens.feature_block import FeatureBlock
from screens.playlist import PlayList


class RootWindow(QWidget):
    def __init__(self):
        super().__init__()
        ### ПЕРЕМЕННЫЕ, ГЛОБАЛЬНЫЕ ЗНАЧЕНИЯ
        self.setWindowTitle('Музыкальный проигрыватель')
        self.resize(1000, 700)

        self.is_visible_track_list = True
        self.main_layout = QHBoxLayout()

        ### ВЕРСТКА
        self._feature_block = FeatureBlock()#левый блок
        self._playlist_screen = PlayList()#правый блок
        self.render_widgets()#рендер

        ### СТИЛИ
        self._playlist_screen.setMinimumWidth(250)
        self._feature_block.setMinimumWidth(250)

        ### ОБРАБОТЧИКИ СОБЫТИЙ
        self._feature_block.emitTogglePlaylist.connect(self.handle_toggle_playlist)

        ### КОНЕЦ
        self.setLayout(self.main_layout)

    def render_widgets(self):
        while self.main_layout.count():
            item = self.main_layout.takeAt(0)
            if item.widget():
                item.widget().setParent(None)

        if self.is_visible_track_list:
            self.main_layout.addWidget(self._playlist_screen)  # левый блок

        self.main_layout.addWidget(self._feature_block) #необходимо всегда оставлять правый блок

    def handle_toggle_playlist(self):
        self.is_visible_track_list = not self.is_visible_track_list
        self.render_widgets()


app = QApplication([])  #глобальный обработчик событий
window = RootWindow()  #корень приложения. экземпляр QWidget
window.show()  #показать корень
app.exec()  #что-то типа event loop
