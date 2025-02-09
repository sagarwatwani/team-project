import os

def count_languages(repo_path):
    # File extensions we are looking for
    language_extensions = {
        '.py': 'Python',
        '.js': 'JavaScript',
        '.java': 'Java',
        '.html': 'HTML',
        '.css': 'CSS'
    }

    # Dictionary to store file counts for each language
    language_count = {lang: 0 for lang in language_extensions.values()}

    # Loop through the directory and count files by extension
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            ext = os.path.splitext(file)[1].lower()  # Get the file extension
            if ext in language_extensions:
                language = language_extensions[ext]
                language_count[language] += 1

    return language_count

def get_dominant_language(language_count):
    # Find the language with the maximum count
    dominant_language = max(language_count, key=language_count.get)
    return dominant_language

if __name__ == "__main__":
    # Example path to the repository (change this to your local directory)
    repo_path = input("Enter the path to your repository: ")

    # Count files by language
    language_count = count_languages(repo_path)

    # Print out the file counts for each language
    print("\nFile counts by language:")
    for language, count in language_count.items():
        print(f"{language}: {count}")

    # Determine and print the dominant language
    dominant_language = get_dominant_language(language_count)
    print(f"\nThe dominant language in this repository is: {dominant_language}")
