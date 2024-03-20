def load_pinyin_mapping(filename):
    """
    加载拼音到汉字的映射。
    参数:
    - filename: 包含拼音和汉字映射的数据文件名。
    
    返回值:
    - 一个字典，键为汉字，值为对应的拼音。
    """
    pinyin_mapping = {}
    with open(filename, "r", encoding="gbk") as file:
        for line in file:
            parts = line.strip().split()
            pinyin = parts[0]
            characters = parts[1:]
            for char in characters:
                pinyin_mapping[char] = pinyin
    return pinyin_mapping

def lazy_pinyin(chars, mapping = load_pinyin_mapping('./resource/拼音汉字表.txt')):
    """
    根据输入的汉字列表返回对应的拼音列表。
    参数:
    - chars: 字符串，输入的汉字序列。
    - mapping: 汉字到拼音的映射字典。
    
    返回值:
    - 一个拼音列表，每个元素对应输入汉字序列中的一个汉字。
    """
    return [mapping.get(char, "UNKNOWN") for char in chars]

# 使用示例
if __name__ == "__main__":
    # 假设你的数据文件名为 "pinyin_mapping.txt"
    filename = "pinyin_mapping.txt"
    pinyin_mapping = load_pinyin_mapping(filename)
    
    # 输入汉字序列
    chars = "汉字转拼音"
    
    # 获取拼音列表
    pinyin_list = lazy_pinyin(chars, pinyin_mapping)
    
    print(pinyin_list)
