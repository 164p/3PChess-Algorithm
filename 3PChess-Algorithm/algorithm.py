import random
import time

def algorithm_provider(possible_move, current_board, type_algorithm):
    if type_algorithm == 1:
        return play_random(possible_move)
    if type_algorithm == 2:
        return testalgo(possible_move, current_board)
    # handle any algorithm
    else:
        return play_random(possible_move)
    

def play_random(possible_move):
    while True:
        try:
            print("This is possible move: ", possible_move)

            random_piece = random.choice(list(possible_move.keys()))
            random_move = random.choice(possible_move[random_piece])

            print(f"This is random piece: {random_piece} and random move: {random_move}")

            return random_piece, random_move
        except:
            pass

        time.sleep(1)

def testalgo(possible_move, current_board):
    targetvalue_chess = {'Pawn':1, 'Knight':3, 'Bishop':3, 'Rocok':5, 'Queen':9, 'King':99}
    value_chess = {'Pawn':1, 'Knight':3, 'Bishop':3, 'Rocok':5, 'Queen':9, 'King':99}

    top = 0
    try:    
        print("This is possible move: ", possible_move)

        for p, m in possible_move.items():
            for move in m:
                if move in [entry['Field'] for entry in current_board]:
                    random_piece = p
                    random_move = move
                    return random_piece, random_move
        
        

        return play_random(possible_move)
    except:
        pass
    time.sleep(1)
    
# def testalgo(possible_move, current_board):
#     targetvalue_chess = {'Pawn':1, 'Knight':3, 'Bishop':3, 'Rook':5, 'Queen':9, 'King':99}
#     value_chess = {'Pawn':1, 'Knight':3, 'Bishop':3, 'Rook':5, 'Queen':9, 'King':99}
#     piece_t = None
#     move_t = None
#     top = 0

#     for p, m in possible_move.items():
#         for move in m:
#             for entry in current_board:
#                 if move in entry['Field']:
#                     if  value_chess[entry['Piece']] > top:
#                         top = value_chess[entry['Piece']]
#                         piece_t = p
#                         move_t = move
                        
#     if piece_t is None or move_t is None:
#         return play_random(possible_move)
    
#     return piece_t, move_t    
    

# def capture_opponent_piece(possible_move, trichess_board):
#     while True:
#         try:
#             # Filter moves that result in captures
#             capture_moves = {
#                 piece_pos: moves
#                 for piece_pos, moves in possible_move.items()
#                 if any(
#                     get_piece_at_field(move, trichess_board) is not None and
#                     trichess_board[get_index_by_field(piece_pos, trichess_board)] is not None and
#                     get_piece_at_field(move, trichess_board).get("Player") != trichess_board[get_index_by_field(piece_pos, trichess_board)].get("Player")
#                     for move in moves
#                 )
#             }

#             # Prioritize capturing higher-value pieces
#             valued_capture_moves = sorted(
#                 capture_moves.items(),
#                 key=lambda item: [
#                     "King", "Queen", "Rook", "Bishop", "Knight", "Pawn"  # Piece value order
#                 ].index(
#                     get_piece_at_field(random.choice(item[1]), trichess_board).get("Piece")
#                     if get_piece_at_field(random.choice(item[1]), trichess_board) is not None
#                     else "Pawn"  # Use lowest value if no piece found
#                 ),
#                 reverse=True,
#             )

#             if valued_capture_moves:
#                 random_capture_move = random.choice(valued_capture_moves)
#                 piece_pos, move = random_capture_move
#                 print(f"Capturing opponent piece: {piece_pos} -> {move}")
#                 return piece_pos, move

#             # If no captures, fall back to random move
#             return play_random(possible_move)

#             # ... rest of your code remains the same ...

#         except Exception as e:
#             print(f"Error selecting move: {e}")
#             time.sleep(1)  # Retry after a brief delay

# def capture_opponent_piece(possible_move, trichess_board):
#     while True:
#         try:
#             # Filter moves that result in captures
#             capture_moves = {
#                 piece_pos: moves
#                 for piece_pos, moves in possible_move.items()
#                 if any(
#                     get_piece_at_field(move, trichess_board) is not None and
#                     trichess_board[get_index_by_field(piece_pos, trichess_board)] is not None and
#                     get_piece_at_field(move, trichess_board).get("Player") != trichess_board[get_index_by_field(piece_pos, trichess_board)].get("Player")
#                     for move in moves
#                 )
#             }

#             # Debug: print capture_moves
#             print("Capture Moves:", capture_moves)

#             # Prioritize capturing higher-value pieces
#             valued_capture_moves = sorted(
#                 capture_moves.items(),
#                 key=lambda item: [
#                     targetvalue_chess.get(get_piece_at_field(random.choice(item[1]), trichess_board).get("Piece"), 0)
#                 ],
#                 reverse=True,
#             )

#             # Debug: print valued_capture_moves
#             print("Valued Capture Moves:", valued_capture_moves)

#             if valued_capture_moves:
#                 random_capture_move = random.choice(valued_capture_moves)
#                 piece_pos, move = random_capture_move
#                 print(f"Capturing opponent piece: {piece_pos} -> {move}")
#                 return piece_pos, move

#             # Debug: print fallback message
#             print("No capture moves, falling back to random move")

#             # If no captures, fall back to the modified play_random
#             return play_random_with_target_values(possible_move, trichess_board)

#         except Exception as e:
#             print(f"Error selecting move: {e}")
#             time.sleep(1)  # Retry after a brief delay

# def play_random_with_target_values(possible_move, trichess_board):
#     try:
#         print("This is possible move: ", possible_move)

#         if not trichess_board:
#             print("The trichess_board is empty.")
#             return None, None

#         valid_fields = [entry['Field'] for entry in trichess_board if 'Field' in entry]

#         if not valid_fields:
#             print("No valid fields in trichess_board.")
#             return None, None

#         for p, m in possible_move.items():
#             for move in m:
#                 if move in valid_fields:
#                     random_piece = p
#                     random_move = move
#                     return random_piece, random_move

#         random_piece = random.choice(list(possible_move.keys()))
#         random_move = random.choice(possible_move[random_piece])

#         print(f"This is random piece: {random_piece} and random move: {random_move}")

#         return random_piece, random_move
#     except Exception as e:
#         print(f"Error in play_random_with_target_values: {e}")
#         time.sleep(1)
#         return None, None

# def get_piece_at_field(field, trichess_board):
#     """Retrieves the piece information at a given field on the board."""
#     try:
#         return next(piece for piece in trichess_board if piece["Field"] == field)
#     except StopIteration:
#         return None  # No piece found at the field

# # The rest of your code remains unchanged

# def get_index_by_field(field, trichess_board):
#     """Retrieves the index of the piece with the given field on the board."""
#     for i, piece in enumerate(trichess_board):
#         if piece["Field"] == field:
#             return i
#     return None  # No piece found at the field

        