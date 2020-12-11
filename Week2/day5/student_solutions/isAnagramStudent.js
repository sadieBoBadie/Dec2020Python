// Posted by Emilie and Niharika from group algos

function isAnagram(s1, s2) {
    if(s1.length != s2.length){
      return false;
    }
    s1 = s1.toLowerCase(); 
    s2 = s2.toLowerCase();
  
    var obj1 = {};
    var obj2 = {};
  
    for(let char of s1) {
      if(obj1[char]) {
        obj1[char] += 1;
      }
      else {
        obj1[char] = 1;
      }
    }
    
    for(let char of s2) {
      if(obj2[char]) {
        obj2[char] += 1;
      }
      else {
        obj2[char] = 1;
      }
  
    }
    console.log(obj1);
    console.log(obj2);
    if (Object.keys(obj1).length !== Object.keys(obj2).length) {
      return false;
    }
    for(let key in obj1) {
      if(obj1[key]!=obj2[key]){
        return false;
      }
    }
  return true;
    
  }
  // yees
  // has(key)
  // Returns whether an entry with the given key exists

  function isAnagram(s1, s2) {
  if(s1.length != s2.length){
    return false;
  }
  s1 = s1.toLowerCase(); 
  s2 = s2.toLowerCase();

  var obj1 = {};
  var obj2 = {};

  for(let char of s1) {
    if(obj1[char]) {
      obj1[char] += 1;
    }
    else {
      obj1[char] = 1;
    }
  }
  
  for(let char of s2) {
    if(obj2[char]) {
      obj2[char] += 1;
    }
    else {
      obj2[char] = 1;
    }

  }
  console.log(obj1);
  console.log(obj2);
  if (Object.keys(obj1).length !== Object.keys(obj2).length) {
    return false;
  }
  for(let key in obj1) {
    if(obj1[key]!=obj2[key]){
      return false;
    }
  }
return true;
  
}
  
  const strA1 = "yeeeees";
  const strB1 = "eeeecys";
  const expected1 = false;
  
  const strA2 = "yes";
  const strB2 = "eYs";
  const expected2 = true;
  
  const strA3 = "no";
  const strB3 = "noo";
  const expected3 = false;
  
  const strA4 = "silent";
  const strB4 = "listen";
  const expected4 = true;
  console.log(isAnagram(strA1, strB1));
  console.log(isAnagram(strA2, strB2));
  console.log(isAnagram(strA3, strB3))
  console.log(isAnagram(strA4, strB4))