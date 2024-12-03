# Genearting Word Combinations assignment
# Create generator function
def two_letter_combinations(char_list):
     for i in range(len(char_list)):
        for j in range(len(char_list)):
            # Combine both letters with yield funciton
            yield char_list[i] + char_list[j]
        
if __name__=="__main__":
    characters = ['t', 's', 'i', 'e', 'n']

print("Two-letter combinations")
# Call generator function to run trough each possibility
for combination in two_letter_combinations(characters):
    print(combination)