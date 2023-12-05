with open('./2/input.txt', 'r') as f:
    max = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    sum_of_game_num = 0
    current_game = 0
    for line in f.readlines():
        line = line.split(': ')[1]  # drop 'Game XX:' at start
        # line = '4 green, 3 blue, 11 red; 7 red, 5 green, 10 blue; 3 green, 8 blue, 8 red; 4 red, 12 blue; 15 red, 3 green, 10 blue'

        current_game += 1
        game_valid = True

        for pull in line.split('; '):
            # pull = '4 green, 3 blue, 11 red'
            if not game_valid: break

            for per_color in pull.split(', '):
                # per_color = '4 green'
                if not game_valid: break

                amt, col = per_color.strip().split(' ')
                game_valid &= int(amt) <= max[col]


        if game_valid: sum_of_game_num += current_game

    print(sum_of_game_num)