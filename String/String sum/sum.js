function sum(str1, str2) {
  if (!str1 || !str2) {
    // log errror
    return;
  }
  let extra = 0;
  let res = [];
  //123, 1234
  const [str1List, str2List] = constructString(str1, str2);
  // 3210, 4321
  console.log(str1List, str2List)
  str1List.forEach((char, index) => {
    const tmpSum = (+char) + (+str2List[index]) + (+extra);
    const number = (+tmpSum) % 10;
    extra = Math.floor((+tmpSum) / 10);
    console.log(tmpSum, number, extra, res)
    res.push(number);
  });
  // 7531
  // 1357
  return res.reverse().join('');
}

function constructString(str1, str2) {
  const lengthDiff = str1.length - str2.length;

  if (lengthDiff > 0) {
    str2 = '0'.repeat(lengthDiff) + str2;
  }
  if (lengthDiff < 0) {
    str1 = '0'.repeat(-lengthDiff) + str1;
  }
  console.log(str2, str1)
  return [str1.split('').reverse(), str2.split('').reverse()];
}