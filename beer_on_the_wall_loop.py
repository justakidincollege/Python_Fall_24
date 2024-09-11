# Bottles of beer on the wall loop assignment

# Establish start total
bottles=99

# Run loop to countdown by one bottle for each loop until it reaches zero
while bottles>1:
    print("",bottles,"bottles of beer on the wall.\n",bottles,"bottles of beer.\n","Take one down, pass it around.")
    bottles -= 1
    if bottles>1:
        print("",bottles,"bottles of beer on the wall!\n")
    elif bottles==1:
        print("",bottles,"bottle of beer on the wall!\n")
# Final bottle of beer on the wall wich requires different wording so we give it its own line of code.
print("",bottles,"bottle of beer on the wall.\n",bottles,"bottle of beer.\n","Take it down, pass it around.\n",
                "No bottles of beer on the wall!")