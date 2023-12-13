import re



def parse_input_file():
    with open('./12/input.txt', 'r') as f:
        for line in f.readlines():
            schematic, clusters = line[:-1].split(' ')
            clusters = clusters.split(',')

            yield schematic, clusters


def simplify_schematic(schematic: str) -> str:
    '''
    simplifies the list of springs to an equivalent form
    that requires less from the regex complexity
    '''
    schematic = schematic.replace('.', '_')  # purely to not have to escape . in regex pattern
    schematic = '_' + schematic + '_'
    schematic = re.sub(r'_+', '_', schematic)

    return schematic


def find_matching_ranges(schematic: str, cluster: str) -> list:
    '''
    for a schematic (e.g: ???.###), and a cluster size (e.g.: 1),
    finds all possible places that cluster size can go in the schematic
    (cluster=1 matches _#_, cluster=2 matches _##_, etc.)

    schematic will be optimised for this:
     - consecutive _ is redundant, and is removed
     - a leading and trailing _ is added to match the first and final cluster
    '''
    pattern = re.compile(r'(?=([_?][?#]{' + cluster + r'}[_?]))')
    possible_index_ranges = pattern.finditer(schematic)

    return [i_r.span(1) for i_r in possible_index_ranges]


def count_exact_cover(all_cluster_ranges, i=0, threshold=0):
    '''
    p_ranges will be a list of possible ranges for each cluster.
    an overall possible configuration is one where we pick one range from each cluster where none of the ranges overlap one another.
    also, because the schematic has been optimised, this also means that all characters will be used by the ranges - hence exact cover.

    this function finds all possible combinations of ranges between clusters and counts the number of exact covers
    '''
    exact_covers_found = 0
    ranges_filtered = list(filter(lambda p_r: p_r[0] >= threshold, all_cluster_ranges[i]))

    # if no valid ranges remain, this is an invalid config
    if len(ranges_filtered) == 0:
        return 0

    # if we've reached the last cluster and still have a valid range, then success for all remaining valid ranges
    if i + 1 == len(all_cluster_ranges):
        return len(ranges_filtered)

    # recursively: pick the next smallest range, update threshold, and repeat on next cluster
    for selected_range_for_this_cluster in ranges_filtered:
        # threshold is x-1 because the trailing _ of cluster[n] overlaps with the leading _ of cluster[n+1]
        threshold = selected_range_for_this_cluster[1] - 1

        exact_covers_found += count_exact_cover(all_cluster_ranges, i+1, threshold)

    return exact_covers_found


sum = 0
for schematic, clusters in parse_input_file():
    schematic = simplify_schematic(schematic)
    matching_ranges_of_sizes_in_schematic = {cluster: find_matching_ranges(schematic, cluster) for cluster in set(clusters)}
    actual_ranges_to_match = [matching_ranges_of_sizes_in_schematic[c] for c in clusters]
    num_of_possibilities = count_exact_cover(actual_ranges_to_match)

    sum += num_of_possibilities

    ### logging
    print(f'\n\n{schematic} ', end='')
    for c in clusters:
        print(f'{c} ', end='')

    for c in clusters:
        p_m = matching_ranges_of_sizes_in_schematic[c]
        print(f'\n > len {c} matchable:')
        for start, end in p_m:
            print(f'\t({start},{end})\t->\t{schematic[start:end]}')
    ###

    print('\npossible: ', num_of_possibilities)
    pass

print(sum)

