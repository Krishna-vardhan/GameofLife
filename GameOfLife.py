
# creating a class for game of life
class GameOfLife:
    def __init__(self):
        self.board = [[0]*20]*20  # 2D list of size 20x20 with all values as 0 is created

    # this method return the sum of live neighbours in 8 directions
    def neighbourSum(self,i,j):
        sum = 0
        n=len(self.board)
        
        if(self.board[(i-1+n)%n][(j-1+n)%n]==1):
            sum += 1
        if(self.board[(i-1+n)%n][j]==1):
            sum += 1
        if(self.board[(i-1+n)%n][(j+1)%n]==1):
            sum += 1
        if(self.board[i%n][(j+1)%n]==1):
            sum += 1
        if(self.board[(i+1)%n][(j+1)%n]==1):
            sum += 1
        if(self.board[(i+1)%n][j]==1):
            sum += 1
        if(self.board[(i+1)%n][(j-1+n)%n]==1):
            sum += 1
        if(self.board[i][(j-1+n)%n]==1):
            sum += 1
        return sum

    # this method generats the next pattern based on the rules of GLT
    def nextPattern(self):
        for i in range(20):
            for j in range(20):
                sum = self.neighbourSum(i,j)    # neighbourSum is called to get the sum of neighbours of current cell

                if (sum < 2 and self.board[i][j]==1): # less than two living neighbours causes a live cell to expire
                    self.board[i][j] = 0
                if(sum >= 2 and sum <=3 and self.board[i][j]==1): #living cell with two or three other living neighbours
                    self.board[i][j] = 1
                if(sum > 3 and self.board[i][j]==1): #More than three live neighbours in a live cell results in death.
                    self.board[i][j] = 0
                if(sum == 3 and self.board[i][j]==0): #Exactly three live neighbours transform a dead cell into an alive cell.
                    self.board[i][j] = 1
            
    #this method print's the board
    def printBoard(self): 
        for i in range(20):
            for j in range(20):
                if(self.board[i][j]==0): # if condition is true if current cell value is 0 and white space is printed
                    print(' ',end=' ')
                else:
                    print('*',end=' ') # else block is executed when current cell value is 1 and * is printed
            print()


def main():
    
    #creating initial patterns
    pattern1 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,1,1,1,0,0,1,1,0,1,1,0,0,1,1,1,0,0,0],
    [0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0],
    [0,0,1,1,1,0,0,1,1,0,1,1,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

    pattern2 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

    pattern3 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0],
    [0,0,1,0,0,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0],
    [0,1,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0,1,0,0],
    [0,0,1,0,0,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

    p = GameOfLife() #instance for a class is created

    patterns = {1:pattern1,2:pattern2,3:pattern3} 

    # Prinring all the initial patterns
    for i in range(3):    
        print('patterns'+str(i+1))    
        p.board = patterns[i+1]
        p.printBoard()
        print()

    # choosing a initial pattern to start the game
    while(1):        
        yourPattern = int(input("Choose a pattern to start the game(1,2 or 3):"))        
        if(yourPattern in patterns):
            p.board = patterns[yourPattern]
            break
        else:
            print('Invalid pattern selected!') # else block is executed when user select invalid option
    
    # this block repeatedly prints the next pattern until user ends the game.
    while(1):
        p.printBoard()
        next = input('To print the next pattern enter y/Y. To end the game enter any other symbol:')

        if(next != 'y' and next != 'Y'): # this condition is true when user wants to exit the game
            print('Thank you for playing.')
            break
        p.nextPattern() 

if __name__ == "__main__":
    main()