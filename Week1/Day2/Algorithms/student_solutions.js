
const nums1 = [1, 13, 14, 15, 37, 38, 70];
const expected1 = "1, 13-15, 37-38, 70";

// Tiffany's Solution:

function bookIndex1(nums) {
    // create result string
    // loop through nums array
    // if n[i + 1] == n[i] + 1  (next number in array is 1 greater than current element)
    // create range and include dash separator
    // else 
    // add to result

    var resultStr = "";
    for (var i = 0; i < nums.length; i++) {
        if (i == nums.length - 1) {
            resultStr = resultStr + nums[i];
            // console.log('result string here: ', resultStr)
        } else if (nums[i + 1] == nums[i] + 1) {
            resultStr = resultStr + nums[i] + "-";
            // console.log('result string: ', resultStr)
        } else {
            resultStr = resultStr + nums[i] + ", ";
        }

    }
    return resultStr;
}
console.log(bookIndex2(nums1));

// Niharika's solution:

function bookIndex2(nums) {
    var str = ""
    var newStr = ""
    var j = 0
    for (var i = 0; i < nums.length; i++) {
        while (nums[j] + 1 == nums[j + 1]) {
            j++;
        }
        if (i != j) {
            newStr = nums[i] + "-" + nums[j];
            i = j;
        }

        if (str.length == 0 && newStr.length == 0) {
            str = nums[i];
        }
        else if (str.length == 0 && newStr.length != 0) {
            str = newStr
        }
        else if (newStr.length != 0) {
            str += "," + newStr;
        }
        else {
            str += "," + nums[i];
        }
        j++;
        newStr = "";
    }
    return str;
}


console.log(bookIndex2(nums1));