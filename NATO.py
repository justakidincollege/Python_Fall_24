# NATO phonetic alphabet dictionaryy assignment
# Create dictionary with NATO phonetic alphabet
nato_alphabet={"A":"Alpha","B":"Bravo","C":"Charlie","D":"Delta","E":"Echo","F":"Foxtrot","G":"Golf","H":"Hotel","I":"India","J":"Juliette","K":"Kilo","L":"Lima","M":"Mike",
               "N":"November","O":"Oscar","P":"Papa","Q":"Quebec","R":"Romeo","S":"Sierra","T":"Tango","U":"Uniform","V":"Victor","W":"Whiskey","X":"X-ray","Y":"Yankee","Z":"Zulu"}

# Define function to ask user for input and match letters in input with NATO alphabet\
def compare():
    user_name=input("Hello user give me a name and I will tell you howto spell it in the NATO phonetic alphabet: ")
    upper_user_name=user_name.upper()
    for letter in upper_user_name:
        if letter in nato_alphabet:
            print(nato_alphabet[letter])

# Define main function
def main():
    compare()

# Call main function
main()