# Spotify playlist example

playlist = {
    "Title": "Tough times",
    "Author": "Richard",
    "Songs": [
        {"title": "Heard 'Em Say'", "artists": ["Kaney West", "Adam Levine"], "duration": 3.23},
        {"title": "Just Give Me a Reason", "artists": ["P!ink", "Nate Ruess"], "duration": 4.02},
        {"title": "HeadLights", "artists": ["Eminem", "Nate Ruess"], "duration": 5.43},
        {"title": "Rose Golden", "artists": ["Kid Cudi", "Willow"], "duration": 4.37}
    ]
}


for song in playlist["Songs"]:
    print(song["title"])

total_duration = 0
for song in playlist["Songs"]:
    total_duration += song["duration"]
print(total_duration)
