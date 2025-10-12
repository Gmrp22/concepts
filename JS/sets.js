let setq = new Set([1, 2, 3]);
console.log(setq); // Set { 1, 2, 3 }
setq.add(4);
console.log(setq); // Set { 1, 2, 3, 4 }
setq.delete(2);
console.log(setq);
setq.add(3); // No effect, 3 is already in the set
console.log(setq);

//weakSet
// Only accepts objects and does not prevent garbage collection, cant be iterated
let ws = new WeakSet();

let obj1 = {name: "Bob"};
let obj2 = {name: "Charlie"};

ws.add(obj1);
ws.add(obj2);

console.log(ws, '//');

//ou need to inspect or print the objects, you would need to maintain a separate reference to them, such as in an array or another data structure. For example
let objects = [obj1, obj2];
objects.forEach(obj => {
  console.log(ws.has(obj) ? obj : "Not in WeakSet");
});