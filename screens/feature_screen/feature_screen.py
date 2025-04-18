from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QTransform, QPixmap
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout

from components.about_track import AboutTrackLayout
from components.feature_buttons import FeatureButtonsLayout
from components.main_image import MainImage
from components.timeline import Timeline


class FeatureLayout(QVBoxLayout):
    def __init__(self, is_full_screen: bool, current_track: dict, is_playing: bool):
        super().__init__()
        ### КОМПОНЕНТЫ

        # открыть / раскрыть
        top_toggle_playlist_btn = QPushButton()
        top_btn_layout = QHBoxLayout()

        # главная картинка
        main_image = MainImage()
        center_info_layout = QHBoxLayout()

        # текст
        about_track = AboutTrackLayout(current_track["title"], current_track["author"])

        # кнопки управления
        feature_btns = FeatureButtonsLayout(is_playing)

        # таймлайн
        t = Timeline()
        timeline = QWidget()

        ## РАЗМЕТКА
        top_btn_layout.addWidget(top_toggle_playlist_btn, stretch=1)
        center_info_layout.addWidget(main_image)
        timeline.setLayout(t)

        self.addLayout(top_btn_layout)
        self.addStretch()

        self.addLayout(center_info_layout)
        self.addLayout(about_track)
        self.addLayout(feature_btns)
        self.addWidget(timeline)

        self.addStretch()

        ## СТИЛИ
        top_btn_layout.setAlignment(Qt.AlignLeft)
        center_info_layout.setAlignment(Qt.AlignCenter)

        top_toggle_playlist_btn.setMaximumWidth(30)
        top_toggle_playlist_btn.setMaximumHeight(40)

        top_toggle_playlist_btn.setCursor(Qt.PointingHandCursor)
        top_toggle_playlist_btn.setStyleSheet('background-color: transparent;')

        timeline.setStyleSheet('background-color: transparent;')

        self.setSpacing(15)
        self.setAlignment(Qt.AlignCenter)


        ### ДИНАМИЧНЫЕ СТИЛИ
        pixmap = QPixmap('assets/arrowBack.svg')
        transformator = QTransform().rotate(180)
        rotated_pixmap = pixmap.transformed(transformator)

        if is_full_screen:
            top_toggle_playlist_btn.setIcon(QIcon(rotated_pixmap))
        else:
            top_toggle_playlist_btn.setIcon(QIcon('assets/arrowBack.svg'))

        ## ЛОГИКА
        top_toggle_playlist_btn.clicked.connect(self.notify_parent)
        feature_btns.emitPlay.connect(self.handle_play)
        feature_btns.emitPause.connect(self.handle_pause)


    def notify_parent(self):
        parent_widget = self.parentWidget()  # здесь будет w из feature_widget, который встраивается в root
        if parent_widget and hasattr(parent_widget, 'to_call_toggle'):  # явно указанный метод в root
            parent_widget.to_call_toggle()

    def handle_play(self):
        parent_widget = self.parentWidget()
        if parent_widget and hasattr(parent_widget, 'to_call_play'):  # явно указанный метод в root
            parent_widget.to_call_play()

    def handle_pause(self):
        parent_widget = self.parentWidget()
        if parent_widget and hasattr(parent_widget, 'to_call_pause'):  # явно указанный метод в root
            parent_widget.to_call_pause()



def feature_widget(is_full_screen: bool, current_track:dict, is_playing: bool):  # обертка лэйаута в виджет для стилизации
    w = QWidget()
    layout = FeatureLayout(is_full_screen, current_track, is_playing)
    w.setStyleSheet('background-color: rgba(0,0,0, 0.2)')
    w.setLayout(layout)
    return w
