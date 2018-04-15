import result

class Tile(object):
    
    def __init__(self, pos, grid):
        self.pos = pos
        self.grid = grid
    
    def update(self):
        pass
    
    def move(self, vel):
        return result.CLEAR
    
    def make_move(self, vel):
        old_pos = [self.pos[0], self.pos[1]]
        self.pos[0] += vel[0]
        self.pos[1] += vel[1]
        r = self.update_grid(vel)
        if r == result.HIT:
            self.pos = old_pos
        return r
    
    def intersect(self, other, vel):
        if other.is_pushable():
            return other.push(vel)
        elif other.is_solid():
            return result.HIT
        return result.CLEAR
    
    def is_pushable(self):
        return False
    
    def is_finish(self):
        return False
    
    def get_color(self):
        return (0, 0, 0)
    
    def push(self):
        return False
    
    def is_solid(self):
        return True
    
    def update_grid(self, vel):
        if not (0 <= self.pos[0] < self.grid.width and 0 <= self.pos[1] < self.grid.height):
            return result.HIT
        at = self.tiles_at(self.pos)
        for other in at:
            r = self.intersect(other, vel)
            if r == result.WON:
                return r
            elif r == result.HIT:
                return r
        return result.CLEAR
    
    def tiles_at(self, pos):
        at = []
        for tile in self.grid.tiles:
            if tile.pos == pos and tile != self:
                at.append(tile)
        return at