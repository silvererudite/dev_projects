state = [[0,0,0],[0,0,0], [0,0,0]]
move = 0
def make_move(row, col, val):
  if is_empty():
    state[row, col] = val
    move += 1

def is_empty():
  return 0 in state

def winning_state():
  if move == 3:
    pass
