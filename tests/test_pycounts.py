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
