class Solution {

    public int inversionCount(int[] arr) {
        return mergeSort(arr, 0, arr.length - 1);
    }

    private int mergeSort(int[] arr, int left, int right) {
        if (left >= right) {
            return 0;
        }

        int mid = left + (right - left) / 2;

        int count = 0;
        count += mergeSort(arr, left, mid);
        count += mergeSort(arr, mid + 1, right);
        count += merge(arr, left, mid, right);

        return count;
    }

    private int merge(int[] arr, int left, int mid, int right) {

        int[] temp = new int[right - left + 1];

        int i = left;
        int j = mid + 1;
        int k = 0;
        int count = 0;

        while (i <= mid && j <= right) {
            if (arr[i] <= arr[j]) {
                temp[k++] = arr[i++];
            } else {
                temp[k++] = arr[j++];
                count += (mid - i + 1);
            }
        }

        while (i <= mid) {
            temp[k++] = arr[i++];
        }

        while (j <= right) {
            temp[k++] = arr[j++];
        }

        for (int idx = 0; idx < temp.length; idx++) {
            arr[left + idx] = temp[idx];
        }

        return count;
    }
}