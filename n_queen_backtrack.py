# Initialising the board
board=[[0,0,0,0],
       [0,0,0,0],
       [0,0,0,0],
       [0,0,0,0]]

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j],end="    ")
        print("\n")
    print("\n\n")
    


def validate(row,i):
    row=row
    col = i 
    # horizontal
    for c_ind,c in enumerate(board[row]):
        if c == 'Q' and c_ind != col :
            return False
    # vertical
    for r in range(len(board)):
        if board[r][col]=="Q" and r !=row:
            return False
    
    # left daigonal(\)
    left_daig=[]
    r=row
    c=col
    while r < len(board)-1 and c < len(board)-1:
        r+=1
        c+=1
        left_daig.append((r,c))
    
    r=row
    c=col
    while r > 0 and c >0:
        r-=1
        c-=1
        left_daig.append((r,c))
    # Right Daigonal (/)
    right_daig=[]
    r=row
    c=col
    while r >0 and c < len(board)-1:
        r-=1
        c+=1
        right_daig.append((r,c))
    r=row
    c=col
    while r < len(board)-1 and c > 0:
        r+=1
        c-=1
        right_daig.append((r,c))
    
    for r,c in left_daig:
        if board[r][c] == "Q" and (r,c)!=(row,col):
            return False

    for r,c in right_daig:
        if board[r][c] == "Q" and (r,c)!=(row,col):
            return False
    return True

def find(board):
    for i,row in enumerate(board):
        if "Q" not in row:
            return i
    return None     

def Solve(board):
    if find(board) == None:
        return True    
    else :
        row = find(board)
    for i in range(len(board)):
        if validate(row,i):
            board[row][i]="Q"
            
            if Solve(board):
                return True
            board[row][i] = 0
    return False
        
print_board(board)
Solve(board)
print_board(board)