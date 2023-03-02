from mindgame import MindGame
from mindgame.strategy import BruteForceStrategy, RandomStrategy

if __name__ == '__main__':
    game = MindGame()

    for strategy in [RandomStrategy(game),
                     BruteForceStrategy(game)]:
        total = 0
        i = 0
        for x in range(300):
            game.reset()
            try:
                steps = strategy.solve()
                total += steps
                i += 1
            except Exception as e:
                print(e)
        print(f"Average steps for {strategy.__class__.__name__}: {total / i:.0f}")
