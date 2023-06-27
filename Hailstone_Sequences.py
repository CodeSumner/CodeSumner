
# https://codeinplace.stanford.edu/cip3/share/hdOWW4yItcEmahPPjnA6
def main():
    number = int(input("Enter a interger number: "))
    print_hailstone_sequences(number)
    
def print_hailstone_sequences(number):
    hailstone_sequences = []
    while number > 1:
        number = next_number(number)
        hailstone_sequences.append(number)
    print(hailstone_sequences)
    
def next_number(number):
    if number == 1:
        return 0
    elif number % 2 == 0:
        return number/2
    else:
        return 3*number + 1
    
        

if __name__ == "__main__":
    main()