function app() {
    console.log("app iniciado!");
    addFavorito();
}

function addFavorito() {
    // Suponha que você tenha elementos com os IDs "elemento1", "elemento2", "elemento3", ...
    // Você pode usar um seletor CSS para selecionar todos os elementos que começam com "elemento"
    var buttons = document.querySelectorAll('[id^="add_favorito"]');

    var contador = 0

    // PARA CADA BOTÃO
    buttons.forEach(async (button) => {
        console.log(button); // Debug

        const produtoID = button.getAttribute("data-produto-id");
        // console.log(produtoID)

        const csrftoken = getCookie('csrftoken'); // Substitua 'getCookie' pela função correta para obter cookies

        const response = await axios.get("http://localhost:8000/api/favoritar", {
            headers: {
                'X-CSRFToken': csrftoken,
            },
        });

        // console.log(response.data)
        // console.log(response.data.favoritos)

        let arrayDeProdutosFavoritos = response.data.favoritos.map(objeto => objeto.produto_favorito);
        console.log(arrayDeProdutosFavoritos);

        for (let i = 0; i < arrayDeObjetos.length; i++) {
            let produtoFavoritoAtual = arrayDeObjetos[i].produto_favorito;
            console.log(produtoFavoritoAtual);
            if (produtoFavoritoAtual === produtoID) {
                console.log("PASSOU AQUI")
                contador++
                botao = document.getElementById(button.id)
                console.log(botao)
                console.log(produtoID)
                botao.innerHTML = ''
    
                const novoIcone = document.createElement("i")
                novoIcone.classList = "fa-solid fa-check"
    
                botao.appendChild(novoIcone)
            }
        }

        button.onclick = async (event) => {
            event.preventDefault();


            if (response.data.usuario.id) {
                const usuario_id = response.data.usuario.id;
                const favorito_id = response.data.favoritos.id;

                // VERIFICA SE TEM FAVORITO PARA O SEGUNDO CLIQUE
                if (response.data.favoritos.produto_favorito === produtoID) {
                    await axios.delete(`http://localhost:8000/api/favoritar?favorito=${favorito_id}`, {
                        headers: {
                            'X-CSRFToken': csrftoken,
                        }
                    }).then((response) => {
                        if (response.staus === 200) {
                            botao = document.getElementById(button.id)
                            botao.innerHTML = ''

                            const novoIcone = document.createElement("i")
                            novoIcone.classList = "fa-regular fa-bookmark"

                            botao.appendChild(novoIcone)
                        }
                    });

                } else {
                    await axios.post("http://localhost:8000/api/favoritar", {
                        produto_favorito: produtoID,
                        usuario: usuario_id,
                    }, {
                        headers: {
                            'X-CSRFToken': csrftoken,
                        },
                    }).then((response) => {
                        if (response.status === 202) {
                            // Ação no HTML quando a resposta for um status 202 (Aceito)
                            botao = document.getElementById(button.id)
                            botao.innerHTML = ''

                            const novoIcone = document.createElement("i")
                            novoIcone.classList = "fa-solid fa-check"

                            botao.appendChild(novoIcone)

                            console.log("Ação bem-sucedida! Pode adicionar sua lógica aqui.");
                        }
                    }).catch((error) => {
                        console.error("Erro na solicitação POST:", error);
                    });
                }

            // SE NÃO ESTIVER LOGADO
            } else {
                window.location.href = `${redireciona}`;
            }
        };
    });
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

app();
