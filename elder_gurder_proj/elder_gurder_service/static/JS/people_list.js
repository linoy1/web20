jQuery(document).ready(function($) {
    $('*[data-href]').on('click', function() {
        window.location = $(this).data("href");
    });
    $('#search_address').on('click', (e) => {
        console.log(e);
        const peopels = document.getElementsByClassName('person');
        
        const search_value_el = document.getElementById('search_value');
        const search_value = search_value_el.value

        console.log(search_value);

        for (let item of peopels) {
            const id = item.getAttribute("id");
            const addres_id = `address_${id}`
            const addres_el = document.getElementById(addres_id);
            const addres_text = addres_el.textContent;
            if (search_value == '') {
                item.setAttribute('class', 'person')
            } else {
                // if the search_value does include addres_text  
                if (search_value.includes(addres_text)) {
                    item.setAttribute('class', 'person')
                } else {
                    item.setAttribute('class', 'person hide_row')
                }
            }
            
        }
    });
    
});