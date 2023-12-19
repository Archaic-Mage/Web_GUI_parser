function add_input_field(some) {
    let input = document.createElement("input");
    let name = some.name;
    let index = name.split('-')[1]
    let first_name = name.split('-')[0]
    input.type = 'text'
    new_name = first_name + '-' + (parseInt(index) + 1)
    input.name = new_name
    input.id = new_name
    input.classList = ['text-holder']
    parent  = some.parentNode
    new_btn = some.cloneNode(true)
    new_btn.name = new_name
    some.remove()
    parent.appendChild(input)
    parent.appendChild(new_btn)
}


function change_active(ele) {
    let parent = ele.parentNode
    for(var i = 0; i < parent.children.length; i++) {
        var child = parent.children[i].classList.remove('active')
    }
    ele.classList.add('active')
}