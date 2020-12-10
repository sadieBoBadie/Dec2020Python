/* 
  Create the function isRotation(str1,str2) that
  returns whether the second string is a rotation of the first.
*/

/**
 * Determines whether the second string is a rotated version of the first.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} s1
 * @param {string} s2
 * @return {boolean} Whether the second string is a rotated version of the 1st.
 */
function isRotation(s1, s2) {

}

const strA1 = "ABCD";
const strB1 = "CDAB";
const expected1 = true;
// Explanation: if you start from A in the 2nd string, the letters are in the same order, just rotated

const strA2 = "ABCD";
const strB2 = "CDBA";
const expected2 = false;
// Explanation: all same letters in 2nd string, but out of order

module.exports = { isRotation };

/*****************************************************************************/
