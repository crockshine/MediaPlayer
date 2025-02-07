from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QTransform, QPixmap
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout

from components.about_track import AboutTrackLayout
from components.feature_buttons import FeatureButtonsLayout
from components.main_image import MainImage


class FeatureLayout(QVBoxLayout):
    def __init__(self, is_full_screen: bool):
        super().__init__()
        ### КОМПОНЕНТЫ
        top_toggle_playlist_btn = QPushButton()
        top_btn_layout = QHBoxLayout()

        main_image = MainImage()
        center_info_layout = QHBoxLayout()

        about_track = AboutTrackLayout('Born To Die', 'Lana Del Ray')
        feature_btns = FeatureButtonsLayout()


        ## РАЗМЕТКА
        top_btn_layout.addWidget(top_toggle_playlist_btn, stretch=1)
        center_info_layout.addWidget(main_image)

        self.addLayout(top_btn_layout)
        self.addStretch()

        self.addLayout(center_info_layout)
        self.addLayout(about_track)
        self.addLayout(feature_btns)

        self.addStretch()

        ## СТИЛИ
        top_btn_layout.setAlignment(Qt.AlignLeft)
        center_info_layout.setAlignment(Qt.AlignCenter)

        top_toggle_playlist_btn.setMaximumWidth(30)
        top_toggle_playlist_btn.setMaximumHeight(40)

        top_toggle_playlist_btn.setCursor(Qt.PointingHandCursor)
        top_toggle_playlist_btn.setStyleSheet('background-color: transparent;')

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

    def notify_parent(self):
        parent_widget = self.parentWidget()  # здесь будет w из feature_widget, который встраивается в root
        if parent_widget and hasattr(parent_widget, 'to_call_toggle'):  # явно указанный метод в root
            parent_widget.to_call_toggle()


def feature_widget(is_full_screen: bool):  # обертка лэйаута в виджет для стилизации
    w = QWidget()
    layout = FeatureLayout(is_full_screen)
    w.setStyleSheet('background-color: rgba(0,0,0, 0.2)')
    w.setLayout(layout)
    return w
