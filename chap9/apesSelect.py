class Monkey:
    id = 0
    def __init__(self, name, strength, intelligence, agility):
        self.name = name
        self.str = strength
        self.int = intelligence
        self.agi = agility
        self.id = Monkey.id
        Monkey.id += 1
        
    def __repr__(self) -> str:
        return str(self.id) + "-" + str(self.name)

    def getAttribute(self, attri):
        if attri == "name":
            return self.name
        elif attri == "str":
            return self.str
        elif attri == "int":
            return self.int
        elif attri == "agi":
            return self.agi
        

    def compare(self, other, attri_l, order):
        if order == "A":
            for attri in attri_l:
                if self.getAttribute(attri) > other.getAttribute(attri):
                    return False
                elif self.getAttribute(attri) < other.getAttribute(attri):
                    return True
            
        else:
            for attri in attri_l:
                if self.getAttribute(attri) < other.getAttribute(attri):
                    return False
                elif self.getAttribute(attri) > other.getAttribute(attri):
                    return True
        return True
    
def merge(arr1, arr2, attri_l, order):
    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i].compare(arr2[j], attri_l, order):
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        result.append(arr2[j])
        j += 1
    return result
    
def mergeSort(arr, attri_l, order):    #7 3 2 16 24 4 11 9
    if len(arr) <= 1:
        return arr
    m = len(arr)//2
    left = mergeSort(arr[0:m], attri_l, order) #2 3 7 16
    right = mergeSort(arr[m:], attri_l, order) #4 9 11 24
    return merge(left, right, attri_l, order)

inp = input("Enter Input: ").split("/")
order = inp[0]
if not inp[1]:
    attri_l = []
else:
    attri_l = inp[1].split(",")
monkeys = inp[2].split(",")
monkey_list = []
for monkey in monkeys:
    attri = monkey.split()
    monkey_list.append(Monkey(attri[0], int(attri[1]), int(attri[2]), int(attri[3])))
if attri_l:
    monkey_list = mergeSort(monkey_list, attri_l, order)
print(f"[{', '.join([f'{monkey}' for monkey in monkey_list])}]")