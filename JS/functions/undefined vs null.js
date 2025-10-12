let value
console.log(value) // undefined

let value2 = null
console.log(value2) // null

console.log(typeof value) // undefined
console.log(typeof value2) // object bug of JS

console.log(value === value2) // false
console.log(value == value2) // true