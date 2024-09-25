
def initial_user_input():
    options = ["1", "2", "3"]
    while True:
        user_input = input("Choose your action from below: \n"
                        "1. Play the Game \n"
                        "2. See Results \n"
                        "3. Exit the Game")

        if user_input in options:
            return user_input

        print(f"Please enter a valid option {options}")


def tm_input():
    options = ["w", "s", "a", "d", "t"]
    while True:
        user_input = input("Choose where the tank will go: \n"
                       "w: Up \n"
                       "s: Down \n"
                       "a: Left \n"
                        "d: Right \n"
                        "t: Shoot!")

        if user_input.lower() in options:
            return user_input.lower()

        print(f"Please pick one of the options {options}")