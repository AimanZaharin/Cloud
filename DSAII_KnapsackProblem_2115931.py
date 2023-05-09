
class Items:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


def main():

    #Declaration of Items Class in an array
    array = [Items(20,2), Items(30,5), Items(50,10), Items(10,5)]
    #Declaration of maximum weight of the knapsack
    w = 16

    #Sorting the array from the most valued to the least valued
    array.sort(key=lambda x: (x.value/x.weight), reverse=True) 

    totalValue = 0.0

    for item in array:

        if item.weight <= w:
            w -= item.weight
            totalValue += item.value

        else:
            totalValue += item.value * w / item.weight
            break
    
    print(totalValue)
        
main()

    

