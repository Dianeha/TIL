typeof true; //bool
typeof false;

// 없다. 확실히 없다 (의도한 결과)
typeof null;

// 아 몰라.. 없어 (의도하지 않은 결과)
typeof undefined; // undefined

typeof 'asdf'; // string

// number
typeof 1;
typeof 1.1;
typeof Infinity;
typeof NaN;


typeof [1, 2]; // object
Array.isArray([1,2]) // true
typeof {a:2, b:3}; // object

typeof function(){}; //function



