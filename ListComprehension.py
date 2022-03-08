def playlist(artists_song, friends_artists):
    friends_list = []
    for artist in friends_artists:
        for k, v in artists_song.items():
            for songs in v:
                if artist in k:
                    friends_list.append(songs)
    if friends_list:
        friends_list.sort()
        return friends_list

    return "I guess I don't mind ads on the radio that much"


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: ["It's a long way to the top", "Memories", "Payphone", "Sugar", "TNT", "Thunderstruck"]
artists_and_songs = {"Beyonce": ["Halo", "Run the World", "Irreplaceable"], \
                     "Maroon 5": ["Sugar", "Payphone", "Memories"], "Harry Styles": \
                         ["Sign of the Times", "Adore You", "Falling"], "AC/DC": \
                         ["TNT", "It's a long way to the top", "Thunderstruck"]}
friends_artists = ["Maroon 5", "AC/DC", "Tame Impala"]
print(playlist(artists_and_songs, friends_artists))
print()


# convert the above code to a list comprehension:
def playlist(artists_song, friends_artists):
    output = [songs for k, v in artists_song.items() for songs in v for x in friends_artists if x in k ]
    if output:
        output.sort()
        return output

    return "I guess I don't mind ads on the radio that much"


artists_and_songs = {"Beyonce": ["Halo", "Run the World", "Irreplaceable"], \
                     "Maroon 5": ["Sugar", "Payphone", "Memories"], "Harry Styles": \
                         ["Sign of the Times", "Adore You", "Falling"], "AC/DC": \
                         ["TNT", "It's a long way to the top", "Thunderstruck"]}
friends_artists = ["Maroon 5", "AC/DC", "Tame Impala"]
print(playlist(artists_and_songs, friends_artists))
### Mancala game:

if (sum(twoDList[0][1:]) != 0) or (sum(twoDList[1][:-1])) != 0: