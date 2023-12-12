//ABA REGISTRO

function cadastro(form) {
    var nome = form.nome.value;
    var email = form.email.value;
    var senha = form.senha.value;
    var confirmarSenha = form.confirmar_senha.value;

    var temArroba = email.includes('@');

    if (nome && email && senha && confirmarSenha && senha === confirmarSenha && temArroba) {
        alert('Cadastro realizado com sucesso!');
        window.location.href = 'index.html';
    } else {
        alert('Preencha todos os campos corretamente, incluindo um endereço de e-mail válido.');
    }
}

//ABA LOGIN

botaoLogin.addEventListener('click', entrar);
function entrar(evento) {
    window.location.href='/templates/cards.html';
}

//ABA UPLOAD E CARDS

function addPost(button) {
    const titulo = document.getElementById("inputTexto").value;
    const descricao = document.getElementById("inputDescricao").value;
    const fotoUrl = document.getElementById("upload").value; // Este é apenas um exemplo, você precisa carregar a imagem de alguma forma

    // Verifica se os campos obrigatórios foram preenchidos
    if (titulo && descricao && fotoUrl) {
        // Cria um novo elemento div para representar o post
        const novoItem = document.createElement("div");
        novoPost.className = "post";

        // Adiciona o conteúdo do post ao novo elemento
        novoPost.innerHTML = `
            <img src="${fotoUrl}" alt="${titulo}" class="foto">
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
    } else {
        alert("Preencha todos os campos obrigatórios.");
    }
}
