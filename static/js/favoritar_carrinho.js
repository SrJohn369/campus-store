function app() {
    console.log("app iniciado!");
    addFavorito();
}

function addFavorito() {
    // Suponha que você tenha elementos com os IDs "elemento1", "elemento2", "elemento3", ...
    // Você pode usar um seletor CSS para selecionar todos os elementos que começam com "elemento"
    var buttons = document.querySelectorAll('[id^="add_favorito"]');

    // PARA CADA BOTÃO
    buttons.forEach(async (button) => {
        // console.log(button); // Debug

        const produtoID = button.getAttribute("data-produto-id");
        // console.log(produtoID)

        const csrftoken = getCookie('csrftoken'); // Substitua 'getCookie' pela função correta para obter cookies

        const response = await axios.get(`http://${webDev}/api/favoritar`, {
            headers: {
                'X-CSRFToken': csrftoken,
            },
        }).catch((error) => {
            console.error("Erro na solicitação GET:", error);
        });

        // console.log(response.data)
        // console.log(response.data.favoritos.id)
        if (response.data.usuario.id) {
            response.data.favoritos.forEach((produto) => {
                // console.log('PASSOU FOREATCH CHECK')
                if (produto.produto_favorito == produtoID) {
                    console.log("PASSOU NESSE IF DE CHECK")
                    botao = document.getElementById(button.id)
                    botao.innerHTML = ''

                    const novoIcone = document.createElement("i")
                    novoIcone.classList = "fa-solid fa-bookmark"

                    botao.appendChild(novoIcone)
                }
            })
        }

        button.onclick = async (event) => {
            event.preventDefault();

            if (response.data.usuario.id) {
                const usuario_id = response.data.usuario.id;
                let verifica = false
                let favorito_id = ''
                console.log('VARIAVEIS PASSOU')

                let responseGET = await axios.get(`http://${webDev}/api/favoritar`, {
                    headers: {
                        'X-CSRFToken': csrftoken,
                    },
                });
                // VERIFICA O PRODUTO ATUAL COM FAVORITO
                responseGET.data.favoritos.forEach((produto) => {
                    if (produto.produto_favorito == produtoID) {
                        verifica = true
                        favorito_id = produto.id
                        console.log('PASSOU FOREATCH')
                    }
                })

                // VERIFICA SE TEM FAVORITO PARA O SEGUNDO CLIQUE
                if (verifica) {
                    console.log('PASSOU NO DELETE')
                    await axios.delete(`http://${webDev}/api/favoritar?favorito=${favorito_id}`, {
                        headers: {
                            'X-CSRFToken': csrftoken,
                        }
                    }).then((response) => {
                        console.log('PASSOU RESPONSE DO DELETE')
                        if (response.status === 200) {
                            console.log("Ação bem-sucedida! REMOVEU DO FAVORITO");
                            botao = document.getElementById(button.id)
                            botao.innerHTML = ''

                            const novoIcone = document.createElement("i")
                            novoIcone.classList = "fa-regular fa-bookmark"

                            botao.appendChild(novoIcone)
                        } else {
                            console.log('NÃO PASSOU NO IF')
                        }
                    });

                } else {
                    await axios.post(`http://${webDev}/api/favoritar`, {
                        produto_favorito: produtoID,
                        usuario: usuario_id,
                    }, {
                        headers: {
                            'X-CSRFToken': csrftoken,
                        },
                    }).then((response) => {
                        if (response.status === 201) {
                            // Ação no HTML quando a resposta for um status 202 (Aceito)
                            botao = document.getElementById(button.id)
                            botao.innerHTML = ''

                            const novoIcone = document.createElement("i")
                            novoIcone.classList = "fa-solid fa-bookmark"

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
