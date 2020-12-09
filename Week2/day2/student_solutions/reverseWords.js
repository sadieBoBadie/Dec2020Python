// Posted by Michael Towson from group algos
const str1 = "hello";
const expected1 = "olleh";

const str2 = "hello world";
const expected2 = "olleh dlrow";

const str3 = "abc def ghi";
const expected3 = "cba fed ihg";

function reverseWords1(str) {
    var word = "";
    var reversedWord = "";
    var newString = "";
    
    for(let i=0;i<=str.length;i++){
      if(str[i]==" " || i == str.length){
        for(let y=word.length-1; y>=0; y--){
          reversedWord += word[y]
        }
        newString += reversedWord+" "
        word = "" //reset word
        reversedWord = "" //reset reversedWord
  
      }
      else{
        word += str[i]
      }
    }
    return newString
  }
  console.log(reverseWords1("The cat jumped over the fence"));
  console.log(reverseWords1(str1));
  console.log(reverseWords1(str2));
  console.log(reverseWords1(str3));

  // NOTE: This solution adds a space at the end. This could be elliminated 
  // if we changed line 11 to just be "newString += reversedWord" and added 
  // another "if" check to also concatenate "" into newString assuming that 
  // we haven't reached the end of the str. But there is probably a better way. :)

/////////////////////////////////////////////////////////////////////////////////////

  // Below solution posted by Emilie Wu.

function reverseWords2(str) {
  var newStr = "";
  var idx = 0;
  var place = 1;
  var space = " ";
  for(let i = 0; i < str.length; i++) {
    if(i === str.length -1) {
      place = 0;
      space = "";
    }
    if(str[i] == " "|| i === str.length-1) {
      for(let j = i-place; j >= idx; j--) {
        newStr += str[j];
      }
      newStr += space;
      idx = i+1;
    }
  }
  return newStr;
}
console.log(reverseWords2(str1));
console.log(reverseWords2(str2));
console.log(reverseWords2(str3));