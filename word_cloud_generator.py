import random
from collections import Counter

import matplotlib.pyplot as plt
from wordcloud import WordCloud


def generate_word_cloud(words, output_file="wordcloud.png"):
    """
    生成词云图
    :param words: 词语列表
    :param output_file: 输出文件名
    """
    # 将词语列表转换为词频字典
    word_freq = Counter(words)

    # 创建自定义颜色函数，设置不同深浅的橘色
    def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
        # 生成随机的橘色深浅
        # 保持红色分量较高，绿色分量中等，蓝色分量较低，以产生橘色
        r = 255  # 红色保持最大
        g = random.randint(100, 180)  # 绿色随机变化
        b = random.randint(0, 50)  # 蓝色保持较低
        # 返回 RGB 格式的颜色（整数值）
        return f"rgb({r}, {g}, {b})"

    # 创建词云对象
    wc = WordCloud(
        font_path="STZHONGS.TTF",  # 使用华文中宋字体
        width=800,
        height=400,
        background_color="white",
        color_func=color_func,
        random_state=42,  # 设置随机种子以保证可重复性
        prefer_horizontal=0.7,  # 70% 的词语水平显示
        max_words=100,
    )

    # 生成词云
    wc.generate_from_frequencies(word_freq)

    # 显示词云图
    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")

    # 保存图片
    wc.to_file(output_file)

    # 显示图片
    plt.show()


# 测试代码
if __name__ == "__main__":
    # 示例词语列表
    test_words = [
        "黑天鹅",
        "落叶",
        "夕阳",
        "图书馆",
        "黑天鹅",
        "落叶",
        "春天",
        "秋天",
        "冬天",
        "夏天",
        "阳光",
        "月光",
        "星星",
        "海洋",
        "山川",
        "河流",
        "森林",
        "花朵",
    ]

    # 生成词云
    generate_word_cloud(test_words)
