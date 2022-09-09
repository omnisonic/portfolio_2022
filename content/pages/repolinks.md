Title: Github Repository List


  <div >
<div id="list">
    <h3>Omnisonic's Repos</h3>
    <ul class="noBullet github-cards" id="userRepos">
    </ul>
</div>
    </div>

<script>
    function requestUserRepos(username){
    const xhr = new XMLHttpRequest();
    const url = `https://api.github.com/users/${username}/repos`;
    xhr.open('GET', url, true);
    xhr.onload = function() {
        const data = JSON.parse(this.response);
        for(let i in data) {
            let ul = document.getElementById('userRepos');
            let li = document.createElement('li');
            li.classList.add('github-card');
            li.innerHTML = (`
            <p>Repo: ${data[i].name}</p>
            <p>Description: ${data[i].description}</p>
            <p>URL: <a href="${data[i].html_url}">${data[i].html_url}</a></p>
            `);
            ul.appendChild(li);
        }
    }
    xhr.send();   
}
requestUserRepos('omnisonic');
</script>