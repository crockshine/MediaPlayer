from PySide6.QtCore import Signal
from PySide6.QtWidgets import QVBoxLayout
from components.track import TrackCard


class TrackList(QVBoxLayout):
    removeTrack = Signal(int)

    def __init__(self, card_data):
        super().__init__()
        self.tracks = card_data
        self.render_list()

    def render_list(self):
        # Создаём карточки
        for track in self.tracks:
            _track_card = TrackCard(track["id"], track["title"], track["author"])
            self.addWidget(_track_card)

            _track_card.emitDelete.connect(self.removeTrack.emit)

