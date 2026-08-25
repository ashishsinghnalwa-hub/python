class playlist:
    def __init__(self,name,genre):
        self.name = name
        self.genre = genre
        self.song = []
    print(playlist
    def add_song(self,song):
        self.song.append(song)
    print("song added",self.name)
    def remove_song(self,song):
        if song in self.song:
            self.song.remove(song)
            print(self,"song removed")
        else:
            print(song,"song nt found in the playlist")
    def display(self):
        print("\n---",self.name,self.genre)