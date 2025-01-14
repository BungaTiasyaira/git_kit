def save(seq):
    file = open('dna.txt', 'w')
    file.write(seq)
    file.close()

from operations import inverse, complement

def main():
    seq = input("Specify your DNA sequence: ")

    while True:
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Your DNA is:", seq)
        print("1. Save to file")
        print("2. Calculate the inverse")
        print("3. Find the complement")
        print("Q. Exit")

        choice = input()

        if choice == '1':
            save(seq)
        elif choice == '2':
            seq = inverse(seq)
        elif choice == '3':
            seq = complement(seq)
        if choice == 'q':
            exit()

main()