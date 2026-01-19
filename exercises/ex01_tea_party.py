"""This exercise uses an inputed number of guests to calculate the quantity of tea bags needed, the number of treats needed, and the expected cost of the tea party."""

__author__: str = "730934513"


def main_planner(guests: int) -> None:
    """A function that calls each function below to calculate quantity of tea bags needed, the number of treats to accompany the tea, and the expected cost of the party."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests))))


def tea_bags(people: int) -> int:
    """A function that computes the number of tea bags needed based on the number of guests."""
    return people * 2


def treats(people: int) -> int:
    """A function that computes the number of treats needed based on the number of teas guests are expecting to drink."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """A function that computes the cost of tea bags and treats combined."""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
