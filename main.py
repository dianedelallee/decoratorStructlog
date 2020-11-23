from models import Player
from initialization import init_app

if __name__ == '__main__':
    init_app()

    player_1 = Player(name='Diane', age=30)
    player_1.get_name()
    player_1.get_age_in_cat_live()
