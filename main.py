import json
import os

# Get the full path to the JSON file
current_directory = os.path.dirname(os.path.realpath(__file__))
json_file_path = os.path.join(current_directory, 'Quran.json')

# Check if the file exists before opening it
if os.path.exists(json_file_path):
    # Load the JSON data from the file
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
else:
    print("Error: Quran.json file not found in the directory.")
    exit(1)  # Exit the script if the file is not found

# Function to retrieve verse text based on chapter and verse number
def get_verse(chapter, verse):
    if verse == 0:
        return '\n'.join([item['text'] for item in data[str(chapter)]])
    else:
        for item in data[str(chapter)]:
            if item['verse'] == verse:
                return item['text']
        return None

# Main function to interactively select chapter and verse
def main():
    while True:
        chapter = int(input("Enter chapter number (or -1 to exit): "))
        if chapter == -1:
            break
        if str(chapter) not in data:
            print("Invalid chapter number. Please try again.")
            continue
        
        verse = int(input(f"Enter verse number for chapter {chapter} (or 0 for the whole chapter): "))
        verse_text = get_verse(chapter, verse)
        if verse_text:
            print(f"Chapter {chapter}, Verse {verse}:")
            print(verse_text)
        else:
            print(f"Verse {verse} not found in chapter {chapter}. Please try again.")

if __name__ == "__main__":
    main()
