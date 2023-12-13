import re



def parse_input_file():
    with open('./12/sample.txt', 'r') as f:
        for line in f.readlines():
            springs, counts = line[:-1].split(' ')
            springs = springs.replace('.', '_')  # simplifies matching pattern
            counts = counts.split(',')

            yield springs, counts


for springs, counts in parse_input_file():
    springs = '_' + springs + '_'  # simplifies matching pattern
    springs = re.sub(r'_+', '_', springs)

    print(f'\n\n{springs}  ', end='')
    for c in counts: print(f'{c} ', end='')

    for count in counts:
        pattern = r'(?=([_?][?#]{' + count + r'}[_?]))'
        possible_index_ranges = re.finditer(pattern, springs)

        print(f'\n\t{pattern} matches:')

        for i_r in possible_index_ranges:
            p, q = i_r.span(1)
            print(f'\t\t[{p} {q}]\t->\t{springs[p:q]}')




