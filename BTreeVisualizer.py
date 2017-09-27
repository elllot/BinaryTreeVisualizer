from TreeNode import TreeNode

"""
"   Binary Tree Visualizer
"   
"   Prints the full view of a Binary tree given the root node. 
"   
"   1. Calculates the maximum depth of the tree to appropriately
"      size the width of the display tree grid
"
"   2. Recursively fills out the grid using a divide and conquer
"      approach
"
"   This is an O(n) algorithm due to having to process each node
"   of the tree a constant number of times to fully generate the
"   visualization. 
"
"   I believe this could be helpful for those who have trouble 
"   visualizing the B Tree data structure. 
"""

"""
" Helper function for getting the max depth of the tree.
" Max depth is used to generate an appropriately sized grid matrix
" (2D list) 
"""
def get_max_depth(root):
    if not root: return 0
    return max(get_max_depth(root.left), get_max_depth(root.right)) + 1

"""
" Recursive function that fills the predetermined node using a
" divide an conquer approach. Similar to a binary search, the 
" function grabs the mid point, fills the grid with the mid point
" then recursively calls on the left and right partitions divided 
" by the midpoint.
"""
def fill_tree_grid(root, grid, lv, i, j):
    if root:
        m = i + (j-i) // 2 # mid point
        grid[lv][m] = str(root.val); lv += 1 # lv ++
        fill_tree_grid(root.left, grid, lv, i, m-1) # left child
        fill_tree_grid(root.right, grid, lv, m+1, j) # right child

"""
" Grid printer helper function
"
" Prints the grid row by row
"""
def print_grid(grid):
    for r in grid:
        print(r)

"""
" Main function 
"
" As mentioned earlier, grabs the max depth then calls the recursive
" function to fill the grid. 
"""
def visualize(root):

    d = get_max_depth(root)
    width = (1 << d) - 1 # width of printed result
    # generate the grid according to the computed width
    grid = [['' for _ in range(width)] for _ in range(d)] 
    fill_tree_grid(root, grid, 0, 0, width-1)
    
    print_grid(grid)

if __name__ == '__main__':

    # example use

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)

    visualize(root)



