"use strict"
let fillter = document.getElementById('searchbox');
fillter.addEventListener('keyup' , function(){
    let search = this.value.toLowerCase();
    let customer = document.querySelectorAll('#customer cusname');
    let searchbox =document.getElementById('searchbox');

 
    for(let i of cusname){
        let item = i.innerHTML.toLowerCase();
        
        if(item.indexOf(search) == -1)
        i.classList.add('hide') 
        
        else
            i.classList.remove('hide');
        
        
    }
})