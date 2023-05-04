import itertools

def count(items):
    num = 0
    for i in items:
        if i == 1:
            num = num+1
    if num<len(items)/2:
        return True
    else:
        return False

def iterate(vars, mainVariable):
    lst = list(itertools.product([0, 1], repeat=len(vars)))
    items = {}
    for i in lst:
        for j in range(len(vars)):
            items[vars[j]] = i[j]
        #print(items)
        if count(i):
            print("Method insert for", mainVariable, "dictionary is", items, "with probabilities [1,0]")
        else:
            print("Method insert for",mainVariable, "dictionary is", items, "with probabilities [0,1]")

def main():
    vars = ["Fog", "Human", "Test"]
    iterate(vars, "Navigation")


if __name__=="__main__":
    main()