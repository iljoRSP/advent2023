with open('./2/input.txt', 'r') as f:
    sum_of_power = 0
    for game in f.readlines():
        game = game.split(': ')[1]  # drop 'Game XX:' at start
        # game = '4 green, 3 blue, 11 red; 7 red, 5 green, 10 blue; 3 green, 8 blue, 8 red; 4 red, 12 blue; 15 red, 3 green, 10 blue'

        highest = {
            'red': 0,
            'green': 0,
            'blue': 0
        }

        for pull in game.split('; '):
            # pull = '4 green, 3 blue, 11 red'

            for per_color in pull.split(', '):
                # per_color = '4 green'

                amt, col = per_color.strip().split(' ')

                highest[col] = max(int(amt), highest[col])


        sum_of_power += highest['red'] * highest['blue'] * highest['green']


    print(sum_of_power)