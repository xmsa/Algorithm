class Backtracking:
    def __init__(self, size):
        self.__size = size
        self.__board = [0]*size

    def __len__(self):
        return self.__size

    def backtracking(self):
        self.__backtracking()

    def __backtracking(self, item=0):
        if item == self.__size:
            self.print(self.__board)
            return
        for i in range(self.__size):
            self.__board[item] = i
            if not self.__conflict(item):
                self.__backtracking(item+1)

    def __conflict(self, item):
        for i in range(item):
            if self.__board[item] == self.__board[i]:
                return True
        for i in range(item+1):
            for j in range(i+1, item+1):
                k = self.__board[i]
                l = self.__board[j]
                if abs(i-j) == abs(k-l):
                    return True
        return False

    def print(self, __board):
        # for i in self.__board:
        #     print(chr((i%28)+65), end=" ")
        # print()
        print(self.__board)
        print("-"*((len(__board)*2)+1))
        for i in __board:
            print("|", " |"*i, "Q|", " |"*(len(__board)-i-1), sep="")
        print("-"*((len(__board)*2)+1))

