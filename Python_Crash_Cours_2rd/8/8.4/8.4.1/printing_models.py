'''
# 首先创建一个列表，其中包含一些要打印的设计。
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron'] 
completed_models = []

# 模拟打印每个设计，直到没有未打印的设计为止。
# 打印每个设计后，都将其移到列表completed_models中。 
while unprinted_designs:
    current_design = unprinted_designs.pop() 
    print(f"Printing model: {current_design}") 
    completed_models.append(current_design)

# 显示打印好的所有模型。
print("\nThe following models have been printed:") 
for completed_model in completed_models:
    print(completed_model)
'''

def print_models(unprinted_designs, completed_models):
    """
    遍历列表并输出，输出完成后移动到completed_models
    """
    while unprinted_designs:
        current_desgin = unprinted_designs.pop()
        print(f"Printing model: {current_desgin}")
        completed_models.append(current_desgin)
def show_completed_models(completed_models):
    """输出处理完成清单"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron'] 
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
