
import matplotlib.pyplot as plt
import numpy as np

from coinPuzzle import CoinPuzzle
class Chessboard(CoinPuzzle):

    def __init__(self, rows, columns, key, **kwargs):
        super().__init__(rows, columns, key, **kwargs)

    def plot(self):   # Plot the chessboard with the binary representation of the key
        fig, ax = plt.subplots()
        ax.set_xticks(np.arange(self._rows+1))
        ax.set_yticks(np.arange(self._columns+1))
        plt.axis("square")
        key = self.keycode()
        flip = self.calculate()
        # print(f"key {self.keycode()}, flip {self.calculate()}")
        for i in range(8):
            for j in range(8):
                if key == bin(8 * i + j):
                    text = ax.text(j + 0.2, i + 0.3, "KEY", color="w", weight='bold')
                if flip == bin(8 * i + j):
                        text = ax.text(j + 0.2, i + 0.3, "FLIP", color="w", weight='bold')
                if self._coinsBin[i][j]:
                    square_color = 'green'
                else:
                    square_color = 'blue'
                ax.add_patch(plt.Rectangle((j, i), 1, 1, fill=True, color=square_color))
        ax.grid(color='white', linewidth=5, linestyle='-', alpha=1.0)
        plt.show()