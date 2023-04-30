

def main():
    Coins = [6, 5, 1];
    value = 9

    numOfways = [0] * (value +1)
    numOfways[0] = 1

    for i in range(len(Coins)):
        for j in range(len(numOfways)):
            if (Coins[i] <= j):
 
                # Update the ways array
                numOfways[j] += numOfways[(int)(j - Coins[i])];

    print(numOfways[value])


    

main()