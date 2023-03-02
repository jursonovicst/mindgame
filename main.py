from mindgame import MindGame
from mindgame.strategy import BruteForceStrategy, RandomStrategy

if __name__ == '__main__':
    game = MindGame()

    for strategy in [RandomStrategy(game.width, game.numcolors), BruteForceStrategy(game.width, game.numcolors)]:
        total = 0
        i = 0
        for x in range(200):
            game.reset()
            try:
                steps = game.solve(RandomStrategy(game.width, game.numcolors))
                total += steps
                i += 1
            except Exception as e:
                print(e)
        print(f"Average steps for {strategy.__class__.__name__}: {total / i:.0f}")
