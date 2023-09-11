import time
from random import Random

from board import Action, Direction, Rotation,Shape

class Player:
    def choose_action(self, board):
        raise NotImplementedError

class MyPlayer(Player):
    def __init__(self, seed=None):
        self.random = Random(seed)

    def print_board(self, board):
        print("--------")
        for y in range(24):
            s = ""
            for x in range(10):
                if (x,y) in board.cells:
                    s += "#"
                else:
                    s += "."
            print(s, y)

    def move_to_target(self,board,pointer,rotations):
        for i in range (rotations):
            if(board.rotate(Rotation.Anticlockwise)):
                return
        if pointer < 5:
            while board.falling.left != pointer:
                if(board.move(Direction.Left)):
                    return
        else:
            while board.falling.right != pointer:
                if (board.move(Direction.Right)):
                    return
        board.move(Direction.Drop)
        #self.print_board(board)

    def scoreboard(self,board,test):
        #IF THERE IS A BUMPINESS OF 2 EITHER SIDE LEAVE BLANK FOR LONG ONE (I)
        #LEAVE LEFT COLUM FOR I SO YOU ELIMINATE MULTIPLE ROWS AT ONCE
        
        aggregate_height = 0
        for x in range(10):
            for y in range(24):
                if (x,y) in board.cells:
                    aggregate_height += (24 -y)
                    break   

        holes = 0
        for x in range (10):
            top = 100
            for y in range(24):
                if (x,y) in board.cells and top == 100:
                    top = y
                    #print("top: ",top, " at ", x,y)
                elif  (x,y) not in board.cells and top != 100:
                    holes += 1
                    
        completed_lines = 0
        cell_change = len(board.cells) - len(test.cells)
        if cell_change == 4:
            completed_lines = 0
        elif cell_change == -6:
            completed_lines = 1
        elif cell_change == -16:
            #completed_lines = 2
            completed_lines = 4
        elif cell_change == -26:
            #completed_lines = 3
            completed_lines = 16
        elif cell_change == -36:
            #completed_lines = 4
            completed_lines = 64

        bumpiness = 0
        for x in range(9):
            topy = 24
            topnexty = 24
            for y in range(24):
                if (x,y) in board.cells and topy == 24:
                    topy = y
                if (x+1,y) in board.cells and topnexty == 24:
                    topnexty = y
            #print("topy",topy,"topnexty",topnexty)
            bumpiness += abs(topy - topnexty)

        a = 1.41
        b = 0.50
        c = 0.16
        d = 0

        heightmax = 50
        for y in range(24):
            for x in range(10):
                if (x,y) in board.cells and y < heightmax:
                    heightmax = y
        if (24 - heightmax) > 13:
            a = 1.41 #same as 1.4
            b = 0.50
            c = 1.16
        #smaller score better
        # weight heuristics belowwwwwww
        score = a * holes + b * aggregate_height + c * bumpiness - d * completed_lines
        #score = 1 * holes + 0.5 * aggregate_height/10 + 0.15 * bumpiness #- completed_lines
        #print("aggregate height : ",aggregate_height,"holes: ",holes,"cell change: ",cell_change,"completed lines: ",completed_lines,"bumpiness: ",bumpiness,"SCORE: ",score)
        return score

    def make_best_move(self,board,pointer,rotations):
        # heightmax = 50
        # for y in range(24):
        #     for x in range(10):
        #         if (x,y) in board.cells and y < heightmax:
        #             heightmax = y
        #     if board.falling.shape == Shape.I and heightmax < 12 and heightmax > 6:
        #         moves = [Direction.Right,Direction.Right,Direction.Right,Direction.Right,Direction.Right]
        #         return moves
        # print(pointer,rotations)
        moves = []
        for i in range (rotations):
            moves.append(Rotation.Anticlockwise)
            if(board.rotate(Rotation.Anticlockwise)):
                return moves
        if pointer < 5:
            while board.falling.left != pointer:
                moves.append(Direction.Left)
                if(board.move(Direction.Left)):
                    #print("in left",moves)
                    return moves
        else:
            #print("pointer:",pointer)
            while board.falling.right != pointer and board.falling.right != 9:
                moves.append(Direction.Right)
                if (board.move(Direction.Right)):
                    #print("in right",moves)
                    return moves
        board.move(Direction.Drop)
        moves.append(Direction.Drop)
        #print("out",moves)
        return moves

    def choose_action(self, board):

        #self.print_board(board)
        #time.sleep(1)
        # for y in range ( board.height ):
        #     for x in range ( board.width ):
        #         if (x , y ) in board.cells :
        #             print(x,y)
        #print(board.falling.shape)
        #print(board.falling.cells)
        left_pointer = 4
        right_pointer = 5
        best_score = 1000000
        best_pointer = 0
        best_no_rotations = 0
        #print("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")
        #print(board.falling.shape)       
        while ( left_pointer >= 0):
            for numrotations in range(4):
                test = board.clone()
                self.move_to_target(test,left_pointer,numrotations)
                score = self.scoreboard(test,board)
                #print("leftpoint: ",left_pointer,"numrot: ",numrotations,"score: ",score)
                #print("\nnext one:")
                # for y in range ( test.height ):
                #     for x in range ( test.width ):
                #         if (x , y ) in test.cells :
                #             print(x,y)
                #self.print_board(test)
                #print("L", test.falling.cells)
                if score < best_score:
                    best_score = score
                    best_pointer = left_pointer
                    best_no_rotations = numrotations
                #print(test.falling.cells)              
            left_pointer -= 1 
        #print("RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")       
        while ( right_pointer < 10):
            for num_rotations in range(4):
                test = board.clone()
                self.move_to_target(test,right_pointer,num_rotations)        
                score = self.scoreboard(test,board)
                #print("rightpoint: ",right_pointer,"numrot: ",num_rotations,"score: ",score)
                #print("\nnext one:")
                # for y in range ( test.height ):
                #     for x in range ( test.width ):
                #         if (x , y ) in test.cells :
                #             print(x,y)
                #self.print_board(test)
                #print("R", test.falling.cells)
                if score < best_score:
                    best_score = score
                    best_pointer = right_pointer
                    best_no_rotations = num_rotations
                #print(test.falling.cells)                   
            right_pointer += 1
        #print("end of test")
        #print("best score:",best_score,"best pointer: ",best_pointer,"best no rotations: ",best_no_rotations)
        test = board.clone()
        return self.make_best_move(test,best_pointer,best_no_rotations)

