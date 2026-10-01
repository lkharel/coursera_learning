"""Practice passing functions as arguments."""


def invoke_thrice(func) -> None:
    """Call a function three times."""
    func()
    func()
    func()


def sample() -> None:
    """Print sample output."""
    print("A")
    print("B")
    print("C\n")


if __name__ == "__main__":
    invoke_thrice(sample)
