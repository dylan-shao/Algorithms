### regarding when to use left < right - 1, or left < right, or left <= right:

#### left < right - 1, break out if left neighbor to right, use when you want check both left and right later

#### left < right, break out when left == right,

#### left <= right, break out after executation of while loop when left == right,if you using left or right after, don't use this, as it may out of index otherwise, use it so you don't need to check left, right afterward
