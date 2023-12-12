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

function cadastraUsuario(event) {
    event.preventDefault(); // Evita o comportamento padrão do formulário

    // Pega os valores do formulário
    let nome = document.getElementById("nome").value;
    let email = document.getElementById("email").value;
    let senha = document.getElementById("senha").value;
    // Confirmação de senha (opcional)
    let confirmarSenha = document.getElementById("confirmar_senha").value;

    // Verifica se as senhas coincidem
    if (senha !== confirmarSenha) {
        alert("As senhas não coincidem!");
        return; // Encerra a função se as senhas não coincidirem
    }

    // Cria um objeto com os dados do formulário
    let body = {
        "name": nome,
        "email": email,
        "password": senha
    };

    // URL para o servidor Python receber os dados
    let url = "http://127.0.0.1:5000/users";

    // Envia os dados para o servidor usando a função fazPost
    fazPost(url, body);
}

// Adiciona um listener para o evento 'submit' do formulário
document.querySelector("#registroForm").addEventListener("submit", cadastraUsuario);
