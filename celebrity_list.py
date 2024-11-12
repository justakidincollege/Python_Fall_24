# Celebrity List Asignment
# Enter starting code that creates main function and includes list
def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    artist=""
    index=""
    print("Hello I am a celebrity list updater enter an index from 0-9 and a new artist name and I will replace the old artist.\nType done for artist when finished.")
    while artist!="done":
        try:
            artist=input("Enter the new artist name: ")
            if artist=="done":
                break
            index=int(input("Enter the index of the artist to replace: "))   
            top_artists[index]=artist
            print(top_artists)
        except(IndexError, ValueError):
            print("An input error ocurred")
        
main()
    