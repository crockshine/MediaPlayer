from PySide6.QtCore import Signal
from PySide6.QtWidgets import QVBoxLayout
from components.track import TrackCard


class TrackList(QVBoxLayout):
    removeTrack = Signal(int)
    chooseCurrentTrack = Signal(dict)

    def __init__(self, card_data, current_track):
        super().__init__()
        self.tracks = card_data
        self.current_track = current_track

        self.render_list()

    def render_list(self):
        # Создаём карточки
        for track in self.tracks:
            _is_current = (self.current_track["id"] == track["id"])
            _track_card = TrackCard(track, _is_current)
            self.addWidget(_track_card)

            _track_card.emitDelete.connect(self.removeTrack.emit)
            _track_card.emitChooseCurrentTrack.connect(self.chooseCurrentTrack.emit)

