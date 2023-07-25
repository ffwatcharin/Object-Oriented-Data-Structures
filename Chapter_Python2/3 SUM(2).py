def findSumTriple(list1, triple, res):
    if len(triple) == 3 and sum(triple) == 5 and set(triple) not in [set(x) for x in res]:
        triple.sort()
        res.append(triple)
        return
    elif len(triple) == 3 or not list1:
        return
    
    findSumTriple(list1[1:], triple + [list1[0]], res)
    findSumTriple(list1[1:], triple, res)

list1 = [int(x) for x in input('Enter Your List : ').split()]
res = []
triple = []

if len(list1) < 3:
        print('Array Input Length Must More Than 2')
else:
    findSumTriple(list1, triple, res)
    print(res)

