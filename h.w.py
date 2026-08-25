class art:
    def __init__(self, welcome, artist, year):
        self.welcome = welcome
        self.artist = artist
        self.year = year
        self.artworks = []
        print(f"\nwelcome user to {self.welcome} art gallery")
        print(f"artist: {self.artist}")
        print(f"year: {self.year}")
        print("====check your art collection====")
    def add_artwork(self, artwork):
        self.artworks.append(artwork)
        print(f"'{artwork}' has been added to the art collection.")
    def remove_artwork(self, artwork):
        self.artworks.remove(artwork) 
        print(f"'{artwork}' has been removed from the art collection.")
    def display_artworks(self):
        self.artworks.sort()
        print("Art collection:")
        for artwork in self.artworks:
            print(f"  - {artwork}")
    def exit_gallery(self):
        print("Thank you for visiting the art gallery. Goodbye!")
    def del_art(self):
        del self.artworks
        print("Art collection has been deleted.")

images = art("Welcome to the Art Gallery", "John Doe", 2023)
while True:
    print("\nOptions:")
    print("1. Add artwork")
    print("2. Remove artwork")
    print("3. Display artworks")
    print("4. Exit gallery")
    print("5. Delete art collection")
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        artwork = input("Enter the name of the artwork to add: ")
        images.add_artwork(artwork)
    elif choice == "2":
        artwork = input("Enter the name of the artwork to remove: ")
        images.remove_artwork(artwork)
    elif choice == "3":
        images.display_artworks()
    elif choice == "4":
        images.exit_gallery()
        break
    elif choice == "5":
        images.del_art()
    else:
        print("====ERROR====.")
