class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def insert(root,key):
    if root is None:
        return Node(key)
    if key<root.val:
        root.left=insert(root.left,key)
    elif key>root.val:
        root.right=insert(root.right,key)
    return root#返回根节点，以便继续进行插入操作
def inorder_traversal(root):
    # 中序遍历二叉树
    if root:
        inorder_traversal(root.left)
        print(root.val, end=' ')
        inorder_traversal(root.right)
root = None
values_to_insert = [4,9,5,11,25,3,12,17,1,32,20,15]

for value in values_to_insert:
    root = insert(root, value)

# 打印二叉排序树的中序遍历结果
print("中序遍历结果：")
inorder_traversal(root)
