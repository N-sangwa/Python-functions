from itertools import product


def multiply_and_greet(*numbers,**attributes):
    product = 1
    for x in numbers:
        product *=x
    print(f"Hello {attributes['name']} from  {attributes['country']} your score is {product}")
    
            


