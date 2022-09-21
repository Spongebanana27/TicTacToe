from board import board

b = board()
b.display()

while not board.isWin() and not b.isFull():
    print(b.turn + " Player's Turn")
    col = int(input("Enter column: "))
    row = int(input("Enter row: "))
    while b.place(row, col) == 0:
        col = int(input("Enter column: "))
        row = int(input("Enter row: "))

    b.nextTurn()
    b.display()

if b.isWin():
    b.nextTurn()
    print(b.turn + " Player wins!")
else:
    print("Tie!")