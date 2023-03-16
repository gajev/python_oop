from math import ceil


class PhotoAlbum:
    PHOTOS_ON_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(ceil(photos_count / cls.PHOTOS_ON_PAGE))

    def add_photo(self, label):
        for current_page in range(len(self.photos)):
            if len(self.photos[current_page]) < 4:
                self.photos[current_page].append(label)
                return f"{label} photo added successfully on page" \
                       f"{current_page + 1} slot {len(self.photos[current_page])}"
        return "No more free slots"

    def display(self):
        result = ["-" * 11]
        for cur_page in self.photos:
            result.append(("[] " * len(cur_page)).rstrip())
            result.append("-" * 11)
        return "\n".join(result)


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())

