import random

artist = (
    "Prime Minister Modi",
    "Sachin Tendulkar",
    "Vicky Kaushal",
    "Katrina Kaif",
    "Sardar Vallabhai Patel"
)

work = (
    "makes a shoe",
    "wins a match",
    "caught up celebrating",
    "wore a suit",
    "moved to gutter",
    "stitching short pants"
)

places = (
    "at Chamkilla Tower",
    "at Eiffel Tower",
    "in the war",
    "inside the bars",
    "at the footpath"
)

while True:
    artists = random.choice(artist)
    works = random.choice(work)
    place = random.choice(places)

    headline = f"Breaking News: {artists} {works} {place}"
    print(headline)

    user_input = input("Do you want to have more news? (y/n): ").strip().lower()
    if user_input == 'n':
        print("Thanks for watching our news!")
        break
