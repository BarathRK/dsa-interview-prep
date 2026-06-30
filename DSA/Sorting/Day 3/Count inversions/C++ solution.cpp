class Solution {
public:
    int inversionCount(vector<int> &arr) {
        return mergeSort(arr, 0, arr.size() - 1);
    }

private:
    int mergeSort(vector<int> &arr, int left, int right) {
        if (left >= right)
            return 0;

        int mid = left + (right - left) / 2;

        int count = 0;
        count += mergeSort(arr, left, mid);
        count += mergeSort(arr, mid + 1, right);
        count += merge(arr, left, mid, right);

        return count;
    }

    int merge(vector<int> &arr, int left, int mid, int right) {

        vector<int> temp;

        int i = left;
        int j = mid + 1;
        int count = 0;

        while (i <= mid && j <= right) {
            if (arr[i] <= arr[j]) {
                temp.push_back(arr[i++]);
            } else {
                temp.push_back(arr[j++]);
                count += (mid - i + 1);
            }
        }

        while (i <= mid) {
            temp.push_back(arr[i++]);
        }

        while (j <= right) {
            temp.push_back(arr[j++]);
        }

        for (int k = 0; k < temp.size(); k++) {
            arr[left + k] = temp[k];
        }

        return count;
    }
};