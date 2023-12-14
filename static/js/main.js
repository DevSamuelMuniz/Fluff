function addPost() {
    const titulo = document.getElementById("inputTexto").value;
    const descricao = document.getElementById("inputDescricao").value;
    const fotoUrl = document.getElementById("imagemData").value; // Este é apenas um exemplo, você precisa carregar a imagem de alguma forma

    // Verifica se os campos obrigatórios foram preenchidos
    if (titulo && descricao && fotoUrl) {
        // Cria um novo elemento div para representar o post
        const novoPost = document.createElement("div");
        novoPost.className = "novoPost";

        // Adiciona o conteúdo do post ao novo elemento
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

        // Adiciona o novo post à div com a classe "posts" na página "cards.html"
        const postsContainer = document.querySelector('.posts');
        postsContainer.appendChild(novoPost);

        // Limpa os campos do formulário na página "upload.html"
        document.getElementById("inputTexto").value = "";
        document.getElementById("inputDescricao").value = "";
        document.getElementById("upload").value = "";

        // Redireciona para a página de cards após adicionar o post com sucesso
        window.location.href = 'cards.html';
    } else {
        alert("Preencha todos os campos obrigatórios.");
    }
}


// Função para adicionar posts na página cards.html
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


// Requisição para obter os posts e adicionar à página
fetch('/get_posts')
    .then(response => response.json())
    .then(posts => addPosts(posts))
    .catch(error => console.error('Erro:', error));




//



// Função para enviar os dados para o backend
function fazPost(url, body) {
    // Criação de uma requisição AJAX
    let request = new XMLHttpRequest();
    
    // Configura a requisição POST
    request.open("POST", url, true);
    request.setRequestHeader("Content-type", "application/json");

    // Define a função a ser executada quando a requisição terminar
    request.onload = function() {
        console.log(this.responseText);
        // Faça o que precisar com a resposta do servidor, se necessário
    };

    // Envia os dados do formulário para o servidor
    request.send(JSON.stringify(body));
}

function publicar() {
    // Pega os valores dos campos
    let titulo = document.getElementById("inputTexto").value;
    let descricao = document.getElementById("inputDescricao").value;
    let imagemSelecionada = document.getElementById("upload").files[0];

    // Verifica se um arquivo foi selecionado
    if (imagemSelecionada) {
        let fileReader = new FileReader();

        fileReader.onload = function(event) {
            let imageData = event.target.result; // Obtém a imagem como base64

            // Cria um objeto com os dados do formulário
            let body = {
                "titulo": titulo,
                "descricao": descricao,
                "imageData": imageData
            };

            // URL para o servidor Python receber os dados
            let url = "upload";
            // Envia os dados para o servidor usando a função fazPost
            fazPost(url, body);
        };

        // Converte a imagem para base64
        fileReader.readAsDataURL(imagemSelecionada);
    } else {
        alert('Selecione uma imagem antes de publicar.');
    }
}

// Adiciona um listener para o evento 'click' do botão de publicar
document.getElementById("publicar").addEventListener("click", publicar);
