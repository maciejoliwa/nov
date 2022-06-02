function new_linked_list(){
return {head:null};
}

function push(ref,val){
if(ref.head===null){
ref.head = {next:null,value:val};
}else {
let second_reference = ref.head
while(true){
if(second_reference.next===null){
second_reference.next = {next:null,value:val};
break;
}else {
second_reference = second_reference.next;
break;
}
}
}
}

function iterate(ref,f){
node = ref.head;
while(true){
if(node!==null){
f(node.value);
node = node.next;
}else {
break;
}

}
}

let l = new_linked_list();

push(l,6);
push(l,9);
push(l,420);

iterate(l,console.log);