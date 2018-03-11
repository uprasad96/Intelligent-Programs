import sys
import warnings
warnings.filterwarnings('ignore')
board = [2,2,2,2,2,2,2,2,2]
rows = [[0,1,2],[3,4,5],[6,7,8]]
cols = [[0,3,6],[1,4,7],[2,5,8]]
diags = [[0,4,8],[2,4,6]]
options = [rows,cols,diags]
turn = [1]

def make2():
    if board[4] == 2:
        return 4
    elif board[1] == 2:
        return 1
    elif board[3] == 2:
        return 3
    elif board[5] == 2:
        return 5
    else:
        return 7

def posswin(p):
    if p == 'X':
        for option in options:
            for op in option:
                mul = 1
                blank = -1
                for ind in op:
                    mul = mul * board[ind]
                    if board[ind] == 2:
                        blank = ind
                if mul == 18:
                    return blank
        return 0
    elif p == 'O':
        for option in options:
            for op in option:
                mul = 1
                blank = -1
                for ind in op:
                    mul = mul * board[ind]
                    if board[ind] == 2:
                        blank = ind
                if mul == 50:
                    return blank
        return 0

def go(n,turn):
    if turn[0] % 2 == 1:
        board[n] = 3
    else:
        board[n] = 5
    turn[0] = turn[0] + 1

def goanywhere(turn):
    for i in xrange(0,9):
        if board[i] == 2:
            go(i,turn)
            break

def move(turn):
    if turn[0] == 1:
        go(0,turn)
    elif turn[0] == 2:
        if board[4] == 2:
            go(4,turn)
        else:
            go(0,turn)
    elif turn[0] == 3:
        if board[8] == 2:
            go(8,turn)
        else:
            go(2,turn)
    elif turn[0] == 4:
        if posswin('X') != 0:
            go(posswin('X'),turn)
        else:
            go(make2(),turn)
    elif turn[0] == 5:
        if posswin('X') != 0:
            go(posswin('X'),turn)
            draw(board)
            print 'AI wins'
            sys.exit()
        elif posswin('O') != 0:
            go(posswin('O'),turn)
        elif board[6] == 2:
            go(6,turn)
        else:
            go(2,turn)
    elif turn[0] == 6:
        if posswin('O') != 0:
            go(posswin('O'),turn)
            draw(board)
            print 'AI wins'
            sys.exit()
        elif posswin('X') != 0:
            go(posswin('X'),turn)
        else:
            go(make2(),turn)
    elif turn[0] == 7:
        if posswin('X') != 0:
            go(posswin('X'),turn)
            draw(board)
            print 'AI wins'
            sys.exit()
        elif posswin('O') != 0:
            go(posswin('O'),turn)
        else:
            goanywhere(turn)
    elif turn[0] == 8:
        if posswin('O') != 0:
            go(posswin('O'),turn)
            draw(board)
            print 'AI wins'
            sys.exit()
        elif posswin('X') != 0:
            go(posswin('X'),turn)
        else:
            goanywhere(turn)
    elif turn[0] == 9:
        if posswin('X') != 0:
            go(posswin('X'),turn)
            draw(board)
            print 'AI wins'
            sys.exit()
        elif posswin('O') != 0:
            go(posswin('O'),turn)
        else:
            goanywhere(turn)

def draw(board):
    print
    k = 0
    for i in xrange(0,3):
        for j in xrange(0,3):
            if board[k] == 2:
                print ' _ ',
            elif board[k] == 3:
                print ' X ',
            else:
                print ' O ',
            k=k+1
        print
        print

def yourMove(n, turn):
    if turn[0] % 2 == 1:
        board[n] = 3
    else:
        board[n] = 5
    turn[0] = turn[0] + 1

if __name__ == '__main__':
    ch = raw_input('X or O ?')
    if ch == 'x' or ch == 'X':
        for i in xrange(0,4):
            yourMove(input('Enter index from 1 to 9: ')-1,turn)
            draw(board)
            print
            print 'AI is thinking...'
            move(turn)
            draw(board)
        yourMove(input('Enter index from 1 to 9: ')-1,turn)
        draw(board)
    if ch == 'o' or ch == 'O':
        for i in xrange(0,4):
            print
            print 'AI is thinking...'
            move(turn)
            draw(board)
            yourMove(input('Enter index from 1 to 9: ')-1,turn)
            draw(board)
        move(turn)
        draw(board)
