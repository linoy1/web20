$(document).ready(function(){

    axios.get(`http://newsapi.org/v2/top-headlines?country=il&category=entertainment&apiKey=c21ad93be4524c388271ce87094eae38`)
    .then(res => {
        const data = res.data.articles;
        const ideas = document.getElementById('ideas');
        ideas.innerHTML = '';
        data.forEach(element => {
            console.log(element);
            ideas.innerHTML += `
                <p>
                    <a href="${element.url}">${element.title}</a>
                </p>
                <img src="${element.urlToImage}" alt="no data for this artical" width="500" height="600">
            `
        });
        console.log();
    })

});
