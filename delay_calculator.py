class Delay:
    def __init__(self, bpm, multiplier):
        """
        :param bpm: Beats Per Minute - tempo measurement unit
        :param multiplier: 1.0 - for standard notes, 0.667 for triplets, 1.5 for dotted
        """

        self.bpm = bpm
        self.multiplier = multiplier

    def calculate(self):
        """
        Returns a list of calculated delay times (in ms), from whole note to 64th
        :rtype: list
        """
        q = 60000 / self.bpm * self.multiplier
        result = [q*4, q*2, q, q/2, q/4, q/8, q/16]
        return result


def user_input():
    """
    Handles all user input and prevents the user from breaking the script.
    :rtype: Returns BPM if user input is correct, or False if the user wants to end the script.
    """

    while True:
        usr = input("""Type 'N' to end script.
Provide BPM (assuming quarter note beat): """)
        if usr == 'n' or usr == 'N':
                print("Terminating")
                return False

        try:
            if float(usr) in range(1, 10001):
                return float(usr)
            else:
                print("BPM must be between 1 and 10 000.")
        except ValueError:
            print("Invalid input. Provide a number or type 'N' to terminate.")


def table(col1, col2, col3):
    """
    This function outputs the calculated times in a pretty table format.
    :param col1, col2, col3: Lists of calculated delay times (Delay.calculate).
    """
    divisions = ["1/1", "1/2", "1/4", "1/8", "1/16", "1/32", "1/64"]
    data = [divisions, col1, col2, col3]

    # Prints table header
    print("{:<10} {:<13} {:<13} {:<13}".format("unit: ms", "Notes", "Triplets", "Dotted"))

    # Prints the calculations as a table
    for i in range(7):
        print("{:.<10} {:.<13.2f} {:.<13.2f} {:<13.2f}".format(data[0][i], data[1][i], data[2][i], data[3][i]))


if __name__ == "__main__":
    while True:
        tempo = user_input()
        if not tempo:
            break

        note = Delay(tempo, 1.0)
        triplet = Delay(tempo, 0.667)
        dotted = Delay(tempo, 1.5)

        table(note.calculate(), triplet.calculate(), dotted.calculate())
