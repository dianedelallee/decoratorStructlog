from typing import Optional

class Player:

    def __init__(self, name: Optional[str] = None, age: Optional[int] = None) -> None:
        self.name = name if name else 'Player 1'
        self.age = age if age else 18
        self.level = 0
        self.experience = 0

    def get_name(self):
        return self.name

    def set_name(self, new_name: str) -> None:
        self.name = new_name

    def get_age_in_cat_live(self) -> int:
        return self.age * 7
