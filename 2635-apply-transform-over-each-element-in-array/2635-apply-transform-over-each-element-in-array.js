/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    
    const returnArray = [];
    
    for(var i = 0; i < arr.length; i++){
        returnArray.push(fn(arr[i], i));
    }
    
    return returnArray;
    
};