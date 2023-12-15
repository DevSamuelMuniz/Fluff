function addPost() {
    const titulo = document.getElementById("inputTexto").value;
    const descricao = document.getElementById("inputDescricao").value;
    const fotoUrl = document.getElementById("imagemData").value; /

    if (titulo && descricao && fotoUrl) {
        const novoPost = document.createElement("div");
        novoPost.className = "novoPost";

        novoPost.innerHTML = `
            <img src="${fotoUrl}" alt="${titulo}"  class="foto">
            <div class="icons">
                <div class="esquerda">
                    <i class="fa-regular fa-bookmark"></i>
                </div>
                <div class="direita">
                    <i class="fa-solid fa-share"></i>
                    <i class="fa-regular fa-heart"></i>
                </div>
            </div>
        `;

        const postsContainer = document.querySelector('.posts');
        postsContainer.appendChild(novoPost);

        document.getElementById("inputTexto").value = "";
        document.getElementById("inputDescricao").value = "";
        document.getElementById("upload").value = "";

        window.location.href = 'cards.html';
    } else {
        alert("Preencha todos os campos obrigatórios.");
    }
}

function addPosts(posts) {
    const postsContainer = document.querySelector('.posts');

    posts.forEach(post => {
        const { imagem, titulo, descricao } = post;

        const novoPost = document.createElement("div");
        novoPost.className = "post";

        novoPost.innerHTML = `
        <img src="${imagem}" alt="${titulo}" class="foto">
        <!-- Adicione outros elementos conforme necessário -->
    `;
    

        postsContainer.appendChild(novoPost);
    });
}

fetch('/get_posts')
    .then(response => response.json())
    .then(posts => addPosts(posts))
    .catch(error => console.error('Erro:', error));


fetch('/get_posts')
    .then(response => response.json())
    .then(posts => addPosts(posts))
    .catch(error => console.error('Erro:', error));




//



function fazPost(url, body) {
    let request = new XMLHttpRequest();
    
    request.open("POST", url, true);
    request.setRequestHeader("Content-type", "application/json");

    request.onload = function() {
        console.log(this.responseText);
    };

    request.send(JSON.stringify(body));
}

function publicar() {
    let titulo = document.getElementById("inputTexto").value;
    let descricao = document.getElementById("inputDescricao").value;
    let imagemSelecionada = document.getElementById("upload").files[0];

    if (imagemSelecionada) {
        let fileReader = new FileReader();

        fileReader.onload = function(event) {
            let imageData = event.target.result; 

            let body = {
                "titulo": titulo,
                "descricao": descricao,
                "imageData": imageData
            };

            let url = "upload";
            fazPost(url, body);
        };

        fileReader.readAsDataURL(imagemSelecionada);
    } else {
        alert('Selecione uma imagem antes de publicar.');
    }
}

document.getElementById("publicar").addEventListener("click", publicar);
