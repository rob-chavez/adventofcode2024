import numpy as np
FILENAME = "/Users/blackbox/Desktop/advent6"

def load_data(FILENAME):
    f = open(FILENAME)
    strings = []
    for line in f:
        strings.append(line.rstrip())
    f.close()
    return strings

def get_game_map(strings):
    game_pieces = {".":0, "#":2, "^":3, "<":4, ">":5, "v":6, "X":7}
    guard_pieces = ["^", "<", ">", "v"]
    guard_piece = 3
    guard_position = [0,0]
    rows = len(strings)
    columns = len(strings[0])
    game_map = np.zeros((rows, columns), dtype=int)
    for r, string in enumerate(strings):
        for c, char in enumerate(string):

            #COMPLETE THE MAP
            if char == ".":
                pass
            else:
                    game_map[r,c] = game_pieces[char]

            #ID GUARD PIECE AND LOCATION
            if char in guard_pieces:
                guard_piece = char
                guard_position = [r,c]
    return game_map, game_pieces, guard_piece, guard_position


def walk_path(game_map, game_pieces, guard_piece, guard_position):
    end_game = 0
    row = guard_position[0]
    column = guard_position[1]
    game_map[row, column] = game_pieces['X']
    
    ###### "^" ######
    if guard_piece == "^":
        next_move = row - 1
        piece_ahead = game_map[next_move, column]
        while (piece_ahead != game_pieces["#"]) or (next_move < 0):
            game_map[next_move, column] = game_pieces['X']
            row = next_move
            guard_position = [row, column]
            next_move = row - 1
            if (next_move < 0):
                end_game = 1
                break
            else:
                piece_ahead = game_map[next_move, column]
        guard_piece = ">"
        guard_position = [row, column]
        wall = [next_move, column]
        return game_map, guard_piece, guard_position, end_game, wall
    
    ###### ">" ######
    if guard_piece == ">":
        next_move = column + 1
        piece_ahead = game_map[row, next_move]
        while (piece_ahead != game_pieces["#"]) or (next_move > game_map.shape[0] - 1):
            game_map[row, next_move] = game_pieces['X']
            column = next_move
            guard_position = [row, column]
            next_move = column + 1
            if (next_move > game_map.shape[0] - 1):
                end_game = 1
                break
            else:
                piece_ahead = game_map[row, next_move]
        guard_piece = "v"
        guard_position = [row, column]
        wall = [row, next_move]
        return game_map, guard_piece, guard_position, end_game, wall
    
    ###### "v" ######
    if guard_piece == "v":
        next_move = row + 1
        piece_ahead = game_map[next_move, column]
        while (piece_ahead != game_pieces["#"]) or (next_move > game_map.shape[0] - 1):
            game_map[next_move, column] = game_pieces['X']
            row = next_move
            guard_position = [row, column]
            next_move = row + 1
            if (next_move > game_map.shape[0] - 1):
                end_game = 1
                break
            else:
                piece_ahead = game_map[next_move, column]
        guard_piece = "<"
        guard_position = [row, column]
        wall = [next_move, column]

        return game_map, guard_piece, guard_position, end_game, wall

    ###### "<" ######
    if guard_piece == "<":
        next_move = column - 1
        piece_ahead = game_map[row, next_move]
        while (piece_ahead != game_pieces["#"]) or (next_move < 0):
            game_map[row, next_move] = game_pieces['X']
            column = next_move
            guard_position = [row, column]
            next_move = column - 1
            if (next_move < 0):
                end_game = 1
                break
            else:
                piece_ahead = game_map[row, next_move]
        guard_piece = "^"
        guard_position = [row, column]
        wall = [row, next_move]
        
        return game_map, guard_piece, guard_position, end_game, wall

data = load_data(FILENAME)
game_map, game_pieces, guard_piece, guard_position = get_game_map(data)
end_game = 0
while not end_game:
    game_map, guard_piece, guard_position,end_game, wall = walk_path(game_map, game_pieces, guard_piece, guard_position)    

count = 0
for row in range(game_map.shape[0]):
    for column in range(game_map.shape[1]):
        if game_map[row, column] == 7:
            count+=1

print("Part 1:",count)

            
data = load_data(FILENAME)
game_map, game_pieces, guard_piece, guard_position = get_game_map(data)
end_game = 0
game_map_copy = game_map.copy()
guard_position_copy = guard_position

end_game_value = 0
for row in range(game_map.shape[0]):
    for column in range(game_map.shape[1]):

        
        #The new obstruction can't be placed at the guard's starting position
        if ((guard_position_copy[0] == row) and (guard_position_copy[1] == column)):
            continue

        #set up the game
        if (game_map_copy[row,column] == 0):
            game_map_copy[row,column] = game_pieces["#"]
            
        n = 0
        
        while not end_game:
            
            game_map_copy, guard_piece, guard_position_copy,end_game, wall = walk_path(game_map_copy, 
                                                                                       game_pieces, 
                                                                                       guard_piece, 
                                                                                       guard_position_copy)  
            if end_game == 1:
                end_game_value +=1
            
            if n == game_map_copy.shape[0]*2:
                break
            else:
                n+=1
                
        #reset game      
        game_map_copy = game_map.copy()
        guard_position_copy = guard_position
        guard_piece = "^"
        end_game = 0 
        
print("Part 2:", game_map_copy.shape[0]*game_map_copy.shape[1] - end_game_value - 1)
