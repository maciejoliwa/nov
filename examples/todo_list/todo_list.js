function __nov_for_each(arr, f) { arr.forEach(f); }
function __nov_on_click(e, f) { e.addEventListener('click', f); }
let todo_input = document.querySelector(`.input`);
let add_button = document.querySelector(`.add`);
let todos_wrapper = document.querySelector(`.todos`);
let todos = [{content:`Finish this app`,done:false}];

function render_single_todo(todo){
let todo_to_add = document.createElement(`div`);
todo_to_add.innerHTML = `<b>`+todo.content+`</b>`;
todos_wrapper.appendChild(todo_to_add);
}

function render_todos(){
todos_wrapper.innerHTML = null;
__nov_for_each(todos,render_single_todo);
}

function add_todo(){
if(todo_input.value!==``){
todos.push({content:todo_input.value,done:false});
todo_input.value = null;
render_todos();
}else {
alert(`Input cannot be empty!`);
}
}

__nov_on_click(add_button,add_todo);
render_todos();