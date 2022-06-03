# <center> The Nov Programming Language 🦊</center>

A simple, small language that transpiles to JavaScript 

##### Current version: 0.0.5
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
to_string = ANY.prototype.toString
element = document.querySelector
new_element = document.createElement,
foreach = ANY.forEach  // example: foreach(array, function)
on_click = ANY.addEventListener  // example: on_click(element, function)

// More coming up in the future!
```

## Getting Started

### Variables
Variables are created using **<-** symbol
```js
name <- "Avery"
language <- "Nov"
favourite_animal <- "Fox"

name <! "Maciej"  // Assign new value
```

### If and loops
Nov provides a pretty cool loop called **forever** which just runs... forever! Use **break** to end the loop in any place you want. 
```js
i <- 0

if (i is 0) {
    log("i is equal to 0");
}

if (i isNot 1) {
    log("i is not equal to 1");
}

forever {
    if (i == 5) {
        break
    }

    i <! i + 1
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

## Example linked list:
```js
func new_linked_list() {
    return { head: null };
} 

func push(ref, val) {
    if (ref.head is null) {
        ref.head <! { value: val, next: null };
        return; 
    }
    
    second_reference <- ref.head;
    
    forever {
        if (second_reference.next is null) {
            second_reference.next <! { next: null, value: val };
            break;
        } 

        second_reference <! second_reference.next;
    }
}

func iterate(ref, f) {
    node <! ref.head;
    forever {
        if (node isNot null) {
            f(node.value);
            node <! node.next;
        } else {
            break;
        }
    }
}

l <- new_linked_list();

push(l, 6);
push(l, 9);
push(l, 420);

iterate(l, log);
```
