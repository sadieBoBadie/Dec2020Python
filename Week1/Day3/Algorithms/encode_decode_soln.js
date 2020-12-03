/*
    Topics to explore:
        - NaN values
        - isNaN() built-in javascript function
          https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN
        - parseInt() built-in javascript function
          https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt
        - .repeat() - JS string method
          https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/repeat
*/

/* 
  String Encode
  You are given a string that may contain sequences of consecutive characters.
  Create a function to shorten a string by including the character,
  then the number of times it appears consecutively. 
  
  
  If final result is not shorter (such as "bb" => "b2" ),
  return the original string.
  */

//  const str1 = "aaaabbcddd";
//  const expected1 = "a4b2c1d3";
 
//  const str2 = "";
//  const expected2 = "";
 
//  const str3 = "a";
//  const expected3 = "a";
 
//  const str4 = "bbcc";
//  const expected4 = "bbcc";
 
 /**
  * Encodes the given string such that duplicate characters appear once followed
  * by a number representing how many times the char occurs only if the
  * character occurs more than two time.
  * - Time: O(?).
  * - Space: O(?).
  * @param {string} str The string to encode.
  * @return {string} The given string encoded.
  */
 function encodeStr(str) {
    
    let encoded = ""

    for (let i = 0; i < str.length;) {
        
        let currentChar = str[i];
        let count = 0;

        while (str[i] == currentChar) {
            count++;
            i++;
        }
        
        encoded+= currentChar + count;

    }

    return encoded.length < str.length? encoded: str;
 }
//  const result1 = encodeStr(str1);
//  console.log(result1, result1 == expected1);

//  const result2 = encodeStr(str2);
//  console.log(result2, result2 == expected2);

//  const result3 = encodeStr(str3);
//  console.log(result3, result3 == expected3);

//  const result4 = encodeStr(str4);
//  console.log(result4, result4 == expected4);

 /*****************************************************************************/

/* 
  String Decode  
*/

const str1 = "a3b2c1d3";
const expected1 = "aaabbcddd";
const str2 = "w2ghdb3fa4e1b";
const expected2 = "wwghdbbbfaaaaeb";

/**
 * Decodes the given string by duplicating each character by the following int
 * amount if there is an int after the character.
 * - Time: O(n * m), where n = str.length and m = largest (worst case) int in the
 *    string which will nested loop from .repeat.
 * - Space: O(n * m).
 * @param {string} str An encoded string with characters that may have an int
 *    after indicating how many times the character occurs.
 * @return {string} The given str decoded / expanded.
 */

function decodeStr(str) {
    let decoded = "";
    for (var i = 1; i < str.length; i++) {

        // parseInt returns NaN (which will evaluate to false) if cannot be cast as number
        //          returns the integer from the string if it can be cast as a number
        let number = parseInt(str[i]);
        //  isNaN returns true if not a number, and false if it is a number 
        let nextIsNotANumber = isNaN(str[i+1]);

        //  If it's a number
        if (number) {

            // Set var for the letter
            let char = str[i-1];

            // Add the letter the number of times needed
            for (let count = number; count > 0; count--) {
                decoded+= char;
            }
            // or could use .repeat():
            // decoded += char.repeat(number); // takes that number of operations
        }
        // Any cases where a number is not given for the character
        // just add the letter.
        else if (nextIsNotANumber) {
            decoded+= str[i];
        }

    }
    return decoded;
}

const result1 = decodeStr(str1);
console.log(result1, result1 == expected1);

const result2 = decodeStr(str2);
console.log(result2, result2 == expected2);

/*****************************************************************************/

module.exports = { decodeStr, encodeStr };