SelectedPlayer = MyPlayer

#MOVE TO POSITION NOT WORKING NEED TO USE OLD METHODDDDDDDDDDDD  

        #for all positions
            #for all rotations
                #clone board  
                #move to target()
                #score board()
        #!!!_return make best move()_!!!

# note how many rotations; not work out from coordinates to know orientation
#do the always drop at the same rotation from the centre????
#order of rotations/move?
#why rotate first???

'''---------------------------------------------------------------------------------------------------------------------------------------------'''
'''---------------------------------------------------------------------------------------------------------------------------------------------'''
'''---------------------------------------------------------------------------------------------------------------------------------------------'''

class RandomPlayer(Player):
    def __init__(self, seed=None):
        self.random = Random(seed)

    def print_board(self, board):
        print("--------")
        for y in range(24):
            s = ""
            for x in range(10):
                if (x,y) in board.cells:
                    s += "#"
                else:
                    s += "."
            print(s, y)
      
    def choose_action(self, board):

        self.print_board(board)
        #time.sleep(0.5)
        if self.random.random() > 0.97:
            # 3% chance we'll discard or drop a bomb
            return self.random.choice([
                Action.Discard,
                Action.Bomb,
            ])
        else:
            # 97% chance we'll make a normal move
            return self.random.choice([
                Direction.Left,
                Direction.Right,
                Direction.Down,
                Rotation.Anticlockwise,
                Rotation.Clockwise,
            ])

#SelectedPlayer = RandomPlayer

def move_to_target_1(self,board,pointer,rotations):
    cells = list(board.falling.cells)
    reachedtarget = 0
    for i in range (rotations):
        if board.rotate(Rotation.Anticlockwise):
            break

    while reachedtarget == 0:

        # if board.falling.left == pointer:
        #     return

        for i in range(len(cells)):
            if cells[i][1] == pointer:
                reachedtarget = 1

        if reachedtarget == 1:
            return

        if pointer < 5:
            if board.move(Direction.Left):
                break
            # print("left")
            # print(board.falling.cells)
        else:
            if board.move(Direction.Right):
                break
            # print("right")
            # print(board.falling.cells)
    #print(board.falling.cells)

def move_to_target_2(self,board,pointer,rotations):
    # cells = list(board.falling.cells)
    # reachedtarget = 0
    for i in range (rotations):
        if board.rotate(Rotation.Anticlockwise):
            break

    #while reachedtarget == 0:

        # for i in range(len(cells)):
        #     if cells[i][1] == pointer:
        #         reachedtarget = 1

        # if reachedtarget == 1:
        #     return

        if pointer < 5:
            while board.falling.left != pointer:
                if board.move(Direction.Left):
                    break
                    # print("left")
                    # print(board.falling.cells)
        else:
            while board.falling.right != pointer:
                if board.move(Direction.Right):
                    break
                    # print("right")
                    # print(board.falling.cells)
    #print(board.falling.cells)

