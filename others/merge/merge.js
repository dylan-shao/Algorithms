// 题目
// 数轴上有若干区间，每个区间由起始点（start）、结束点（end）两个属性组成
// 当两个区间重叠或者相邻的时候，我们认为这两个区间是可以合并的（可以合并成一个）
// 现在给定若干区间，写一个函数执行合并过程，要求合并后的结果是最简的
//
// 例子
// [{ start: 1, end: 3 }, { start: 2, end: 6 }, { start: 4, end: 5 }, { start: 8, end: 10 }], 无序
// 经过合并后将变为 [{ start: 1, end: 6 }, { start: 8, end: 10 }]


// complexity O(nlog(n)): O(nlog(n)) for sort, and O(n) for the double for loop
function merge(ranges) {
  if(ranges.length <= 1) {
    return ranges;
  }
  const res = [];
  ranges.sort((a,b) => a.start - b.start);

  for ({start,end} of ranges) {
      if(res.length === 0 || res[res.length-1][1] < start) {
          res.push([start,end]);
      }else {
          res[res.length-1][1] = Math.max(end, res[res.length-1][1]);
      }
  }

  return res;
}

// more complex one
function merge(ranges) {
  if(ranges.length <= 1) {
    return ranges;
  }
  const res = [];
  ranges.sort((a,b) => a.start - b.start);

  for(let i=0;i<ranges.length-1;) {
    const start = ranges[i].start;
    let end = ranges[i].end;

    for(let j=i+1;j<ranges.length;j++) {
      if(ranges[j].start > end) {
        res.push({start, end:Math.max(end, ranges[j-1].end)});
        i = j;
        if(j === ranges.length - 1) {
          res.push({start:ranges[j].start, end:ranges[j].end});
        }
        break;

      }
      end = Math.max(end, ranges[j].end);
      if(j === ranges.length - 1) {
        res.push({start, end});
        i = j;
      }
    }
  }

  return res;
}
