// Posted by Emilie Wu from group algos

const str1 = "abcABC";
const expected1 = "abcABC";

const str2 = "hellool";
const expected2 = "helo";

function stringDedupe(str) {
  let newStr = "";
  let temp = {};
  for(let i = str.length-1; i >= 0; i--) {
    for (let c of str) {
        if (!temp[c]) {
            temp[c] = 1;
            newStr += c;
        }
    }
  }
  return newStr;
}
console.log(stringDedupe(str1));
console.log(stringDedupe(str2));