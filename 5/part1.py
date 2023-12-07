def generate_fx(conv_key: str, conv_maps: str):
    function_definitions = []
    for conv_map in conv_maps.strip().split('\n'):
        to_num, from_num, range_length = [int(d) for d in conv_map.split(' ')]

        fx_def = {
            'condition': range(from_num, from_num + range_length),
            'offset': to_num - from_num
        }

        function_definitions.append(fx_def)


    def fx(from_num: int):
        for definition in function_definitions:
            if from_num in definition['condition']:
                return from_num + definition['offset']

        return from_num

    from_unit, _, to_unit = conv_key[:-5].split('-')
    return from_unit, to_unit, fx


with open('./5/input.txt', 'r') as f:
    seeds = [int(i) for i in f.readline()[7:-1].split(' ')]
    f.readline()

    funcs = {}
    for group in f.read().split("\n\n"):
        from_unit, to_unit, func = generate_fx(*group.split('\n', maxsplit=1))

        funcs[(from_unit, to_unit)] = func


def seed_to_location(num):
    unit_path = ('seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location')
    func_path = list(zip(unit_path[:-1], unit_path[1:]))

    running_num = num
    for func_key in func_path:
        running_num = funcs[func_key](running_num)
        # doing this iteratively instead of recursively, just because its simpler

    return running_num


print(min([seed_to_location(seed) for seed in seeds]))