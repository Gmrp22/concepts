//  arguments passed by reference will reflect changes made to the object within the function, while primitive values will not be affected outside the function scope. Reassigning the parameter itself does not affect the original variable.

function changePrimitive(prim) {
  prim = 2;
  return prim;
}

let a = 1;
console.log(changePrimitive(a))
console.log(a); // 1



function changeObject(obj) {
  obj.name = "Changed";
  return obj;
}

let obj = { name: "Original" };
console.log(changeObject(obj))
console.log(obj); // { name: "Changed" }


// default parameters are evaluated at call time, they are not hoisted ----important
function defaultParam(obj = { name: "Default" }) {
  return obj;
}

console.log(defaultParam()) // { name: "Default" }
console.log(defaultParam({ name: "Provided" })) // { name: "Provided" }
