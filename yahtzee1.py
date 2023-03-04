from random import randint

def make_roll() -> tuple:
    """
    Returns a tuple of five random values between 1 and 6.
    """
    # use randint to generate random values between 1 and 6
    roll = tuple(randint(1,6) for _ in range(5))
    print("Rolling the dice... ",roll)

    return roll

def sum_of_given_number(roll: tuple, number: int) -> int:
    """
    Returns the sum of the values in the roll that match the given number.
    """
    sum_of_number = 0
    for value in roll:
        if value == number:
            sum_of_number += value

    return sum_of_number

def fill_upper_section(roll: tuple) -> list:
    """
    Returns a list of the sums of all values in the roll.
    """
    # create upper-section with all value as 0 
    upper_section = [0]*6

    # using set we only get unique value
    for value in set(roll):
        # index starts from 0, so (value - 1)
        upper_section[value - 1] = sum_of_given_number(roll, value) 

    print("Upper section: ", upper_section)
    return upper_section

def display_upper_section(upper_section_scores: list) -> None:
    """
    Displays the upper section.
    """
    # define all faces name, we can use it later
    face_names = ["Aces", "Twos", "Threes", "Fours", "Fives", "Sixes"]
    separator = ":"

    for index,score in enumerate(upper_section_scores):
        print(face_names[index] + separator, score)

def main():
    """
    Main function.
    """
    roll = make_roll()
    
    upper_section = fill_upper_section(roll)

    display_upper_section(upper_section)

if __name__ == "__main__":
    main()
