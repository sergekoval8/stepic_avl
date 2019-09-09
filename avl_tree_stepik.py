import sys


def visit_pre_order(d, v):
    print(d[v]['val'], end=" ")
    if d[v]['left'] != -1:
        visit_pre_order(d, d[v]['left'])
    if d[v]['right'] != -1:
        visit_pre_order(d, d[v]['right'])
    return


def visit_post_order(d, v):
    if d[v]['left'] != -1:
        visit_post_order(d, d[v]['left'])
    if d[v]['right'] != -1:
        visit_post_order(d, d[v]['right'])
    print(d[v]['val'], end=" ")
    return


def visit_in_order(d, v, res):
    if d[v]['left'] is not None:
        visit_in_order(d, d[v]['left'], res)
    res. append(d[v]['val'])
    if d[v]['right'] is not None:
        visit_in_order(d, d[v]['right'], res)
    return

def avl_tree():
    n = int(input())
    sys.setrecursionlimit(2000)
    res, flag = [], 1
    d = {i: {'left': None, 'right': None, 'val': None} for i in range(n)}
    for key in range(n):
        val, left, right = tuple(map(int, sys.stdin.readline().split()))
        d[key]['left'], d[key]['right'], d[key]['val'] =left if left !=-1 else None, right if right != -1 else None, val
    visit_in_order(d, 0, res)
    for i in range(n-1):
        if res[i]>=res[i+1]:
            flag=0
    print ('CORRECT' if flag else 'INCORRECT')



if __name__ == "__main__"
    avl_tree()