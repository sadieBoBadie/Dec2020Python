function isAnagram(s1, s2) {
    var s1l = s1.length;
    var s2l = s2.length;
    var myDict = {};
    if(s1l != s2l){
        return false;
    }
    for(var i=0;i<s1.length;i++){
        if(s1[i] in myDict){
            myDict[s1[i]] = myDict[s1[i]]+1;
        }
        else {
            myDict[s1[i]] = 1;
        }
    }
    for(var j=0;j<s1.length;j++){
        if(s2[j] in myDict){
            myDict[s2[j]] = myDict[s2[j]] - 1;
        }
        else {
            return false;
        }
    }
    var istrue = Object.keys(myDict).every((k) => myDict[k] === 0);
    return istrue;
};