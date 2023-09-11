import time
from random import Random

from board import Action, Direction, Rotation

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

    def move_to_target(self,board,rpointer,rotations):
        if rpointer < board.falling.right:
            while board.falling.right != rpointer and board.falling.left != 0:
                if(board.move(Direction.Left)):
                    return
        elif rpointer > board.falling.right:
            while board.falling.right != rpointer and board.falling.right != 9:
                if(board.move(Direction.Right)):
                    return
        for i in range (rotations):
            if(board.rotate(Rotation.Anticlockwise)):
                return
        if rpointer < board.falling.right:
            while board.falling.right != rpointer and board.falling.left != 0:
                if(board.move(Direction.Left)):
                    return
        elif rpointer > board.falling.right:
            while board.falling.right != rpointer and board.falling.right != 9:
                if(board.move(Direction.Right)):
                    return
        board.move(Direction.Drop)
        #self.print_board(board)

    def scoreboard(self,board,test):      
        #self.print_board(board)
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
            a = 1.41
            b = 0.50
            c = 1.16

        
        #smaller score better
        # weight heuristics belowwwwwww
        score =  a * holes + b * aggregate_height / 10 + c * bumpiness - d * completed_lines
        score_array = [score,holes,aggregate_height,completed_lines,bumpiness,score]
        #print("holes: ",score_array[1],"aggregate height : ",score_array[2],"completed lines: ",score_array[3],"bumpiness: ",score_array[4],"SCORE: ",score_array[5])
        return score_array

    def make_best_move(self,board,rpointer,rotations):
        moves = []
        if rpointer < board.falling.right:
            while board.falling.right != rpointer and board.falling.left != 0:
                moves.append(Direction.Left)
                if(board.move(Direction.Left)):
                    return moves
        elif rpointer > board.falling.right:
            while board.falling.right != rpointer and board.falling.right != 9:
                moves.append(Direction.Right)
                if(board.move(Direction.Right)):
                    return moves
        for i in range (rotations):
            moves.append(Rotation.Anticlockwise)
            if(board.rotate(Rotation.Anticlockwise)):
                return moves
        if rpointer < board.falling.right:
            while board.falling.right != rpointer and board.falling.left != 0:
                moves.append(Direction.Left)
                if(board.move(Direction.Left)):
                    return moves
        elif rpointer > board.falling.right:
            while board.falling.right != rpointer and board.falling.right != 9:
                moves.append(Direction.Right)
                if(board.move(Direction.Right)):
                    return moves
        board.move(Direction.Drop)
        moves.append(Direction.Drop)
        #print("rpointer ",rpointer," rotations ",rotations)
        return moves

    def choose_action(self, board):
        #time.sleep(1)
        rpointer = 0
        best_score = 1000000
        best_pointer = 0
        best_no_rotations = 0
        for y in range(4):
            for rpointer in range(10):
            #for y in range(4):
                test = board.clone()
                self.move_to_target(test,rpointer,y)
                score = self.scoreboard(test,board)
                if score[0] < best_score:
                    best_score = score[0]
                    best_pointer = rpointer
                    best_no_rotations = y
        
        test = board.clone()
        #print("holes: ",score[1],"aggregate height : ",score[2] / 10,"completed lines: ",score[3],"bumpiness: ",score[4],"SCORE: ",score[5])
        return self.make_best_move(test,best_pointer,best_no_rotations)

SelectedPlayer = MyPlayer

        #for all positions
            #for all rotations
                #clone board  
                #move to target()
                #score board()
        #!!!_return make best move()_!!!