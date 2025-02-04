from PySide6.QtWidgets import QVBoxLayout

from widgets.add_track_block import AddTrackBlock
from widgets.track_list import TrackList
from PySide6.QtCore import Qt


class PlayList(QVBoxLayout):
    def __init__(self):
        super().__init__()

        ## ДАННЫЕ
        self.card_data = []
        self._track_list_layout = TrackList(self.card_data)
        self._add_track_block = AddTrackBlock()

        ## РАЗМЕТКА
        self.addLayout(self._track_list_layout)
        self.addStretch()
        self.addLayout(self._add_track_block)

        ## СТИЛИ
        self.setAlignment(Qt.AlignTop)

        ## ЛОГИКА
        self._add_track_block.emitAddNewTrack.connect(self.handle_add_new_track)
        self._track_list_layout.removeTrack.connect(self.handle_remove_track)

    def handle_add_new_track(self, id_of_track, title, author):
        self.card_data.append({"id": id_of_track, "title": title, "author": author})
        self._track_list_layout.update_list(self.card_data)

    def handle_remove_track(self, id_of_track):
        new_data = []
        for track in self.card_data:
            if track["id"] != id_of_track:
                new_data.append(track)
        self.card_data = new_data
        self._track_list_layout.update_list(self.card_data)

