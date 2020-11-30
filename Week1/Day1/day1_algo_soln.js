/* 

Possible topics to explore: 
  1.) Iterating over strings
  2.) Immutability
  3.) while loop example
  4.) (extra) let, const and var

*/
 

/*
  String: Reverse
  Given a string,
  return a new string that is the given string reversed
*/

const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

/**
 * Reverses the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str String to be reversed.
 * @return {string} The given str reversed.
 */
function reverseString(str) {
  let reversedStr = "";
  for (let i = str.length - 1; i >= 0; i--) {
    reversedStr+= str[i];
  }
  return reversedStr;
}

console.log(reverseString(str1), reverseString(str1) == expected1);
console.log(reverseString(str2), reverseString(str2) == expected2);

/*****************************************************************************/

/* case insensitive string compare */

// const strA1 = "ABC";
// const strB1 = "abc";
// const expected1 = true;

// const strA2 = "ABC";
// const strB2 = "abd";
// const expected2 = false;

// const strA3 = "ABC";
// const strB3 = "bc";
// const expected3 = false;

/**
 * Determines whether or not the strings are equal, ignoring case.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} strA
 * @param {string} strB
 * @return {boolean} If the strings are equal or not.
 */
function caseInsensitiveStringCompare(strA, strB) {

  if(strA.length !== strB.length) {
    return false;
  }
  let middle = strA.length/2;
  for (let i = 0, j = strA.length - 1; i < middle; i++, j--) {
    if (strA[i].toUpperCase() !== strB[i].toUpperCase() ||
        strA[j].toUpperCase() !== strB[j].toUpperCase()) {
          return false;
    }
  }
  return true;

}
// console.log(caseInsensitiveStringCompare(strA1, strB1) == expected1);
// console.log(caseInsensitiveStringCompare(strA2, strB2) == expected2);
// console.log(caseInsensitiveStringCompare(strA3, strB3) == expected3);

module.exports = { caseInsensitiveStringCompare };

/*****************************************************************************/

/* 
  Acronyms
  Create a function that, given a string, returns the string’s acronym 
  (first letter of each word capitalized). 
  Do it with .split first if you need to, then try to do it without
*/

// const str1 = " there's no free lunch - gotta pay yer way. ";
// const expected1 = "TNFL-GPYW";

// const str2 = "Live from New York, it's Saturday Night!";
// const expected2 = "LFNYISN";

// const str3 = "              ";
// const expected3 = "";

// const str4 = "LivefromNewYork,it'sSaturdayNight!";
// const expected4 = "L";

// const str5 = "     there's     no free lunch -     gotta pay yer way.    ";
// const expected5 = "TNFL-GPYW";

/**
 * Turns the given str into an acronym.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string to be turned into an acronym.
 * @return {string} The given str converted into an acronym.
 */

// without using .split()
function acronymize(str) {
  
  // Initialize acronym, set tracking for white spaces to 
  // true so it captures the first letter if it is not a space.
  let acronym = "";
  let lastWasSpace = true;

  for (let i = 0; i < str.length; i++) {

    // If the last character was a space and current one is a non-space
    if (str[i] !== " " && lastWasSpace) {
      // Add letter/character to acronym
      acronym+= str[i].toUpperCase();
      lastWasSpace = false;
    }
    else if (str[i] === " "){
      lastWasSpace = true;
    }
  }
  return acronym;
}
// console.log(acronymize(str1), acronymize(str1) == expected1);
// console.log(acronymize(str2), acronymize(str2) == expected2);
// console.log(acronymize(str3), acronymize(str3) == expected3);
// console.log(acronymize(str4), acronymize(str4) == expected4);
// console.log(acronymize(str5), acronymize(str5) == expected1);
/*****************************************************************************/

/* 
  String: Reverse
  Given a string,
  return a new string that is the given string reversed
*/

const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

/**
 * Reverses the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str String to be reversed.
 * @return {string} The given str reversed.
 */
function reverseString(str) {
  let reversedStr = "";
  for (let i = str.length - 1; i >= 0; i--) {
    reversedStr+= str[i];
  }
  return reversedStr;
}

console.log(reverseString(str1), reverseString(str1) == expected1);
console.log(reverseString(str2), reverseString(str2) == expected2);

/*****************************************************************************/