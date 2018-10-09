/**
 * @param {string} s1
 * @param {string} s2
 * @param {string} s3
 * @return {boolean}
 */

// dp
var isInterleave = function(s1, s2, s3) {
    // init the dp array to memory infomation
    if(s1.length+s2.length !== s3.length) {
        return false;
    }
    const dp = [];
    for (let i=0;i<s1.length+1;i++){
        dp.push(new Array(s2.length+1));
    }
    dp.forEach(item=>item.fill(false));

    for (let i=0;i<s1.length+1;i++){
        for (let j=0;j<s2.length+1;j++){
            if (i===0 && j===0){
                dp[0][0] = true;
            }else if(i === 0 && j > 0) {
                dp[i][j] = dp[i][j-1] && s2[j-1] === s3[j-1];
            }else if (j === 0 && i > 0) {
                dp[i][j] = dp[i-1][j] && s1[i-1] === s3[i-1];
            }else {
                dp[i][j] = dp[i][j-1] && s2[j-1] === s3[i+j-1] || dp[i-1][j] && s1[i-1] === s3[i+j-1];
            }
        }
    }
    return dp[s1.length][s2.length];

};

// dfs
var isInterleave = function(s1, s2, s3) {
    return helper(s1, s2, s3);

    function helper(s1, s2, s3) {
        if(s3.length === 1) {
            return s3 === s1 + s2 || s3 === s2 + s1;
        }
        if(s1.length === 0) {
            return s2 === s3;
        }
        if(s2.length === 0) {
            return s1 === s3;
        }
        const left = s1.slice(-1) === s3.slice(-1) && helper(s1.slice(0,-1), s2, s3.slice(0,-1));
        const right = s2.slice(-1) === s3.slice(-1) && helper(s1, s2.slice(0,-1), s3.slice(0,-1));
        return left || right;
    }

};
