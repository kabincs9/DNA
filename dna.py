import csv
import sys  # acces to system command line argument
# watch video all about dns and understand sequence and how many time they repeat ..
# name, AGAT, AATG, TATC
# Alice, 28,42,14 like aatg for 42 ...
# Bob, 17,22,19 like agat for 17 times repeated   ( csv file have all these data are given and all data like aagat in squence file ) and bigest run of like agat counted (how amy times str repeats)
# Charlie, 36,18,25


def main():  # function

    # TODO: Check for command-line usage

    if len(sys.argv) != 3:  # to check there are exactly three arguments
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)  # stop if not that

    # TODO: Read database file into a variable
    database_file = sys.argv[1]  # to store the first file name
    # open file for reading and with means like like statement automatically close ..
    with open(database_file, "r") as file:
        reader = csv.DictReader(file)  # create a reader that treats csv as a table with headers
        # load all rows into list of the dictionary like [{"name": "Alice", "AGAT": "2"....}]
        database = list(reader)
        # extract STRs ["AGAT",..]by skipping the name coloumn (index 0) as we asked about 1
        str_list = reader.fieldnames[1:]
        # like making list and pattern to look for

    # TODO: Read DNA sequence file into a variable
    sequence_file = sys.argv[2]  # to store second file in sequence.txt
    with open(sequence_file, "r") as file:  # open for reading
        sequence = file.read()  # read entire dna like AGATCAGA...

    # TODO: Find longest match of each STR in DNA sequence
    counts = {}     # create a dictionary to store STR count
    for str in str_list:
        # call longest ... to count the longest run of str in sequence storing in counts[str]
        counts[str] = longest_match(sequence, str)

    # TODO: Check database for matching profiles
    for person in database:
        match = True
        for str in str_list:
            if int(person[str]) != counts[str]:
                match = False
                break

        if match:
            print(person["name"])
            sys.exit(0)

    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
