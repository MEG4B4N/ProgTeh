import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Крестики-Нолики")
        self.size = 10
        self.cell_size = 50
        self.board = [[0] * self.size for _ in range(self.size)]
        self.current_player = 1

        self.buttons = [[None] * self.size for _ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                button = tk.Button(master, width=4, height=2, command=lambda x=i, y=j: self.click(x, y))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

        # Метка для отображения текущего игрока
        self.status_label = tk.Label(master, text="Ход игрока 1 (X)", font=("Arial", 14))
        self.status_label.grid(row=self.size, columnspan=self.size)

    def click(self, x, y):
        if self.board[x][y] == 0:
            self.board[x][y] = self.current_player
            self.buttons[x][y].config(text='X' if self.current_player == 1 else 'O', fg='black')

            if self.check_winner(x, y):
                winner = "Игрок 1 (X)" if self.current_player == 1 else "Игрок 2 (O)"
                messagebox.showinfo("Победа!", f"{winner} выиграл!")
                self.reset_game()
            else:
                self.current_player = 3 - self.current_player  # Смена игрока
                self.update_status()  # Обновляем статус

    def check_winner(self, x, y):
        for dx, dy in [(1, 0), (0, 1), (1, 1), (1, -1)]:
            count = 1
            count += self.count_in_direction(x, y, dx, dy)
            count += self.count_in_direction(x, y, -dx, -dy)
            if count >= 4:
                return True
        return False

    def count_in_direction(self, x, y, dx, dy):
        count = 0
        player = self.board[x][y]
        while True:
            x += dx
            y += dy
            if 0 <= x < self.size and 0 <= y < self.size and self.board[x][y] == player:
                count += 1
            else:
                break
        return count

    def reset_game(self):
        self.board = [[0] * self.size for _ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                self.buttons[i][j].config(text='', state='normal')
        self.current_player = 1
        self.update_status()  # Обновляем статус при сбросе игры

    def update_status(self):
        # Обновляем текст метки в зависимости от текущего игрока
        self.status_label.config(text=f"Ход игрока {self.current_player} ({'X' if self.current_player == 1 else 'O'})")

# Создание основного окна и запуск игры
root = tk.Tk()
game = TicTacToe(root)
root.mainloop()