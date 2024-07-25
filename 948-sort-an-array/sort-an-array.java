class Solution {
    public int[] sortArray(int[] nums) {
        // for(int i=0;i<nums.length-1;i++){
        //     for(int j = 0 ; j< nums.length-1-i ; j++){
        //         if(nums[j]>nums[j+1]){
        //             int temp = nums[j];
        //         nums[j] = nums[j+1];
        //         nums[j+1]=temp;
        //         }
        //     }
        // }
        // return nums;
     mergeSort(nums,0,nums.length-1);
    return nums;
    }
    public static void mergeSort(int[] nums,int l,int h){
        if(l>=h){
            return;
        }

        int mid = (l+h)/2;
        mergeSort(nums,l,mid);
        mergeSort(nums,mid+1,h);
        merge(nums,l,mid,h);
    }

    public static void merge(int[] nums,int l,int mid,int h){
        int[] mergedArr = new int[h-l+1];
        int i = l;
        int j = mid +1;
        int k = 0;
        while(i<=mid && j<=h){
            if(nums[i]>nums[j]){
                mergedArr[k]=nums[j];
                j++;
            }
            else{
                mergedArr[k]=nums[i];
                i++;
            }
            k++;
        }

        while(i<=mid){
            mergedArr[k]=nums[i];
            i++;
            k++;
        }
        while(j<=h){
            mergedArr[k]=nums[j];
            j++;
            k++;
        }
        for(int a=0; a<mergedArr.length;a++){
            nums[a+l]=mergedArr[a];
        }
    }
}
