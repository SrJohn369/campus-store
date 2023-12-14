function app() {
    console.log("app iniciado!");
    addFavorito();
    addCarrinho();
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

        const response = await axios.get(`/api/favoritar`, {
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

                    const novoIcone = `
                    <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" fill="currentColor" class="bi bi-heart-fill" viewBox="0 0 16 16">
                        <path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314"/>
                    </svg>
                    `

                    botao.innerHTML = novoIcone
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

                let responseGET = await axios.get(`/api/favoritar`, {
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
                    await axios.delete(`/api/favoritar?favorito=${favorito_id}`, {
                        headers: {
                            'X-CSRFToken': csrftoken,
                        }
                    }).then((response) => {
                        console.log('PASSOU RESPONSE DO DELETE')
                        if (response.status === 200) {
                            // console.log("Ação bem-sucedida! REMOVEU DO FAVORITO");

                            if (window.location.pathname != "/perfil/favoritos") {
                                botao = document.getElementById(button.id)
                                botao.innerHTML = ''

                                const novoIcone = `
                                    <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" fill="currentColor" class="bi bi-heart" viewBox="0 0 16 16">
                                        <path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15"/>
                                    </svg>
                                    `
                                botao.innerHTML = novoIcone
                            } else {
                                const id_card = button.getAttribute("id-card")
                                const card_id = document.getElementById(`card${id_card}`)

                                card_id.remove()
                            }
                            
                        } else {
                            console.log('NÃO PASSOU NO IF')
                        }
                    });

                } else {
                    await axios.post(`/api/favoritar`, {
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

                            const novoIcone = `
                            <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" fill="currentColor" class="bi bi-heart-fill" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314"/>
                            </svg>
                            `

                            botao.innerHTML = novoIcone
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

function addCarrinho() {

    // Suponha que você tenha elementos com os IDs "elemento1", "elemento2", "elemento3", ...
    // Você pode usar um seletor CSS para selecionar todos os elementos que começam com "elemento"
    var buttons = document.querySelectorAll('[id^="add-carrinho"]');

    // PARA CADA BOTÃO
    buttons.forEach(async (button) => {
        // console.log(button); // Debug

        const produtoID = button.getAttribute("data-produto-id");
        // console.log(produtoID)

        const csrftoken = getCookie('csrftoken'); // Substitua 'getCookie' pela função correta para obter cookies

        const response = await axios.get(`/api/carrinho`, {
            headers: {
                'X-CSRFToken': csrftoken,
            },
        }).catch((error) => {
            console.error("Erro na solicitação GET:", error);
        });

        // console.log(response.data)
        console.log(response.data.carrinho)
        if (response.data.usuario.id) {
            response.data.carrinho.forEach((produto) => {
                // console.log('PASSOU FOREATCH CHECK')
                if (produto.produto.id == produtoID) {
                    console.log("PASSOU NESSE IF DE CHECK")
                    botao = document.getElementById(button.id)
                    botao.innerHTML = ''

                    const novoIcone = `
                        <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" fill="currentColor" class="bi bi-cart-check-fill" viewBox="0 0 16 16">
                            <path d="M.5 1a.5.5 0 0 0 0 1h1.11l.401 1.607 1.498 7.985A.5.5 0 0 0 4 12h1a2 2 0 1 0 0 4 2 2 0 0 0 0-4h7a2 2 0 1 0 0 4 2 2 0 0 0 0-4h1a.5.5 0 0 0 .491-.408l1.5-8A.5.5 0 0 0 14.5 3H2.89l-.405-1.621A.5.5 0 0 0 2 1zM6 14a1 1 0 1 1-2 0 1 1 0 0 1 2 0m7 0a1 1 0 1 1-2 0 1 1 0 0 1 2 0m-1.646-7.646-3 3a.5.5 0 0 1-.708 0l-1.5-1.5a.5.5 0 1 1 .708-.708L8 8.293l2.646-2.647a.5.5 0 0 1 .708.708z"/>
                        </svg>`

                    botao.innerHTML = novoIcone
                }
            })
        }

        button.onclick = async (event) => {
            event.preventDefault();

            if (response.data.usuario.id) {
                const usuario_id = response.data.usuario.id;
                let verifica = false
                let carrinho_id = ''
                console.log('VARIAVEIS PASSOU')

                let responseGET = await axios.get(`/api/carrinho`, {
                    headers: {
                        'X-CSRFToken': csrftoken,
                    },
                });
                // VERIFICA O PRODUTO ATUAL COM FAVORITO
                console.log(responseGET.data.carrinho)
                responseGET.data.carrinho.forEach((carrinho) => {
                    if (carrinho.produto.id == produtoID) {
                        verifica = true
                        carrinho_id = carrinho.id
                        console.log('PASSOU FOREATCH')
                    }
                })

                // VERIFICA SE TEM FAVORITO PARA O SEGUNDO CLIQUE
                if (verifica) {
                    console.log('PASSOU NO DELETE')
                    await axios.delete(`/api/carrinho?remove_carrinho=${carrinho_id}`, {
                        headers: {
                            'X-CSRFToken': csrftoken,
                        }
                    }).then((response) => {
                        console.log('PASSOU RESPONSE DO DELETE')
                        if (response.status === 200) {
                            console.log("Ação bem-sucedida! REMOVEU DO carrinho");
                            botao = document.getElementById(button.id)
                            botao.innerHTML = ''

                            const novoIcone = `
                                <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" fill="currentColor" class="bi bi-cart-plus" viewBox="0 0 16 16">
                                    <path d="M9 5.5a.5.5 0 0 0-1 0V7H6.5a.5.5 0 0 0 0 1H8v1.5a.5.5 0 0 0 1 0V8h1.5a.5.5 0 0 0 0-1H9z"/>
                                    <path d="M.5 1a.5.5 0 0 0 0 1h1.11l.401 1.607 1.498 7.985A.5.5 0 0 0 4 12h1a2 2 0 1 0 0 4 2 2 0 0 0 0-4h7a2 2 0 1 0 0 4 2 2 0 0 0 0-4h1a.5.5 0 0 0 .491-.408l1.5-8A.5.5 0 0 0 14.5 3H2.89l-.405-1.621A.5.5 0 0 0 2 1zm3.915 10L3.102 4h10.796l-1.313 7h-8.17zM6 14a1 1 0 1 1-2 0 1 1 0 0 1 2 0m7 0a1 1 0 1 1-2 0 1 1 0 0 1 2 0"/>
                                </svg> `

                            botao.innerHTML = novoIcone
                        } else {
                            console.log('NÃO PASSOU NO IF')
                        }
                    });

                } else {
                    await axios.post(`/api/carrinho`, {
                        produto: produtoID,
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

                            const novoIcone = `
                                <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" fill="currentColor" class="bi bi-cart-check-fill" viewBox="0 0 16 16">
                                    <path d="M.5 1a.5.5 0 0 0 0 1h1.11l.401 1.607 1.498 7.985A.5.5 0 0 0 4 12h1a2 2 0 1 0 0 4 2 2 0 0 0 0-4h7a2 2 0 1 0 0 4 2 2 0 0 0 0-4h1a.5.5 0 0 0 .491-.408l1.5-8A.5.5 0 0 0 14.5 3H2.89l-.405-1.621A.5.5 0 0 0 2 1zM6 14a1 1 0 1 1-2 0 1 1 0 0 1 2 0m7 0a1 1 0 1 1-2 0 1 1 0 0 1 2 0m-1.646-7.646-3 3a.5.5 0 0 1-.708 0l-1.5-1.5a.5.5 0 1 1 .708-.708L8 8.293l2.646-2.647a.5.5 0 0 1 .708.708z"/>
                                </svg>`

                            botao.innerHTML = novoIcone
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
