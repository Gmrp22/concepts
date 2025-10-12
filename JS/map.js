let newMap = new Map([
    ['a', 1],
    ['b', 2],
    ['c', 3]
]);
console.log(newMap);
newMap.set('d', 4);
console.log(newMap);
newMap.delete('b');
console.log(newMap);
newMap.set('a', 10); // Update value for key 'a'
console.log(newMap);

newMap.set([1], [1, 2, 3]);
console.log(newMap);

for (let x of newMap) {
    console.log(x);
}


//weakMap
// Only accepts objects as keys and does not prevent garbage collection, cant be iterated
let wm = new WeakMap();

let obj = {name: "Alice"};
wm.set(obj, "datos");

console.log(wm.get(obj)); // "datos"
console.log(wm.has(obj)); // true

obj = null;
// At this point, the entry in the WeakMap may be garbage collected
// after some time, since there are no other references to the key object.
console.log(wm.has(obj)); // false, since obj is now null