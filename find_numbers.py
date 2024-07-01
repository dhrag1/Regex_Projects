import re


# Set variable for text file path
file = 'C:\\Users\\dhruv\\Downloads\\numbers.txt'

# Set "pattern" or keyword for the program to search only digits 
pattern = re.compile(r"\d")

# Open the file
with open(file, 'r') as f:
    
    # Set "file_content" variable to match all text in the text file
    file_content = f.read()

    # Search for all digits put in "matches"     
    matches = pattern.finditer(file_content)
    matches_list = []
    sum = 0

    # Iterate through "matches" and add each match to "matches_list"
    for match in matches:
        matches_list.append(match.group())

    if len(matches_list) <= 200:
        print("Here are all of the digits in your file: ", matches_list)

    # Calculate sum of all matches
    for item in matches_list:
        sum += int(item)

    print("The sum of all of the digits in your file is", sum)

    # Close file
    f.close()
