/* 
  Braces Valid
  Given a string sequence of parentheses, braces and brackets, determine whether it is valid. 
*/

/**
 * Determines whether the string's braces, brackets, and parenthesis are valid
 * based on the order and amount of opening and closing pairs.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @return {boolean} Whether the given strings braces are valid.
 */
function bracesValid(str) {

}

const str1 = "({}[({})])[{}]!";
const expected1 = true;

const str2 = "({}[]){";
const expected2 = false;

const str3 = "()[(]{)}";
const expected3 = false;

module.exports = { bracesValid };

/*****************************************************************************/