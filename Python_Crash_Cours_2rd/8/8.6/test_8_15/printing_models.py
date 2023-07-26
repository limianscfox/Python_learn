from printing_functions import *

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron'] 
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

print("\nunprinted")
for unprinted_design in unprinted_designs:
    print(f"{unprinted_design}")