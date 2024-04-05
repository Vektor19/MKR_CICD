import re
from collections import Counter

def get_top_ten_words_from_file(file_path: str) -> dict:
    """
        Reads a text file and returns a dictionary containing the top ten most common words in the file.

        Args:
            file_path (str): The path to the text file to be read.

        Returns:
            dict: A dictionary containing the top ten most common words in the file, along with their frequencies.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()
    return dict(Counter(words).most_common(10))

def write_top_words_to_file(most_common_words: dict, output_file: str):
    """
        Writes the most common words and their frequencies to a text file.

        Args:
            most_common_words (dict): A dictionary containing the most common words and their frequencies.
            output_file (str): The path to the output text file where the data will be written.

        Returns:
            None
    """
    with open(output_file, 'w', encoding='utf-8') as file:
        for word, count in most_common_words.items():
            file.write(f"{word}-{count}\n")
def main():
    input_file_path = 'input.txt'
    output_file_path = 'output.txt'

    most_common_words = get_top_ten_words_from_file(input_file_path)

    write_top_words_to_file(most_common_words, output_file_path)

    print(f"Top 10 words written in {output_file_path}")

if __name__ == "__main__":
    main()