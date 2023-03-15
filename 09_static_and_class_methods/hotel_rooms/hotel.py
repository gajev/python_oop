from hotel_rooms.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        result = None
        for current_room in self.rooms:
            if current_room.number == room_number:
                result = current_room.take_room(people)
        if result:
            return result
        self.guests += people

    def free_room(self, room_number):
        for current_room in self.rooms:
            if current_room.number == room_number:
                guests = current_room.guests
                result = current_room.free_room()
                if result:
                    return result
                self.guests -= guests

    def status(self):
        result = f"Hotel {self.name} has {self.guests} total guests\n"
        result += f"Free rooms: {', '. join(str(r.number) for r in self.rooms if not r.is_taken)}\n"
        result += f"Taken rooms: {', '. join(str(r.number) for r in self.rooms if r.is_taken)}"
        return result






