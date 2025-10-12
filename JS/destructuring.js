
let myArray = [1,2,3,4,5]

let [a, b] = myArray
console.log(a, b)


let person = {
    name: 'Gilda',
    age: 30,
    country: 'CO'
}

let {name:nameP, age} = person
console.log(nameP, age)



function printPerson({name, age}) {
    console.log(name, age)
}

printPerson(person)