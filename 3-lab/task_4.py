class Solution(object):

    def arrayPairSum(self, list_n):
        def quick_sort(a):
            if len(a) <= 1:
                return a
            else:
                pivot = a.pop()
            lower = [x for x in a if x < pivot]
            higher = [x for x in a if x >= pivot]
            return quick_sort(lower) + [pivot] + quick_sort(higher)

        list_n = quick_sort(list_n)
        res = 0
        for i in range(0, len(list_n), 2):
            res += min(list_n[i], list_n[i + 1])
        return res
