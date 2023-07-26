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