function app() {
    console.log("app iniciado!");
    get_info();
    addFavorito();
}

async function get_info() {
    const csrftoken = getCookie('csrftoken'); // Substitua 'getCookie' pela função correta para obter cookies

    const response = await axios.get("http://localhost:8000/api/favoritar", {
        headers: {
            'X-CSRFToken': csrftoken,
        },
    });

    console.log(response.data);
}

function addFavorito() {
    // Suponha que você tenha elementos com os IDs "elemento1", "elemento2", "elemento3", ...
    // Você pode usar um seletor CSS para selecionar todos os elementos que começam com "elemento"
    var buttons = document.querySelectorAll('[id^="add_favorito"]');

    buttons.forEach((button) => {
        console.log(button); // Debug

        button.onclick = async (event) => {
            event.preventDefault();

            const produtoID = button.getAttribute("data-produto-id");

            const csrftoken = getCookie('csrftoken'); // Substitua 'getCookie' pela função correta para obter cookies

            const response = await axios.get("http://localhost:8000/api/favoritar", {
                headers: {
                    'X-CSRFToken': csrftoken,
                },
            });

            if (response.data.usuario.id) {
                const usuario_id = response.data.usuario.id;

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
                        novoIcone.classList = "fa - solid fa - check"

                        botao.appendChild(novoIcone)

                        console.log("Ação bem-sucedida! Pode adicionar sua lógica aqui.");
                    }
                }).catch((error) => {
                    console.error("Erro na solicitação POST:", error);
                });

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
