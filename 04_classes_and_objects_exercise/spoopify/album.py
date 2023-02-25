class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.published = False
        self.songs = list(songs)

    def add_song(self, some_song):
        if some_song.single:
            return f"Cannot add {some_song.name}. It's a single"

        if self.published:
            return "Cannot add songs. Album is published."

        if some_song in self.songs:
            return f"Song is already in the album."

        self.songs.append(some_song)
        return f"Song {some_song.name} has been added to the album {self.name}."

    def remove_song(self, song):
        if self.published:
            return "Cannot remove songs. Album is published."
        try:
            current_song = next(filter(lambda s: s.name == song, self.songs))
        except StopIteration:
            return f"Song is not in the album."

        self.songs.remove(current_song)
        return f"Removed song {song} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}\n"
        for song in self.songs:
            result += f'== {song.get_info()}\n'
        return result

