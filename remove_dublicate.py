def remove_duplicates(lst):
    # Your code goes here
    result=[]
    for i in lst:
        if i not in result:
            result.append(i)
    return result