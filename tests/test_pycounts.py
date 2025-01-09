from pycounts import pycounts
from pycounts import count_words
from collections import Counter
import pytest

# 创建一个临时测试文件
@pytest.fixture
def sample_text(tmp_path):
    text_file = tmp_path / "sample.txt"
    text_file.write_text("Beautiful is better than ugly. Explicit is better than implicit.")
    return text_file

# 测试 count_words 功能
def test_count_words(sample_text):
    result = count_words(sample_text)
    assert isinstance(result, Counter), "Result should be a Counter instance"
    assert result["beautiful"] == 1, "'beautiful' should appear once"
    assert result["better"] == 2, "'better' should appear twice"

# 测试空文件的处理
def test_empty_file(tmp_path):
    empty_file = tmp_path / "empty.txt"
    empty_file.write_text("")
    result = count_words(empty_file)
    assert result == Counter(), "Empty file should return an empty Counter"

from pycounts.pycounts import count_words
from collections import Counter

def test_count_words():
    """Test word counting from a file."""
    expected = Counter({'insanity': 1, 'is': 1, 'doing': 1, 
                        'the': 1, 'same': 1, 'thing': 1, 
                        'over': 2, 'and': 2, 'expecting': 1,
                        'different': 1, 'results': 1})
    actual = count_words("tests/einstein.txt")
    assert actual == expected, "Einstein quote counted incorrectly!"