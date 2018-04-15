import tiles.player
import tiles.finish
import tiles.push

TILES = {
     "P": tiles.player.Player,
     "F": tiles.finish.Finish,
     "B": tiles.push.Push,
    }

class Grid(object):
    
    def __init__(self, level):
        self.text = ""
        filename = "levels/" + str(level) + ".txt"
        with open(filename) as f:
            lines = [line.rstrip('\n') for line in f]
        
        self.width = len(lines[0])
        self.height = len(lines)
        
        self.tiles = []
        y = 0
        for line in lines:
            if line[0] == '#':
                self.height -= 1
                self.text = line[1:]
                break
            x = 0
            for char in line:
                if char != ' ':
                    tile = TILES[char]
                    self.tiles.append(tile([x, y], self))
                x += 1
            y += 1