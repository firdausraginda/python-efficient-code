# ---------------------------------------- The Zip Function ----------------------------------------
names = ['bulbasaur', 'charmander', 'squirtle']
hps = [45, 39, 44]

# example of non-pythonic combining objects ----------------------------------------
combined = []

for i, pokemon in enumerate(names):
    combined.append((pokemon, hps[i]))

print(f'non-pythonic combining objects: {combined}')

# example of pythonic combining objects ----------------------------------------
combined_zip = zip(names, hps)
combined_zip_list = [*combined_zip]

print(f'pythonic combining objects: {combined}')

# ---------------------------------------- The Collections Module ----------------------------------------
# namedtuple: tuple subclasses with named field
# deque: list-like container with fast appends and pops
# Counter: dict for counting hashable objects
# OrderedDict: dict that retains order of entries
# defaultdict: dict that calls a factory function to supply missing values

poke_types = ['grass', 'dark', 'fire', 'fire']

# example of non-pythonic counting ----------------------------------------
type_counts = {}

for poke_type in poke_types:
    if poke_type in type_counts:
        type_counts[poke_type] += 1
    else:
        type_counts[poke_type] = 1

print(f'non-pythonic counting: {type_counts}')

# example of pythonic counting ----------------------------------------
from collections import Counter

count_poke = Counter(poke_types)
print(f'pythonic counting: {count_poke}')

# ---------------------------------------- The Itertools Module ----------------------------------------
# infinite iterators: count, cycle, repeat
# finite iterators: accumulate, chain, zip_longest, etc
# combination generators: product, permutations, combinations

poke_types = ['bug', 'fire', 'ghost', 'grass', 'water']

# example of non-pythonic combinations ----------------------------------------
combos = []

for x in poke_types:
    for y in poke_types:
        if x == y:
            continue
        if ((x,y) not in combos) and ((y,x) not in combos):
            combos.append((x,y))
print(f'non-pythonic combinations: {combos}')

# example of pythonic combinations ----------------------------------------
from itertools import combinations

combos_obj = combinations(poke_types, 2)
combos_obj_list = [*combos_obj]

print(f'pythonic combinations: {combos_obj_list}')

# ---------------------------------------- The Set Type ----------------------------------------
# set datatype has following methods:
# intersection(): all elements that are in both sets
# difference(): all elements in one set but not the other
# symmetric_difference(): all elements in exactly one set
# union(): all elements that are in either set

list_a = ['bulbasaur', 'charmander', 'squirtle']
list_b = ['caterpie', 'pidgey', 'squirtle']

# example of non-pythonic way to find elements that exist in both lists ----------------------------------------
in_common = []

for pokemon_a in list_a:
    for pokemon_b in list_b:
        if pokemon_a == pokemon_b:
            in_common.append(pokemon_a)
        
print(f'non-pythonic way to find elements exist in both lists: {in_common}')

# example of pythonic way to find elements that exist in both lists ----------------------------------------
set_a = set(list_a)
set_b = set(list_b)

intersect = set_a.intersection(set_b)
intersect_list = [*intersect]

print(f'pythonic way to find elements exist in both lists: {intersect_list}')

# example of pythonic way to find elements that exist in one list but not in other ----------------------------------------
set_a = set(list_a)
set_b = set(list_b)

difference = set_a.difference(set_b)
difference_list = [*difference]

print(f'pythonic way to find elements exist in one list but not in other list: {difference_list}')

# example of pythonic way to find elements that exist in exactly one list and not both ----------------------------------------
set_a = set(list_a)
set_b = set(list_b)

symmetric_difference = set_a.symmetric_difference(set_b)
symmetric_difference_list = [*symmetric_difference]

print(f'pythonic way to find elements exist in exactly one list and not both: {symmetric_difference_list}')

# example of pythonic way to collect all unique elements that appear in either or both lists ----------------------------------------
set_a = set(list_a)
set_b = set(list_b)

union = set_a.union(set_b)
union_list = [*union]

print(f'pythonic way to collect all unique elements that appear in either or both lists: {union_list}')

# ---------------------------------------- Eliminate Loops ----------------------------------------
poke_stats = [
    [90, 92, 75, 60],
    [25, 20, 15, 90],
    [65, 130, 60, 75]
]

# example of non-pythonic way to sum row ----------------------------------------
totals = []
for row in poke_stats:
    totals.append(sum(row))

print(f'non-pythonic way to sum row: {totals}')

# example of using list comprehension way to sum row ----------------------------------------
totals_comp = [sum(row) for row in poke_stats]

print(f'using list comprehension way to sum row: {totals}')

# example of using map in list comprehension to sum row ----------------------------------------
totals_sum = [*map(sum, poke_stats)]

print(f'using map in list comprehension to sum row: {totals}')

# ----------------------------------------

# example of using map in list comprehension to find mean row ----------------------------------------
import statistics

mean_sum = [*map(statistics.mean, poke_stats)]

print(f'using map in list comprehension to find mean row: {mean_sum}')

# example of using numpy and list comprehension to find mean row ----------------------------------------
import numpy as np

poke_stats_np = np.array(poke_stats)
mean_np = [np.mean(row) for row in poke_stats_np]
mean_np_list = [*mean_np]

print(f'using numpy & list comprehension to find mean row: {mean_np_list}')

# example of using numpy and axis to find mean row ----------------------------------------
import numpy as np

poke_stats_np = np.array(poke_stats)
mean_simple_np = poke_stats_np.mean(axis=1)
mean_simple_np_list = [*mean_simple_np]

print(f'using numpy and axis to find mean row: {mean_simple_np_list}')