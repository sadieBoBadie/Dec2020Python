/*****************************************************************************/

/**
 * - Time: O(n) linear.
 * - Space: O(n) linear.
 */
function frequencyTableBuilder(arr) {
    const freqTable = {};
  
    for (let i = 0; i < arr.length; i++) {
      const str = arr[i];
  
      if (freqTable.hasOwnProperty(str) === false) {
        // first occurrence found
        freqTable[str] = 1;
      } else {
        freqTable[str]++;
      }
    }
    return freqTable;
  }
  
  function frequencyTableBuilder2(arr) {
    const freqTable = {};
  
    for (const str of arr) {
      if (freqTable.hasOwnProperty(str) === false) {
        // first occurrence found
        freqTable[str] = 1;
      } else {
        freqTable[str]++;
      }
    }
  
    return freqTable;
  }