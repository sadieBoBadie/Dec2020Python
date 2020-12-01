/*

Possible topics for discussion:
    refactoring old code
    ternary statements
    review string concatenation

*/

/* 
  Given an arr and a separator string, output a string of every item in the array separated by the separator.
  
  No trailing separator at the end
  Default the separator to a comma with a space after it if no separator is provided
*/

const arr1 = [1, 2, 3];
const separator1 = ", ";
const expected1 = "1, 2, 3";

const arr2 = [1, 2, 3];
const separator2 = "-";
const expected2 = "1-2-3";

const arr3 = [1, 2, 3];
const separator3 = " - ";
const expected3 = "1 - 2 - 3";

const arr4 = [1];
const separator4 = ", ";
const expected4 = "1";

const arr5 = [];
const separator5 = ", ";
const expected5 = "";

/**
 * Converts the given array into a string of items separated by the given separator.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string|number|boolean>} arr The items to be joined as a string.
 * @param {string} separator To separate each item of the given arr.
 * @return {string} The given array items as a string separated by the given separator.
 */
function join(arr, separator) {

    let outPutString = !arr.length? "": String(arr[0]);

    for (let i = 1; i < arr.length; i++) {
        outPutString+= separator + arr[i];
    }
    return outPutString;
}

const result1 = join(arr1, separator1);
console.log(result1, result1 === expected1);

const result2 = join(arr2, separator2);
console.log(result2, result2 === expected2);

const result3 = join(arr3, separator3);
console.log(result3, result3 === expected3);

const result4 = join(arr4, separator4);
console.log(result4, result4 === expected4);

const result5 = join(arr5, separator5);
console.log(result5, result5 === expected5);

module.exports = { join };

/*****************************************************************************/


/* 
  Book Index
  Given an arry of ints representing page numbers
  return a string with the page numbers formatted as page ranges when the nums span a consecutive range
*/

const nums1 = [1, 2, 3, 4, 10, 13, 14, 15, 16, 20, 35, 37, 38, 55, 56, 57, 58, 59, 60, 70];
// const expected1 = "1-4, 10, 13-16, 20, 35, 37-38, 55-60, 70";

/**
 * Turns the given arr of page numbers into a string of comma hyphenated
 * page ranges.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums Page numbers.
 * @return {string} The given page numbers as comma separated hyphenated
 *    page ranges.
 */
function bookIndex(nums) {

    let pageNums = String(nums[0])

    for (let i = 1; i < nums.length; i++) {

        let currentPage = nums[i];
        let previousPage = nums[i-1];
        let nextPage = nums[i+1];

        // Starting a new page-range
        if (previousPage !== currentPage - 1) {
            pageNums += `, ${currentPage}`;
        }
        // Ending a page range
        else if (nextPage !== currentPage + 1){
            pageNums += `-${currentPage}`;
        }
        // Otherwise is within a page-range, do not add page

    }
    return pageNums;
}

let result = bookIndex(nums1);
// console.log(result, result === expected1);

module.exports = { bookIndex };

/*****************************************************************************/