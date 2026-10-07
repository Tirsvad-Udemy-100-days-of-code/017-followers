"""Demo of a simple `User` class with follower counts."""


class User:
    """A user that can follow other users."""

    def __init__(self, user_id: str, username: str) -> None:
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user: "User") -> None:
        """Follow another user, updating both users' counters."""
        user.followers += 1
        self.following += 1


def main() -> None:
    user_1 = User(user_id="001", username="Tirsvad")
    user_2 = User(user_id="002", username="Tirsvad")

    user_1.follow(user_2)

    print(user_1.followers)
    print(user_1.following)
    print(user_2.followers)
    print(user_2.following)


if __name__ == "__main__":
    main()
