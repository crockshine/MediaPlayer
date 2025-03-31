from PySide6.QtCore import QSize, Qt, Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QHBoxLayout, QPushButton, QWidget, QSlider


class Timeline(QHBoxLayout):
    def __init__(self):
        super().__init__()

        self.timeline_slider = QSlider(Qt.Horizontal)
        ### РАЗМЕТКА

        self.addWidget(self.timeline_slider)

        ### СТИЛИ
        self.timeline_slider.setStyleSheet("""
           QSlider::groove:horizontal {
               background: transparent;
               height: 8px;
               border-radius: 4px;
               opacity: 0;
           }
            
           QSlider::sub-page:horizontal {
               background: white; /* Цвет заполненной части */
               height: 8px;
               border-radius: 4px;
           }

           QSlider::add-page:horizontal {
               background: #ccc; /* Цвет незаполненной части */
               height: 8px;
               border-radius: 4px;
           }
           
           QSlider::handle:horizontal {
               background: white;
               width: 20px;
               height: 20px;
               margin: -6px 0; /* Смещение ручки */
               border-radius: 10px;
           }
        """)
        ### ЛОГИКА


