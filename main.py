from chessboard import Chessboard
from farmers import plot_farmers
class Main:
    def run(self):
        input_value = input("Give an Integer: ")

        try:
            value = int(input_value)

            if value == 1:
                # Plot the farmer production representation from description matplotlib
                plot_farmers()

            elif value == 2:
                # generate and plot the chessboard
                key_location = 27
                chessboard = Chessboard(rows=8,columns=8,key=key_location)
                chessboard.plot()
                chessboard.print()

        except ValueError:
            print("wrong input: give a numer please")

if __name__ == '__main__':
    main = Main()
    main.run()