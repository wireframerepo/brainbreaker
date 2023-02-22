import random
# Array inverter implmementation
"""
Array inverter implmementation

certainly we can use native functions to invert a list(array)
but why not play ourselves with that and implement a method
for it?

super basic and barebones algorythm, just pass the original
teams backwards to an auxiliar list and return it and assign
it.
"""

# pass a parameter that is a list
def invert_list(local_list):
    # make a result list that is empty so it receives
    # the flipped list
    result_list = []
    # obtain the length of the parameter list
    # use it as the superior limit to decrement indexes
    # remember to decrement it 1 because a n length list's 
    # top index is equals n-1
    for i in range(len(local_list),0,-1):
        #append each element to the new list
        result_list.append(local_list[i-1])
    return result_list

def main():
    # let us make a list
    the_list = [1,2,3,4,5,6,7,8,42,432,43,342]
    print("INVERTING ARRAY THE OLD WAY")
    print("ORIGINAL LIST")
    print(the_list)
    # invert the list, save it in the original list
    the_list = invert_list(the_list)
    print("invert_list method applied")
    print(the_list)

if __name__=="__main__":
    main()