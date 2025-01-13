# Function to count lines and words in a file
def count_lines_and_words(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
        return num_lines, num_words
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        return None, None

# Specify the file path
file_path = 'c://users/RAMADAN/Documents/python day 8.rtf'

# Get the line and word counts
lines, words = count_lines_and_words(file_path)

# Print the results
if lines is not None and words is not None:
    print(f"The file {file_path} has {lines} lines and {words} words.")