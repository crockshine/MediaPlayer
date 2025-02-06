from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout
from screens.feature_block import FeatureWidget  # наш новый виджет с encapsulated layout
from screens.playlist import PlayList  # допустим, у вас уже есть этот класс

class RootWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Музыкальный проигрыватель')
        self.resize(1000, 700)

        # Глобальные переменные
        self.is_visible_track_list = True
        self.main_layout = QHBoxLayout()

        ### ВЕРСТКА
        self.feature_widget = FeatureWidget()  # правый блок
        self._playlist_screen = PlayList()      # левый блок

        # Рендерим виджеты
        self.render_widgets()

        ### СТИЛИ
        self._playlist_screen.setMinimumWidth(250)
        self.feature_widget.setMinimumWidth(250)
        self._playlist_screen.setMaximumWidth(500)
        self.feature_widget.setMaximumWidth(500)


        ### ОБРАБОТЧИКИ СОБЫТИЙ
        self.feature_widget.emitTogglePlaylist.connect(self.handle_toggle_playlist)

        # Устанавливаем основной layout
        self.setLayout(self.main_layout)

    def render_widgets(self):
        # Очищаем предыдущие виджеты из основного layout
        while self.main_layout.count():
            item = self.main_layout.takeAt(0)
            if item.widget():
                item.widget().setParent(None)

        if self.is_visible_track_list:
            self.main_layout.addWidget(self._playlist_screen)
            self.main_layout.setAlignment(Qt.AlignCenter)# левый блок
        else:
            self.main_layout.setAlignment(Qt.AlignLeft)


        self.main_layout.addWidget(self.feature_widget)  # правый блок всегда добавляем

    def handle_toggle_playlist(self):
        # Переключение видимости плейлиста
        self.is_visible_track_list = not self.is_visible_track_list
        self.render_widgets()


app = QApplication([])
window = RootWindow()
window.show()
app.exec()
