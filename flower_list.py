# Flower List Manager Assignment
# Create main function
def main():
    flower_list=[]
    flower=""
    print("Hello I am a flower list manager.\nPlease enter the names of flowers.\nType done when finished.")
    while flower!="done":
        flower=input("Please enter a flower name: ")
        if flower=="done":
            break
        flower_list.append(flower)
    flower_list.sort()
    number=0
    new_list=[]
    for char in flower_list:
        new=(f"{number} {char}")
        number+=1
        new_list.append(new)
    print(new_list)
    
    print("You may now type a number to search for the corresponding flower.\nAgain type done when finished")
    search=""
    while search!="done":
        try:
            search=(input("Please enter the flowers corresponding number: "))
            if search=="done":
                break
            search=int(search)
            result=new_list[search]
            print(result)
        except ValueError:
            print("Please input the flowers corresponding number.")
        except IndexError:
            print("That item is not in the list.")
        except:
            print("Oops something went wrong :(\nPlease try again")
    
main()