// Given a collection of boxes. Return the max number of boxes that you can russian doll.
// Each box has (w, h, l).
// Explanation: [1,5,3] fits in [3,9,9] which fits in [5,10,11]
// All the dimensions must be smaller to fit into a larger box -- [1,5,3] does not fit into [3,9,3]

function russianDoll(boxes) {
  if (boxes.length == 0 || boxes.length == 1) {
    return boxes.length;
  }

	boxes = boxes.sort((a, b) => a[0] * a[1] * a[2] - b[0] * b[1] * b[2])
	.map(item => item.sort((a,b) => a - b));
	
	const dp = [];
	boxes.forEach((e, index) => {
		dp[index] = 1;
	});
	let result = 1;
	for (let i = 1; i < boxes.length; i ++) {
		for (let j = 0; j < i; j ++ ) {
			if (boxes[j][0] < boxes[i][0] && boxes[j][1] < boxes[i][1] && boxes[j][2] < boxes[i][2]) {
				dp[i] = Math.max(dp[i], dp[j] + 1);
			}
		}
		result = Math.max(result, dp[i]);
	}

	return result;

}

const boxes = [
	[3,9,9],
	[1,4,10],
	[5,10,11],
	[3,9,3],
	[1,5,3],
	[7, 12, 1]
];

console.log(russianDoll(boxes));