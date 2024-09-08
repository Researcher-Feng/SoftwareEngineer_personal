from src.get_tokenize import index_token

# 测试
def test_index_token():
    # 定义一个标记列表（token_list）和词表（vocab_index）
    token_list = ["hello", "world", "hello", "again"]
    vocab_index = {"hello": 0, "world": 1, "again": 2}
    # 定义一个预期结果列表（expected_result）
    expected_result = [0, 1, 0, 2]
    # 使用index_token函数将标记列表转换为整数列表
    result = index_token(token_list, vocab_index)
    # 断言结果是否与预期结果匹配
    assert result == expected_result

def test_index_token_with_unk():
    # 定义一个标记列表（token_list）和词表（vocab_index）
    token_list = ["hello", "world", "unk"]
    vocab_index = {"hello": 0, "world": 1}
    # 定义一个预期结果列表（expected_result）
    expected_result = [0, 1, 2]
    # 使用index_token函数将标记列表转换为整数列表
    result = index_token(token_list, vocab_index)
    # 断言结果是否与预期结果匹配
    assert result == expected_result

def test_index_token_with_duplicate_words():
    # 定义一个标记列表（token_list）和词表（vocab_index）
    token_list = ["hello", "hello", "world"]
    vocab_index = {"hello": 0, "world": 1}
    # 定义一个预期结果列表（expected_result）
    expected_result = [0, 0, 1]
    # 使用index_token函数将标记列表转换为整数列表
    result = index_token(token_list, vocab_index)
    # 断言结果是否与预期结果匹配
    assert result == expected_result