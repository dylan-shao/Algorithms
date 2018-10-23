function quickSort(arr) {
  const n = arr.length;
  if(n===0) {
    return arr;
  }

  let low = 0;
  let high = n - 1;

  _helper(arr, low, high);

  return arr;

  function _helper(arr,low,high) {
    if(low < high) {
      // let pivot = _partition(arr, low, high);
      // _helper(arr, low, pivot-1);
      // _helper(arr,pivot+1,high);

      let pivot = _partition2(arr, low, high);
      _helper(arr, low, pivot-1);
      _helper(arr,pivot+1,high);
    }
  }

  function _partition(arr, low, high) {
    const pivot = high;
    high -= 1;
    while(low<=high) {
      // low point to the higher than arr[pivot] index
      while(arr[low]<arr[pivot]) {
        low++;
      }
      // high point to the lower than arr[pivot] index
      while(arr[high] > arr[pivot]) {
        high--;
      }
      if(low<=high) {
        _switch(arr, low, high);
        low ++;
        high --;
      }
    }

    _switch(arr, low, pivot);

    return low;

  }

  function _partition2(arr,low,high) {
      let wall = low;
      const pivot = high;

      for (let i=low;i<high;i++) {
        while(arr[i]>arr[pivot]) {
          i++;
        }
        _switch(arr, wall, i);
        wall ++;
      }

      _switch(arr, wall, pivot);
      return wall;
  }

  function _switch(arr, i,j) {
    const temp = arr[i];
    arr[i]  = arr[j];
    arr[j] = temp;
  }
}
