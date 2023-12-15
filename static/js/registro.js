function fazPost(url, body) {
    let request = new XMLHttpRequest();
    
    request.open("POST", url, true);
    request.setRequestHeader("Content-type", "application/json");

    request.onload = function() {
        console.log(this.responseText);
    };

    request.send(JSON.stringify(body));
}

function cadastraUsuario(event) {
    event.preventDefault(); 

    let nome = document.getElementById("nome").value;
    let email = document.getElementById("email").value;
    let senha = document.getElementById("senha").value;
    let confirmarSenha = document.getElementById("confirmar_senha").value;

    if (senha !== confirmarSenha) {
        alert("As senhas não coincidem!");
        return; 
    }

    let body = {
        "name": nome,
        "email": email,
        "password": senha
    };

    let url = "http://127.0.0.1:5000/users";

    fazPost(url, body);
}

document.querySelector("#registroForm").addEventListener("submit", cadastraUsuario);


var reader = new FileReader();

reader.onload = function(event) {
    var imageData = event.target.result;

    var imageObject = {
        "imageData": imageData,
    };

    fetch('/upload', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(imageObject)
    })
    .then(response => {
    })
    .catch(error => {
    });
};

reader.readAsDataURL(capturedImage);
