#!/usr/bin/env python3
"""
Movie Catalog Application
Browse movies by genre
"""

# Movie database organized by genre
MOVIES = {
    "Action": [
        "The Matrix",
        "Die Hard",
        "Mission: Impossible",
        "John Wick",
        "Top Gun",
        "Fast & Furious",
        "Avengers: Endgame"
    ],
    "Comedy": [
        "The Grand Budapest Hotel",
        "Superbad",
        "Bridesmaids",
        "Anchorman",
        "The Hangover",
        "Ghostbusters",
        "Knives Out"
    ],
    "Drama": [
        "The Shawshank Redemption",
        "Forrest Gump",
        "The Godfather",
        "Schindler's List",
        "Pulp Fiction",
        "Moonlight",
        "The Social Network"
    ],
    "Horror": [
        "The Ring",
        "Hereditary",
        "Get Out",
        "A Quiet Place",
        "The Exorcist",
        "Halloween",
        "Insidious"
    ],
    "Romance": [
        "The Notebook",
        "Titanic",
        "La La Land",
        "Pride and Prejudice",
        "Eternal Sunshine of the Spotless Mind",
        "Crazy, Stupid, Love",
        "Before Sunrise"
    ],
    "Sci-Fi": [
        "Inception",
        "Interstellar",
        "Blade Runner 2049",
        "The Martian",
        "Dune",
        "Tenet",
        "Ex Machina"
    ],
    "Thriller": [
        "Psycho",
        "Se7en",
        "Zodiac",
        "Gone Girl",
        "Parasite",
        "The Silence of the Lambs",
        "No Country for Old Men"
    ],
    "Animation": [
        "Spirited Away",
        "Coco",
        "Frozen",
        "Toy Story",
        "The Lion King",
        "Zootopia",
        "Incredibles 2"
    ]
}


def display_genres():
    """Display all available genres"""
    print("\n" + "="*50)
    print("AVAILABLE GENRES")
    print("="*50)
    for idx, genre in enumerate(sorted(MOVIES.keys()), 1):
        print(f"{idx}. {genre}")
    print("="*50)


def display_movies(genre):
    """Display movies for a given genre"""
    if genre not in MOVIES:
        print(f"\n❌ Genre '{genre}' not found!")
        return False
    
    movies = MOVIES[genre]
    print(f"\n{'='*50}")
    print(f"📽️  {genre.upper()} MOVIES ({len(movies)} films)")
    print(f"{'='*50}")
    for idx, movie in enumerate(movies, 1):
        print(f"{idx:2}. {movie}")
    print(f"{'='*50}\n")
    return True


def main():
    """Main application loop"""
    print("\n")
    print("╔════════════════════════════════════════════════╗")
    print("║         🎬 MOVIE CATALOG 🎬                    ║")
    print("╚════════════════════════════════════════════════╝")
    
    while True:
        display_genres()
        
        user_input = input("\nEnter a genre (or 'q' to quit): ").strip().title()
        
        if user_input.lower() == 'q':
            print("\n👋 Thanks for using Movie Catalog! Goodbye!")
            break
        
        # Try to match the genre (case-insensitive)
        matched_genre = None
        for genre in MOVIES.keys():
            if genre.lower() == user_input.lower():
                matched_genre = genre
                break
        
        if matched_genre:
            display_movies(matched_genre)
        else:
            print(f"\n❌ '{user_input}' is not a valid genre. Please try again.\n")


if __name__ == "__main__":
    main()
