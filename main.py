def save(seq):
    file = open('dna.txt', 'w')
    file.write(seq)
    file.close()

def main():
    seq = input("Specify your DNA sequence: ")

    while True:
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Your DNA is:", seq)
        print("1. Save to file")
        print("Q. Exit")

        choice = input()

        if choice == '1':
            save(seq)
        if choice == 'q':
            exit()

main()