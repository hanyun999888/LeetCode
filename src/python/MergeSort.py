# coding: utf-8

def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    num = int( len(lists)/2 )
    # 从中间，进行数据的拆分, 递归的返回数据进行迭代排序
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    print left
    print "*"*20
    print right
    print "_"*20
    return merge(left, right)

def merge(left,right):
    r, l=0, 0
    result=[]
    while l<len(left) and r<len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    print 'result:', result
    return result

if __name__ == "__main__":
    print merge_sort([1, 2, 3, 4, 5, 6, 7, 90, 21, 23, 45])