// pulls out the elements of an array or object
// and spreads them into individual elements

const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];

// Spread in arrays
const combined = [...arr1, ...arr2];
console.log(combined); // [1, 2, 3, 4, 5, 6]

// Spread in objects
const obj1 = { a: 1, b: 2 };
const obj2 = { c: 3, d: 4 };

const merged = { ...obj1, ...obj2 };
console.log(merged); // { a: 1, b: 2, c: 3, d: 4 }

const newp = {a:2, ...obj1}
