# <center> The Nov Programming Language 🦊</center>

A simple, small language that transpiles to JavaScript 

##### Current version: 0.0.1
___
Example:

```js
// Semicolons are optional
age <- 20;
funny <- 69;  // I am a very funny individial
log(age + funny);
```

Output JavaScript:
```js
let age = 20;
let funny = 69;
console.log(age + funny);
```

Nov is just a hobby project, it aims to make writing simple web apps a bit faster. Some of the syntax of the language may seem weird, but it's just the way I would like programming languages to look like, so yeah, just a personal choice.

Nov comes with a lot of built-in functions, that are just abstractions over javascript functions, here's the current list of them:
```js
log = console.log
to_int = Number.parseInt
to_float = Number.parseFlot
element = document.querySelector

// More coming up in the future!
```

## Getting Started

### Variables
Variables are created using **<-** symbol
```js
name <- "Avery"
language <- "Nov"
favourite_language <- "Fox"
```

### If and loops
Nov provides a pretty cool loop called **forever** which just runs... forever! Use **break** to end the loop in any place you want. 
```js
i <- 0

forever {
    if (i == 5) {
        break
    }

    i = i + 1
}
```

### Functions
Functions are defined using **func** keyword, just like in Go.
```js
func sayHello() {
    log("HELLO!")
}

sayHello()
```