

function outerFunction() {
    let outerVariable = 1;

    function innerFunction() {
        debugger
        var terst = 0
        outerVariable += 1;
        console.log(outerVariable); // Accessing variable from outer function
    }

    return innerFunction;
}

const myClosure = outerFunction();
myClosure();
myClosure();
