import click
from card_knockout_game.player import Player
from card_knockout_game.card_knockout_game import CardKnockoutGame


def validate_cards(ctx, param, value):
    if value <= 0:
        raise click.BadParameter('number of card must greater than 0')

    modulo_cards = value % 4

    if modulo_cards == 0:
        return value
    else:
        raise click.BadParameter('Number of cards must be multiple of 4')


@click.command()
@click.option('--player1', '-p1', default='John',  help='name of player 1')
@click.option('--player2', '-p2', default='Andrew', help='name of player 2')
@click.option('--verbose', '-v', is_flag=True, help='print more output.')
@click.option('--cards', '-c', default=52, type=int, callback=validate_cards,  help='number of cards')
def play(player1, player2, verbose, cards):
    game = CardKnockoutGame(Player(player1), Player(player2), number_cards=cards)

    if verbose:
        print(f'{player1} deck:')
        print(game.cards_player_1)
        print('-----------------------------')
        print(f'{player2} deck:')
        print(game.cards_player_2)
        print('-----------------------------')
        print('Score:')
        print(game.score)
        print('-----------------------------')

    print(game.check_result())


@click.command()
@click.option('--player1', '-p1', default='John',  help='name of player 1')
@click.option('--player2', '-p2', default='Andrew', help='name of player 2')
@click.option('--verbose', '-v', is_flag=True, help='print more output.')
@click.option('--cards', '-c', default=52, type=int, callback=validate_cards,  help='number of cards')
@click.option('--games', '-g', default=10, type=int, help='number of games')
def simulate(player1, player2, verbose, cards, games):
    first_player = Player(player1)
    second_player = Player(player2)
    for _ in range(games):
        game = CardKnockoutGame(first_player, second_player, number_cards=cards)
        if verbose:
            print('Score:')
            print(game.score)
            print(game.check_result())
            print('-----------------------------')

    print(f'{player1} won {first_player.games_won} games')
    print(f'{player2} won {second_player.games_won} games')
    print(f'They tied {second_player.games_played - ( second_player.games_won + second_player.games_lost)} games')
