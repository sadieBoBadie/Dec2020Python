/*****************************************************************************/

/**
 * - Time: O(2n) -> O(n) linear. The 2n comes from the fact that words.length
 *    is at most the same length as wordsStr when there are no spaces.
 *    If there are spaces then words.length will be less than wordsStr
 *    because of the spaces being removed from the .split.
 * - Space: O(2n) -> O(n) linear. Storing wordsStr twice, once in words
 *    array and again in reversedWordOrder.
 */
function reverseWordOrderSplit(wordsStr) {
    // if all spaces
    if (wordsStr == false) {
      return wordsStr;
    }
  
    const words = wordsStr.split(" ");
    let reversedWordOrder = "";
  
    // loop backwards
    for (let i = words.length - 1; i >= 0; --i) {
      reversedWordOrder += words[i];
  
      // don't add an extra space at the end
      if (i !== 0) {
        reversedWordOrder += " ";
      }
    }
    return reversedWordOrder;
  }
  
  /**
   * - Time: O(n) linear.
   * - Space: O(n) linear. wordsStr is stored again in reversedWOrdOrder var.
   */
  function reverseWordOrder(wordsStr) {
    // if all spaces
    if (wordsStr == false) {
      return wordsStr;
    }
  
    let currWord = "";
    let reversedWordOrder = "";
  
    for (let i = wordsStr.length - 1; i >= 0; --i) {
      if (wordsStr[i] !== " ") {
        // prepend so the Word itself is not reversed by looping backWords
        currWord = wordsStr[i] + currWord;
      }
      // space found
      else {
        // add a space in front of the word, except on first word
        if (reversedWordOrder.length > 0) {
          currWord = " " + currWord;
        }
  
        reversedWordOrder += currWord;
        currWord = "";
      }
    }
  
    // no space at end of string means we didn't add the last word
    if (currWord.length > 0) {
      reversedWordOrder += " " + currWord;
    }
    return reversedWordOrder;
  }