const filter = document.getElementById('searchFilter');
const items = document.querySelectorAll('.product'); // oughta change that name up soon lol also querySelectorAll places it in a list.
const searchFilter = document.getElementById('search-bar');
var globalSelectedType = 'All'; // by default it's 'All' so there's no null errors.
// need to set item to be .product and not prdocut-left

filter.addEventListener('change', function() {
    const selectedType = this.value;
    globalSelectedType = selectedType;

    items.forEach(item => {
        const itemType = item.getAttribute('data-type');
        
        // Only want item to be searchable if the itemType matches the selectedType.
        if (selectedType === 'All' || itemType === selectedType){ // They stay weird for some reason.
            item.style.display = 'flex'; 
        } else {
            item.style.display = 'none';
        }
    })
}); // current issue is that everything is hidden when 'All' is toggled and search is performed.

searchFilter.addEventListener('input', function(event) {
    const searchTerm = event.target.value.toLowerCase();
    //const itemDiv = document.querySelectorAll('.product');

    items.forEach(item => { 
        const itemText = item.textContent.toLowerCase();
        const itemType = item.getAttribute('data-type');

        if(itemText.includes(searchTerm) && itemType === globalSelectedType || itemText.includes(searchTerm) && globalSelectedType === 'All') {
            item.style.display = 'flex';
        } else {
            item.style.display = 'none';
        }
    });
});


