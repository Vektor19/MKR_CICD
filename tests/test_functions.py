import os
import pytest

from main import get_top_ten_words_from_file,write_top_words_to_file

@pytest.fixture
def prepare_most_common_words():
    return {'the': 4, 'quick': 2, 'brown': 2, 'fox': 2, 'jumps': 2, 'over': 2, 'lazy': 2, 'dog': 2}

def test_get_top_ten_words_from_file(prepare_text_file, prepare_most_common_words):
    result = get_top_ten_words_from_file(prepare_text_file)
    assert result == prepare_most_common_words

def test_write_top_words_to_file(tmp_path, prepare_most_common_words):
    output_file = os.path.join(tmp_path, 'temp_output.txt')
    write_top_words_to_file(prepare_most_common_words, output_file)
    assert os.path.exists(output_file)

    with open(output_file, 'r', encoding='utf-8') as file:
        content = file.read()
        assert content.strip() == "the-4\nquick-2\nbrown-2\nfox-2\njumps-2\nover-2\nlazy-2\ndog-2"

    os.remove(output_file)