def scoreboard_1(self,board):
    heightmax = 50
    for y in range(24):
        for x in range(10):
            if (x,y) in board.cells and y < heightmax:
                heightmax = y

    heightmin = 0
    for b in range(24):
        for a in range(10):
            if (a,b) in board.cells and b > heightmin:
                heightmin = b
    #print("heightmax: ",heightmax,"heightmin: ",heightmin)

    totalheight = 0
    for x in range(10):
        for y in range(24):
            if (x,y) in board.cells:
                totalheight += (24 -y)
                break     

    gaps = 0
    for x in range (10):
        top = 100
        for y in range(24):
            if (x,y) in board.cells and top == 100:
                top = y
                #print("top: ",top, " at ", x,y)
            elif  (x,y) not in board.cells and top != 100:
                gaps += 1

                #print(x,y)
        #print("gaps for this colum: ", gaps)
    #print("HEIGHT: ",24 - height,"GAPS: ",gaps)
    #print("totalheight: ",totalheight,"gaps: ",gaps)
    if (heightmin - heightmax + 1) > 6 or (24 - heightmax) > 15:
        score = gaps + 24 - heightmax
    else:
        score = 3 * gaps + (24 - heightmax) #(heightmin - heightmax + 1)+ totalheight +#(not height do bumpiness)
    return score

def move_to_target_11k(self,board,pointer,rotations):
    for i in range (rotations):
        if(board.rotate(Rotation.Anticlockwise)):
            return
    if pointer < 5:
        while board.falling.left != pointer:
            if(board.move(Direction.Left)):
                return
    else:
        while board.falling.right != pointer:
            if (board.move(Direction.Right)):
                return
    board.move(Direction.Drop)
    #self.print_board(board)

def make_best_move_11k(self,board,pointer,rotations):
    # print(pointer,rotations)
    moves = []
    for i in range (rotations):
        moves.append(Rotation.Anticlockwise)
        if(board.rotate(Rotation.Anticlockwise)):
            return moves
    if pointer < 5:
        while board.falling.left != pointer:
            moves.append(Direction.Left)
            if(board.move(Direction.Left)):
                #print("in left",moves)
                return moves
    else:
        #print("pointer:",pointer)
        while board.falling.right != pointer and board.falling.right != 9:
            moves.append(Direction.Right)
            if (board.move(Direction.Right)):
                #print("in right",moves)
                return moves
    board.move(Direction.Drop)
    moves.append(Direction.Drop)
    #print("out",moves)
    return moves

def scoreboard_11k(self,board,test):
#IF THERE IS A BUMPINESS OF 2 EITHER SIDE LEAVE BLANK FOR LONG ONE (I)
#LEAVE LEFT COLUM FOR I SO YOU ELIMINATE MULTIPLE ROWS AT ONCE

    aggregate_height = 0
    for x in range(10):
        for y in range(24):
            if (x,y) in board.cells:
                aggregate_height += (24 -y)
                break   

    holes = 0
    for x in range (10):
        top = 100
        for y in range(24):
            if (x,y) in board.cells and top == 100:
                top = y
                #print("top: ",top, " at ", x,y)
            elif  (x,y) not in board.cells and top != 100:
                holes += 1
    completed_lines = 0
    cell_change = len(board.cells) - len(test.cells)
    if cell_change == 4:
        completed_lines = 0
    elif cell_change == -6:
        completed_lines = 1
    elif cell_change == -16:
        #completed_lines = 2
        completed_lines = 4
    elif cell_change == -26:
        #completed_lines = 3
        completed_lines = 16
    elif cell_change == -36:
        #completed_lines = 4
        completed_lines = 64

    bumpiness = 0
    for x in range(9):
        for y in range(24):
            topx = 0
            topnextx = 0
            if (x,y) in board.cells:
                topx = (24 -y)
                break
            if (x+1,y) in board.cells:
                topnextx = (24 - y)
                break
        bumpiness += abs(topx - topnextx)

    #smaller score better
    # weight heuristics belowwwwwww
    score = 4 * holes + aggregate_height + 2 *bumpiness - 6 * completed_lines
    #print("aggregate height : ",aggregate_height,"holes: ",holes,"cell change: ",cell_change,"completed lines: ",completed_lines,"SCORE: ",score)
    return score