/* 
  String: Rotate String
  Create a standalone function that accepts a string and an integer, 
  and rotates the characters in the string to the right by that given integer amount.
*/

/**
 * Rotates a given string's characters to the right by the given amount,
 * wrapping characters to the beginning.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @param {number} n The amount of characters in the given str to rotate to the
 *    right.
 * @return {string} The string rotated by the given amount.
 */
function rotateStr(str, n) {}


const str1 = "Hello World";
const rotateAmnt1 = 0;
const expected1 = "Hello World";

const str2 = "Hello World";
const rotateAmnt2 = 1;
const expected2 = "dHello Worl";

const str3 = "Hello World";
const rotateAmnt3 = 2;
const expected3 = "ldHello Wor";

const str4 = "Hello World";
const rotateAmnt4 = 4;
const expected4 = "orldHello W";

module.exports = { rotateStr };

/*****************************************************************************/