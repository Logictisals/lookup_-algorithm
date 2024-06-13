import re
from collections import defaultdict


class TreeNode:
    def __init__(self, key, words):
        self.left = None
        self.right = None
        self.val = key
        self.words = words  # 存储具有相同出现次数的所有单词


def insert(root, key, word):
    if root is None:
        return TreeNode(key, [word])

    if key < root.val:
        if root.left is None:
            root.left = TreeNode(key, [word])
        else:
            insert(root.left, key, word)
    elif key > root.val:
        if root.right is None:
            root.right = TreeNode(key, [word])
        else:
            insert(root.right, key, word)
    else:
        # 如果出现次数相同，则添加到链表中
        root.words.append(word)


def find_words_by_count(root, count):
    if root is None or root.val != count:
        return []

    return root.words


def create_bst_from_word_counts(word_counts):
    root = None
    for word, count in word_counts.items():
        insert(root, count, word)
    return root


def count_words_in_article(article):
    word_counts = defaultdict(int)
    words = re.findall(r'\b\w+\b', article.lower())
    for word in words:
        word_counts[word] += 1
    return word_counts


# 示例文章
article = """
Your article text goes here. Make sure to include a variety of words with different frequencies.
"""

# 统计单词出现次数
word_counts = count_words_in_article(article)

# 创建二叉排序树
bst = create_bst_from_word_counts(word_counts)

# 查找特定出现次数的单词
counts_to_check = [3, 8, 16]
for count in counts_to_check:
    words = find_words_by_count(bst, count)
    print(f"Words appearing {count} times: {', '.join(words) if words else 'None'}")
