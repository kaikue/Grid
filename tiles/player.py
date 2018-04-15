import tile
import result
import sound

class Player(tile.Tile):
    
    def move(self, vel):
        r = self.make_move(vel)
        sound.play_move(r)
        return r
    
    def get_color(self):
        return (255, 255, 255)
    
    def intersect(self, other, vel):
        if other.is_finish():
            return result.WON
        else:
            return super().intersect(other, vel)