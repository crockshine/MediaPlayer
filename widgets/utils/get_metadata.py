from mutagen import File
from mutagen.flac import FLAC
from mutagen.id3 import ID3, APIC
from mutagen.mp3 import MP3
from mutagen.oggvorbis import OggVorbis
from mutagen.wave import WAVE
import os

def get_audio_metadata(filepath, fallback_artist="Unknown Artist", fallback_title="Unknown Title"):
    """
    Извлекает метаданные (исполнитель, название, обложку) из аудиофайла.

    :param filepath: Путь к аудиофайлу
    :param fallback_artist: Fallback-значение для исполнителя
    :param fallback_title: Fallback-значение для названия
    :param fallback_cover: Fallback-значение для обложки (путь к файлу или None)
    :return: Словарь с метаданными {'artist', 'title'}
    """
    try:
        audio = File(filepath, easy=True)
    except Exception as e:
        print(f"Ошибка при чтении файла {filepath}: {e}")
        return [
            fallback_artist,
            fallback_title,
        ]

    # Получаем исполнителя и название
    artist = audio.get('artist', [fallback_artist])[0] if audio else fallback_artist
    title = audio.get('title', [fallback_title])[0] if audio else fallback_title
    # Получаем обложку (если есть)

    return [
        artist,
        title,
    ]


print(get_audio_metadata('C:/Users/Михаил/OneDrive/Рабочий стол/Lana Del Rey - Summer time sadness.mp3'))

