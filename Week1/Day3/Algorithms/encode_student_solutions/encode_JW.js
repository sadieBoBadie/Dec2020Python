// Solution from John Williams

function encodeStr(str) {
    console.log("\n\noriginal str ->", str);
    if (str.length <= 1) return str;
    var counter = 1;
    var newStr = "";
    for (var i = 0; i < str.length; i++) {
      while (str[i] == str[i + 1]) {
        counter++;
        i++;
      }
      newStr += str[i] + counter;
      counter = 1;
    }
    if (newStr.length == str.length) return str;
    return newStr;
  }