//Object literal
let Person = {
    name: 'Gilda',
    age: 30,
    country: 'CO'
}


//New object
let person1 = new Object()
person1.name = 'Gilda'
person1.age = 30
person1.country = 'CO'

//Constructor function
function createPerson(name, age, country) {
   this.name = name
    this.age = age
    this.country = country
}
//each instance duplicates the methods, so we use prototypes
createPerson.prototype.greet = function() {
    console.log(`Hello, my name is ${this.name}`);
}
let p = new createPerson('Gilda', 30, 'CO')
p.greet() // Hello, my name is Gilda


//class
class CreatePerson {
    constructor(name, age, country) {
        this.name = name
        this.age = age
        this.country = country
    }

    greet() {
        console.log(`Hello, my name is ${this.name}`);
    }
}

let p2 = new CreatePerson('Gilda', 30, 'CO')
p2.greet() // Hello, my name is Gilda



//Factory function
function factoryPerson(name, age, country) {
    return {
        name,
        age,
        country,
        greet() {
            console.log(`Hello, my name is ${this.name}`);
        }
    }
}

let p3 = factoryPerson('Gilda', 30, 'CO')
p3.greet() // Hello, my name is Gilda


//object prototypes
const personaProto = {
  saludar() {
    console.log(`Hola, soy ${this.nombre}`);
  }
};

const juan = Object.create(personaProto);
juan.nombre = "Juan";
juan.saludar();
