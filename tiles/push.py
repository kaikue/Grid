import tile

class Push(tile.Tile):
    
    def is_pushable(self):
        return True
    
    def push(self, vel):
        return self.make_move(vel)
    
    def get_color(self):
        return (127, 94, 65)