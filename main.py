from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout
from screens.feature_screen import feature_widget
from screens.playlist_screen import PlayList
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput

class RootWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Музыкальный проигрыватель')
        self.resize(1000, 700)

        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput(self)
        self.player.setAudioOutput(self.audio_output)

        ### ГЛОБАЛЬНЫЕ СОСТОЯНИЯ
        self.is_visible_track_list = True
        self.is_playing = False
        self.card_data = []

        self.default_track = {"id": -1, "title": '', "author": '', "source": ''}
        self.current_track = self.default_track

        self.main_layout = QHBoxLayout()
        self.feature_screen = None # правый блок
        self._playlist_screen = None

        ### ВЕРСТКА
        self.render_widgets()

        ### СТИЛИ
        self.main_layout.setAlignment(Qt.AlignCenter)

        # Устанавливаем основной layout
        self.setLayout(self.main_layout)

    #изменить текущий трек
    def handle_choose_current_track(self, new_current_track):
        if new_current_track == self.current_track: #если трек тот-же - ставим на паузу, иначе изменяем проигрывание
            if self.player.isPlaying():
                self.player.pause()
                self.is_playing = False
                self.render_widgets()
            else:
                self.player.play()
                self.is_playing = True
                self.render_widgets()
        else:
            self.current_track = new_current_track
            self.player.setSource(self.current_track["source"])
            self.player.play()
            self.is_playing = True
            self.render_widgets()

    #воспроизвести
    def handle_play(self):
        # защита от дурочка
        if len(self.card_data) > 0:
            #ничего не играет - ставим первый
            if self.current_track == self.default_track:
                self.handle_choose_current_track(self.card_data[0])
            else:
                self.player.play()
                self.is_playing = True
                self.render_widgets()

    #пауза
    def handle_pause(self):
        self.player.pause()
        self.is_playing = False
        self.render_widgets()

    def handle_next(self):


    #добавить трек
    def handle_add_new_track(self, track):
        self.card_data.append(track)
        self.render_widgets()

    #удалить трек
    def handle_remove_track(self, id_of_track):
        #очистка плеера, если удален текущий
        if id_of_track == self.current_track["id"]:
            self.player.pause()
            self.is_playing = False
            self.current_track = self.default_track

        #интерфейс
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

    #рендер / ререндер
    def render_widgets(self):
        while self.main_layout.count():
            item = self.main_layout.takeAt(0)
            if item.widget():
                item.widget().setParent(None)

        self._playlist_screen = PlayList(self.card_data, self.current_track)
        self.feature_screen = feature_widget(not self.is_visible_track_list, self.current_track, self.is_playing)  # правый блок всегда открыт

        # нужно ли показывать левый блок
        if self.is_visible_track_list:
            self.main_layout.addWidget(self._playlist_screen, stretch=1)

        ### ОБРАБОТЧИКИ СОБЫТИЙ
        self.feature_screen.to_call_toggle = self.handle_toggle_playlist  # явно указываем метод to_call_toggle
        self.feature_screen.to_call_play = self.handle_play  # явно указываем метод to_call_play
        self.feature_screen.to_call_pause = self.handle_pause  # явно указываем метод to_call_pause

        self._playlist_screen.emitAddNewTrack.connect(self.handle_add_new_track)
        self._playlist_screen.emitDeleteTrack.connect(self.handle_remove_track)
        self._playlist_screen.emitChooseCurrentTrack.connect(self.handle_choose_current_track)

        self.main_layout.addWidget(self.feature_screen, stretch=1)


app = QApplication([])
window = RootWindow()
window.show()
app.exec()