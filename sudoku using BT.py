{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Sudoku Solver using Python\n",
    "### Algorithm used -: Backtracking"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "board = [\n",
    "    [7,8,0,4,0,0,1,2,0],\n",
    "    [6,0,0,0,7,5,0,0,9],\n",
    "    [0,0,0,6,0,1,0,7,8],\n",
    "    [0,0,7,0,4,0,2,6,0],\n",
    "    [0,0,1,0,5,0,9,3,0],\n",
    "    [9,0,4,0,6,0,0,0,5],\n",
    "    [0,7,0,3,0,0,0,1,2],\n",
    "    [1,2,0,0,0,7,4,0,0],\n",
    "    [0,4,9,2,0,6,0,0,7]\n",
    "]\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7 8 0  | 4 0 0  | 1 2 0\n",
      "6 0 0  | 0 7 5  | 0 0 9\n",
      "0 0 0  | 6 0 1  | 0 7 8\n",
      "- - - - - - - - - - - - - \n",
      "0 0 7  | 0 4 0  | 2 6 0\n",
      "0 0 1  | 0 5 0  | 9 3 0\n",
      "9 0 4  | 0 6 0  | 0 0 5\n",
      "- - - - - - - - - - - - - \n",
      "0 7 0  | 3 0 0  | 0 1 2\n",
      "1 2 0  | 0 0 7  | 4 0 0\n",
      "0 4 9  | 2 0 6  | 0 0 7\n",
      "_________________________________________\n",
      "7 8 5  | 4 3 9  | 1 2 6\n",
      "6 1 2  | 8 7 5  | 3 4 9\n",
      "4 9 3  | 6 2 1  | 5 7 8\n",
      "- - - - - - - - - - - - - \n",
      "8 5 7  | 9 4 3  | 2 6 1\n",
      "2 6 1  | 7 5 8  | 9 3 4\n",
      "9 3 4  | 1 6 2  | 7 8 5\n",
      "- - - - - - - - - - - - - \n",
      "5 7 8  | 3 9 4  | 6 1 2\n",
      "1 2 6  | 5 8 7  | 4 9 3\n",
      "3 4 9  | 2 1 6  | 8 5 7\n"
     ]
    }
   ],
   "source": [
    "def solve(board):\n",
    "    find = find_empty(board)\n",
    "    if not find:  \n",
    "        return True                       # it will return true only when their is no more spaces left\n",
    "    else:\n",
    "        row, col = find\n",
    "\n",
    "    for i in range(1,10):\n",
    "        if valid(board, i, (row, col)):\n",
    "            board[row][col] = i\n",
    "\n",
    "            if solve(board):            # call solve again with new board each time till we solve the whole board\n",
    "                return True\n",
    "\n",
    "            board[row][col] = 0\n",
    "\n",
    "    return False\n",
    "\n",
    "#to check if entered number is valid or not\n",
    "def valid(board, num, pos):  \n",
    "    #to Check in the row\n",
    "    for i in range(len(board[0])):\n",
    "        if board[pos[0]][i] == num and pos[1] != i:    #we entered two values for pos i.e. i and j so pos[0]=row and pos[1]=column\n",
    "            return False\n",
    "\n",
    "    #to Check in the column\n",
    "    for i in range(len(board)):\n",
    "        if board[i][pos[1]] == num and pos[0] != i:\n",
    "            return False\n",
    "\n",
    "    #to Check each box\n",
    "    box_x = pos[1] // 3\n",
    "    box_y = pos[0] // 3\n",
    "\n",
    "    for i in range(box_y*3, box_y*3 + 3):\n",
    "        for j in range(box_x * 3, box_x*3 + 3):\n",
    "            if board[i][j] == num and (i,j) != pos:\n",
    "                return False\n",
    "\n",
    "    return True\n",
    "\n",
    "\n",
    "#print board in a easily readable way.\n",
    "def print_board(board):                                \n",
    "    for i in range(len(board)):                    #iterate through column\n",
    "        if i % 3 == 0 and i != 0:\n",
    "            print(\"- - - - - - - - - - - - - \")     \n",
    "\n",
    "        for j in range(len(board[0])):             #iterate through each individual rows\n",
    "            if j % 3 == 0 and j != 0:\n",
    "                print(\" | \", end=\"\")\n",
    "\n",
    "            if j == 8:\n",
    "                print(board[i][j])\n",
    "            else:\n",
    "                print(str(board[i][j]) + \" \", end=\"\")\n",
    "\n",
    "\n",
    "#to find empty space on board which is needed to be filled\n",
    "def find_empty(board):\n",
    "    for i in range(len(board)):\n",
    "        for j in range(len(board[0])):\n",
    "            if board[i][j] == 0:\n",
    "                return (i, j)  # returns row,column\n",
    "\n",
    "    return None\n",
    "\n",
    "print_board(board)\n",
    "solve(board)\n",
    "print(\"_________________________________________\")\n",
    "print_board(board)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
