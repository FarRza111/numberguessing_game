from error_handler import *

def roll_dice(amount: int = 2) -> list[int]:
    """
    :param amount: the amount of dice to roll
    :return: a list of dice rolls
    """
    if amount <= 0:
        raise LessThanZero('it is less than zero')

    rolls: list[int] = []
    for i in range(amount):
        random_roll: int = random.randint(1, 6)
        rolls.append(random_roll)

    return rolls


def main():
    while True:
        try:
            user_input: str = input("How many dice would you like to roll:")

            if user_input.lower() == 'exit':
                print("Playing stopped, thanks..")
                break

            amount = int(user_input)
            print(*roll_dice(amount), sep=', ')

        except ValueError:
            print('Input is not a valid integer')
        except LessThanZero as e:
            print(e)
        except StringError as e:
            print(e)


if __name__ == "__main__":
    main()
