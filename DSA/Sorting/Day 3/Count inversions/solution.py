

class Solution:
    def inversionCount(self, arr: List[int]) -> int:
        return self.merge_sort(arr, 0, len(arr) - 1)

    def merge_sort(self, arr, left, right):
        if left >= right:
            return 0

        mid = (left + right) // 2

        count = 0
        count += self.merge_sort(arr, left, mid)
        count += self.merge_sort(arr, mid + 1, right)
        count += self.merge(arr, left, mid, right)

        return count

    def merge(self, arr, left, mid, right):
        temp = []
        i, j = left, mid + 1
        count = 0

        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                count += (mid - i + 1)
                j += 1

        while i <= mid:
            temp.append(arr[i])
            i += 1

        while j <= right:
            temp.append(arr[j])
            j += 1

        arr[left:right + 1] = temp
        return count