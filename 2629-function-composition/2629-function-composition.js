/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
	return function(x) {
        
        if(functions.length === 0){
            return x;
        }
        
        for(let i = 0; i < functions.length; i++){
            x = functions[functions.length - 1 - i](x);
        }
        return x;
        
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */