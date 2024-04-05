import re
from collections import Counter

def get_top_ten_words_from_file(file_path: str) -> dict:
    """
        Reads a text file and returns a dictionary containing the top ten most common words in the file.

        Args:
            file_path (str): The path to the text file to be read.

        Returns:
            dict: A dictionary containing the top ten most common words in the file, along with their frequencies.

        Example:
            Given a text file named 'sample.txt' with the following content:
            "The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog."

            >>> get_top_ten_words_from_file('sample.txt')
            {'the': 4, 'quick': 2, 'brown': 2, 'fox': 2, 'jumps': 2, 'over': 2, 'lazy': 2, 'dog': 2}
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()
    return dict(Counter(words).most_common(10))

def main():

    ...

if __name__ == "__main__":
    main()