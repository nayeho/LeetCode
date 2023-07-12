/**
 * @param {number} n
 * @return {Function} counter
 */
var temp = 0;

var createCounter = function(n) {
    return function() {
        temp = n;
        
        return n++;
        
        
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */