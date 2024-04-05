import os
import pytest

@pytest.fixture(autouse=True)
def prepare_text_file(tmp_path):
    target_file = os.path.join(tmp_path, 'test.txt')
    with open(target_file, 'w') as file:
        test_sentence="The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog."
        file.writelines(test_sentence)
    return target_file