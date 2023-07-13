/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    
    const resultArray = [];
    
    for(var i = 0; i < arr.length; i++){
        
        if(fn(arr[i], i)){
            resultArray.push(arr[i]);
        }
        
    }
    
    return resultArray;
    
};