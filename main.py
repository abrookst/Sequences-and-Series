import math

looping = True
while looping:
    # choosing the sequence
    chosenSequence = 0
    print("Which series/sequence would you like to calculate?")
    print("1) Padovan Sequence")
    print("2) Catalan Numbers")
    print("3) Perrin Numbers")
    print("4) Fermat Numbers")

    while chosenSequence <=0 or chosenSequence >=5:
        chosenSequence = int(input(">"))
        if chosenSequence <=0 or chosenSequence >=5:
            print("Not a valid Series.")

    if chosenSequence == 1:
        print("The Padovan Sequence is a sequence named after Richard Padovan. It is a series of integers defined by the recursive formula P(n) = P(n-2) - P(n-3), and it's values can create a triangular spiral, similar to how Fibbonachi can create a square spiral.")
    elif chosenSequence == 2:
        print("The Catalan Numbers is a sequence named after Eugene Charles Catalan. It is a series of integers defined by the formula (2n)!/((n+1)!*n!), which is equivalent to the product summation (capital pi) of n+k/k from k=2 to n. It has many applications in combinatorics.")
    elif chosenSequence == 3:
        print("Perrin Explanation")
    else:
        print("Fermat Explanation")

    #Choosing the number of terms
    numTerms = 0
    print("How many terms?")
    while numTerms <= 0:
        numTerms = int(input(">"))
        if numTerms <= 0:
            print("Not a valid number of terms")

    #calculating the sequences
    count = 0
    if chosenSequence == 1:
        prev,prevPrev,current,next = 1,1,1,1
        while count < numTerms:
            if count < 3:
                print(1)
                count += 1
            else:
                next = prevPrev + prev
                prevPrev = prev
                prev = current
                current = next
                print(next)
                count += 1
    elif chosenSequence == 2:
        while count < numTerms:
            print(int((math.factorial(count*2))/(math.factorial(count+1)*math.factorial(count))))
            count += 1
    elif chosenSequence == 3:
        print("Perrin Calculation")
    else:
        print("Fermat Calculation")
    print("Would you like to calculate some more? Y/N")
    choice = input(">")
    if choice == "Y":
        print("Sounds good!")
    elif choice == "N":
        print("Thank you for calculating with us!")
        looping = False
    else:
        print("Unknown input, exiting.")
        looping = False