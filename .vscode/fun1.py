artist = ["artist1", "artist2", "artist3"]

a = open("a.txt").read()
songs = a.split("\n")

result= tuple(zip(songs, artist))

result.join("\n")