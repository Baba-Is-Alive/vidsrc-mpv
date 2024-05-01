import imdb
import subprocess
import requests

def play_movie():
    movie_title = input("\nEnter Movie Title: ")
    ia = imdb.IMDb()
    results = ia.search_movie(movie_title)
    movie = results[0]  # First result
    imdb_url = ia.get_imdbURL(movie)  # IMDb URL for the first result
    api_url = "https://versrc-p6kmgh6md-baba-is-alives-projects.vercel.app/vidsrc/"
    vid_url = imdb_url.replace("https://www.imdb.com/title/", api_url)
    print("Fetching movie info from API...")
    response = requests.get(vid_url).json()
    if response['status'] == 200:
        stream_url = response['sources'][0]['data']['stream']
        subtitle_urls = [sub['file'] for sub in response['sources'][0]['data']['subtitle']]
        print("Playing movie in mpv...")
        subprocess.run(["mpv", stream_url])
        for sub_url in subtitle_urls:
            subprocess.run(["mpv", "--sub-file", sub_url, stream_url])
    else:
        print("Error fetching movie info from API")
def play_series():
    series_title = input("\nEnter Series Title: ")
    ia = imdb.IMDb()
    results = ia.search_movie(series_title)
    series = results[0]  # First result
    imdb_url = ia.get_imdbURL(series)  # IMDb URL for the first result
    season = input("Enter Season (in 01-15 format): ")
    episode = input("Enter Episode (in 01-15 format): ")
    api_url = "https://versrc-p6kmgh6md-baba-is-alives-projects.vercel.app/vidsrc/"
    vid_url = imdb_url.replace("https://www.imdb.com/title/", api_url) + f"?s={season}&e={episode}"
    print("Fetching series info from API...")
    response = requests.get(vid_url).json()
    if response['status'] == 200:
        stream_url = response['sources'][0]['data']['stream']
        subtitle_urls = [sub['file'] for sub in response['sources'][0]['data']['subtitle']]
        print("Playing series in mpv...")
        subprocess.run(["mpv", stream_url])
        for sub_url in subtitle_urls:
            subprocess.run(["mpv", "--sub-file", sub_url, stream_url])
    else:
        print("Error fetching series info from API")

print("\033[1;32m\n                Welcome Baba                     \n")

print("\n[1] Movie \n[2] Series")
decision = int(input("\n>> "))

if decision == 1:
    play_movie()
elif decision == 2:
    play_series()

for _ in range(30):
    print("(r) Reselect")
    print("(q) Quit")
   
    user_input = input(">> ")
    
        
    answer = input('Anything else? (y/n): ')
    if answer == 'n':
        break
    elif answer == 'y':
        print("\n[1] Movie \n[2] Series")
        decision = int(input("\n>> "))
        if decision == 1:
            play_movie()
        elif decision == 2:
            play_series()
    elif user_input == "q":
        break
