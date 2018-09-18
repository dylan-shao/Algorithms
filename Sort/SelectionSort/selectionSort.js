function selectionSort(a) {
  if (!Array.isArray(a) || a.length < 1) {
    return a;
  }

  for (let i = 0; i < a.length; i++) {
    let globalMinIndex = i;
    for (let j = i + 1; j < a.length; j++) {
      if (a[j] < a[globalMinIndex]) {
        globalMinIndex = j;
      }
    }
    globalMinIndex !== i && swap(a, globalMinIndex, i);
  }

  return a;

  function swap(arr, i, j) {
    let temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
  }
}
