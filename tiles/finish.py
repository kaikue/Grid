import tile

class Finish(tile.Tile):
    
    def is_finish(self):
        return True
    
    def get_color(self):
        return (255, 221, 56)