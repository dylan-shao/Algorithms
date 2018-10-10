// O(log(max(m,n)))
// suppose m > n
// O(log(m+n)) < O(log(2*m)) = O(log(2) + log(m)) < O(2*log(m)) = O(log(m))

class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {

        if(matrix.length ==0 || matrix[0].length ==0) {
            return false;
        }
        int left = 0;
        int right = matrix.length*matrix[0].length - 1;

        while(left<=right) {
            int mid = left + (right-left)/2;
            int row = mid/matrix[0].length;
            int col = mid%matrix[0].length;
            if(matrix[row][col] == target) {
                return true;
            }else if(matrix[row][col] < target) {
                left = mid + 1;
            }else {
                right = mid - 1;
            }
        }

        return false;
    }
}
