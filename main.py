from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout
from screens.feature_screen import feature_widget
from screens.playlist_screen import PlayList


class RootWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Музыкальный проигрыватель')
        self.resize(1000, 700)

        ### ГЛОБАЛЬНЫЕ СОСТОЯНИЯ
        self.is_visible_track_list = True
        self.card_data = []
        self.current_track = {"id": 0, "title": '', "author": ''}

        self.main_layout = QHBoxLayout()
        self.feature_screen = None # правый блок
        self._playlist_screen = None

        ### ВЕРСТКА
        self.render_widgets()

        ### СТИЛИ
        self.main_layout.setAlignment(Qt.AlignCenter)

        # Устанавливаем основной layout
        self.setLayout(self.main_layout)

    def handle_choose_current_track(self, new_current_track):
        self.current_track = new_current_track
        self.render_widgets()

    #добавить трек
    def handle_add_new_track(self, track):
        self.card_data.append(track)
        self.render_widgets()

    #удалить трек
    def handle_remove_track(self, id_of_track):
        new_data = []
        for track in self.card_data:
            if track["id"] != id_of_track:
                new_data.append(track)
        self.card_data = new_data
        self.render_widgets()

    # Переключение видимости плейлиста
    def handle_toggle_playlist(self):
        self.is_visible_track_list = not self.is_visible_track_list
        self.render_widgets()


    def render_widgets(self):
        while self.main_layout.count():
            item = self.main_layout.takeAt(0)
            if item.widget():
                item.widget().setParent(None)

        self._playlist_screen = PlayList(self.card_data, self.current_track)
        self.feature_screen = feature_widget(not self.is_visible_track_list, self.current_track)  # правый блок всегда открыт

        # нужно ли показывать левый блок
        if self.is_visible_track_list:
            self.main_layout.addWidget(self._playlist_screen, stretch=1)

        ### ОБРАБОТЧИКИ СОБЫТИЙ
        self.feature_screen.to_call_toggle = self.handle_toggle_playlist  # явно указываем метод to_call_toggle
        self._playlist_screen.emitAddNewTrack.connect(self.handle_add_new_track)
        self._playlist_screen.emitDeleteTrack.connect(self.handle_remove_track)
        self._playlist_screen.emitChooseCurrentTrack.connect(self.handle_choose_current_track)

        self.main_layout.addWidget(self.feature_screen, stretch=1)


app = QApplication([])
window = RootWindow()
window.show()
app.exec()