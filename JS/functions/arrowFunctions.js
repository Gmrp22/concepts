
let printName = name => console.log(name)

printName('Gilda')

function Person(name, age) {
    this.name = name
    this.age = age
}

let p =  new Person('Gilda', 30)
console.log(p) // Person {}