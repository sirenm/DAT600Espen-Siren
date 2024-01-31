#ref: https://www.geeksforgeeks.org/python-program-for-merge-sort/
#Merged the merge functions and added steps, such that we can use a singular input of arr
def merge_sort(arr):
    def merge(arr, l, m, r, steps):
        n1 = m - l + 1
        n2 = r - m

        L = [0] * n1
        R = [0] * n2

        for i in range(n1):
            L[i] = arr[l + i]
            steps += 1

        for j in range(n2):
            R[j] = arr[m + 1 + j]
            steps += 1

        i, j, k = 0, 0, l

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            steps += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
            steps += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
            steps += 1

        return steps

    def sort(arr, l, r, steps=0):
        if l < r:
            m = l + (r - l) // 2

            steps = sort(arr, l, m, steps)
            steps = sort(arr, m + 1, r, steps)
            steps = merge(arr, l, m, r, steps)

        return steps

    return sort(arr, 0, len(arr) - 1)


 