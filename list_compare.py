def list_compare(list1,list2):
    set1 = set(list1)
    set2 = set(list2)

    set1_only = [x for x in list1 if x not in set2]
    set2_only = [x for x in list2 if x not in set1]
    set3 = (set1_only + set2_only)
    
    return set3

def main():
    list_x = [13, 5, 6, 2, 5,77]
    list_y = [5, 2, 5, 13, 7,69]

    set3 = list_compare(list_x, list_y)
    
    #print each number 
    for x in set3:
        print(x)
        #return x

    #print a list of all numbers
    print(set3)
    

main()
