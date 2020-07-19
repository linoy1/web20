function removeChilds (node) {
    var last;
    while (last = node.lastChild) node.removeChild(last);
};

async function displayPosts() {
    const res = await axios.get(`https://jsonplaceholder.typicode.com/users/1/posts`)
    
    const data = res.data;
    const ideas = document.getElementById('ideas');
    removeChilds(ideas);
    // ideas.innerHTML = '';
    data.forEach(element => {
        const post_id = element.id.toString();

        console.log(element);
        const container = document.createElement('div');
        const content_wrapper = document.createElement('div');
        const header = document.createElement('h3');
        const p = document.createElement('p');

        header.textContent = element.title;
        p.textContent = element.body;
        
        content_wrapper.setAttribute('id', post_id);
        content_wrapper.appendChild(header);
        content_wrapper.appendChild(p);

        container.appendChild(content_wrapper);

        ideas.appendChild(container);

        content_wrapper.addEventListener('click',  () => {
            displayaCommnetes(post_id);
        });
        
    });
}

async function displayaCommnetes(id) {
    const comments_url = `https://jsonplaceholder.typicode.com/posts/${id}/comments`;
    const comments = document.getElementById('comments');
    // comment.innerHTML = ''
    const respond  = await axios.get(comments_url)
    const commntes_data = respond.data
    removeChilds(comments);

    commntes_data.forEach(comment => {
        const container = document.createElement('div');
        const wrapper_container = document.createElement('div');
        const name = document.createElement('h4');
        const email = document.createElement('h5');
        const body = document.createElement('p');

        name.textContent  = comment.name;
        email.textContent = comment.email;
        body.textContent  = comment.body;

        wrapper_container.appendChild(name);
        wrapper_container.appendChild(email);
        wrapper_container.appendChild(body);

        container.appendChild(wrapper_container);

        comments.appendChild(container);

    });
}
jQuery(document).ready(function($) {
    displayPosts();
});