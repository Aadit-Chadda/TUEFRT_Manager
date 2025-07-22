
document.getElementById('search-bar').addEventListener('input', function(event) {
    // Get html elements.
    const searchTerm = event.target.value.toLowerCase();
    const itemDiv = document.querySelectorAll('.product');
    
    itemDiv.forEach(function(item) { // could I also use array map()?
        const itemText = item.textContent.toLowerCase();

        if(itemText.includes(searchTerm)) {
            item.style.display = 'flex';
        } else {
            item.style.display = 'none';
        }
    }); 

});

/* didn't work ripppp
window.addEventListener("load", () => {
    var filter = document.getElementById("search-bar"),
        list = document.querySelectorAll(".product");

    filter.addEventListener('onkeyup', function(){
        let search = filter.value.toLowerCase();

        for(let i of list) {
            let item = i.innerHTML.toLowerCase();
            if (item.indexOf(search) == -1) {
                i.style.display = 'list-item'; 
            } else {
                i.style.display = 'none';
            }
        }});
    });
 */   
