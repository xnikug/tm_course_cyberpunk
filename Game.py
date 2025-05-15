import Player
from Direction import Direction
from LinkedRoom import LinkedRoomNode


class Game:

    def __init__(self, player: Player, entry_room: LinkedRoomNode):
        self.current_room = entry_room
        self.player = player

    def move(self, direction: Direction):
        next_room = getattr(self.current_room, direction.value, None)
        if next_room:
            self.current_room = next_room

    def start(self):
        pass

