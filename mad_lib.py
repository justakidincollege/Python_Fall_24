# Mad lib assignment with functions
# Ask user for inputs
input_adjective=input("Please enter an adjective: ")
input_noun=input("Pleae enter a noun: ")
input_verb=input("Pleae enter a verb: ")
input_noun_2=input("Pleae enter a second noun: ")
input_adjective_2=input("Pleae enter a second adjective: ")
input_noun_3=input("Pleae enter a third noun: ")
input_noun_4=input("Pleae enter a fourth noun: ")
input_adjective_3=input("Pleae enter a third adjective: ")
input_noun_5=input("Pleae enter a fifth noun: ")
input_verb_2=input("Pleae enter a second verb: ")
input_adjective_4=input("Pleae enter a fourth adjective: ")
input_noun_6=input("Pleae enter a sixth noun: ")

# Create function and layout for song
def song(adjective, noun, verb, noun_2, adjective_2, noun_3, noun_4, adjective_3, noun_5, verb_2, adjective_4, noun_6):
    print(f"Twinkle, twinkle {adjective} {noun}")  
    print(f"How I {verb} what you are")
    print(f"Up above the {noun_2} so {adjective_2}")
    print(f"Like a {noun_3} in the {noun_4}")

    print(f"\nTwinkle, twinkle {adjective} {noun} ")
    print(f"How I {verb} what you are")
    print(f"When the {adjective_3} {noun_5} is gone")
    print(f"When he nothing {verb_2} upon")
    print(f"Then you show your {adjective_4} {noun_6}")
    print(f"Twinkle, twinkle all the night")
song(adjective=input_adjective, noun=input_noun, verb=input_verb, noun_2=input_noun_2, adjective_2=input_adjective_2,
     noun_3=input_noun_3, noun_4=input_noun_4, adjective_3=input_adjective_3, noun_5=input_noun_5, verb_2=input_verb_2, 
     adjective_4=input_adjective_4, noun_6=input_noun_6)

