from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout
from screens.feature_block import feature_widget
from screens.playlist import PlayList


class RootWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.feature_widget = None
        self._playlist_screen = PlayList()  # левый блок
        self.setWindowTitle('Музыкальный проигрыватель')
        self.resize(1000, 700)

        ### ГЛОБАЛЬНЫЕ ЗНАЧЕНИЯ
        self.is_visible_track_list = True
        self.main_layout = QHBoxLayout()

        ### ВЕРСТКА
        # Рендерим виджеты
        self.render_widgets()

        ### СТИЛИ
        self.main_layout.setAlignment(Qt.AlignCenter)

       # Устанавливаем основной layout
        self.setLayout(self.main_layout)

    def handle_toggle_playlist(self):
        # Переключение видимости плейлиста
        self.is_visible_track_list = not self.is_visible_track_list
        self.render_widgets()

    def render_widgets(self):
        # Очищаем предыдущие виджеты из main_layout

        while self.main_layout.count():
            item = self.main_layout.takeAt(0)
            if item.widget():
                item.widget().setParent(None)
                
        self.feature_widget = feature_widget(not self.is_visible_track_list)  # правый блок
        self.feature_widget.to_call_toggle = self.handle_toggle_playlist  # явно указываем метод to_call_togle

        # нужно ли показывать левый блок
        if self.is_visible_track_list:
            self.main_layout.addWidget(self._playlist_screen, stretch=1)

        self.main_layout.addWidget(self.feature_widget, stretch=1)


app = QApplication([])
window = RootWindow()
window.show()
app.exec()