from PySide6.QtWidgets import QVBoxLayout, QWidget

from widgets.add_track_block import AddTrackBlock
from widgets.track_list import TrackList
from PySide6.QtCore import Qt, Signal


class PlayList(QWidget):
    emitAddNewTrack = Signal(dict)
    emitDeleteTrack = Signal(int)
    emitChooseCurrentTrack = Signal(dict)

    def __init__(self, card_data, current_track):
        super().__init__()
        play_list_layout = QVBoxLayout()
        ## ДАННЫЕ
        self._track_list_layout = TrackList(card_data, current_track)
        self._add_track_block = AddTrackBlock()

        ## РАЗМЕТКА
        play_list_layout.addLayout(self._track_list_layout)
        play_list_layout.addStretch()
        play_list_layout.addLayout(self._add_track_block)
        self.setLayout(play_list_layout)

        ## СТИЛИ
        play_list_layout.setAlignment(Qt.AlignTop)

        ## ЛОГИКА
        self._add_track_block.emitAddNewTrack.connect(self.emitAddNewTrack.emit)
        self._track_list_layout.removeTrack.connect(self.emitDeleteTrack.emit)
        self._track_list_layout.chooseCurrentTrack.connect(self.emitChooseCurrentTrack.emit)





