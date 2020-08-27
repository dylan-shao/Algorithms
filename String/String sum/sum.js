function sum(str1, str2) {
  if (!str1 || !str2) {
    // log errror
    return;
  }
  str1 = str1.trim();
  str2 = str2.trim();
  let extra = 0;
  let res = [];
  //-456, 1234
  const negtiveFlag1 = str1[0] === '-';
  const negtiveFlag2 = str2[0] === '-';
  if (negtiveFlag1) {
    str1 = str1.slice(1, str1.length);
  }
  if (negtiveFlag2) {
    str2 = str2.slice(1, str2.length);
  }
  // 大数放前面：
  const [str1List, str2List] = constructStringList(str1, str2);
  // 3210, 4321
  str1List.forEach((char, index) => {
    // 一边为负数的情况
    if (negtiveFlag1 !== negtiveFlag2) {
      let tmpSum;
      if (str1List[index] < str2List[index]) {
         tmpSum = 10 + (+char) - (+str2List[index]) - extra;
         extra = 1;
      } else {
         tmpSum =  (+char) - (+str2List[index]) - extra;
         extra = 0;
      }

      res.push(tmpSum);
    } else {
      // 同为正或负的情况
      const tmpSum = (+char) + (+str2List[index]) + (+extra);
      const number = (+tmpSum) % 10;
      extra = Math.floor((+tmpSum) / 10);
      res.push(number);
    }
  });
  // 7531
  // 1357
  // 一边为负数
  if (negtiveFlag1 !== negtiveFlag2) {
    if (negtiveFlag1 && str1 > str2 || negtiveFlag2 && str2 > str1) {
        return '-' + res.reverse().join('');
    } else {
      return res.reverse().join('');
    }
  }
  // 同为正或负
  return negtiveFlag1 && negtiveFlag2 ?  '-' + res.reverse().join('') : res.reverse().join(''); 
}

function constructStringList(str1, str2) {
  const lengthDiff = str1.length - str2.length;

  if (lengthDiff > 0) {
    str2 = '0'.repeat(lengthDiff) + str2;
  }
  if (lengthDiff < 0) {
    str1 = '0'.repeat(-lengthDiff) + str1;
  }
  // 大数放前面，方便做减法
  if (+str1 > +str2) {
    return [str1.split('').reverse(), str2.split('').reverse()];
  }
  return [str2.split('').reverse(), str1.split('').reverse()];
}