function main() {
    remover_carrinho();
};

async function salvar_quantidade() {
    const csrftoken = getCookie('csrftoken');
    const response = await axios.get(`/api/carrinho`, {
        headers: {
            'X-CSRFToken': csrftoken,
        },
    }).catch((error) => {
        console.error("Erro na solicitação GET:", error);
    });
}

function remover_carrinho() {
    var buttons = document.querySelectorAll('[id^="btn-remove"]');
    console.log(buttons);

    buttons.forEach(async (botao) => {
        botao.onclick = async (event) => {
            event.preventDefault();

            const carrinho_id = botao.getAttribute("id-carrinho")

            const csrftoken = getCookie('csrftoken');
            await axios.delete(`/api/carrinho?remove_carrinho=${carrinho_id}`, {
                headers: {
                    'X-CSRFToken': csrftoken,
                },
            }).then((response) => {
                if (response.status === 200) {
                    const id_tr_tabela = botao.getAttribute("id-tr-tabela")
                    const id_tr = document.getElementById(`tabela_produto${id_tr_tabela}`)

                    id_tr.remove()
                }
            })
        }
    })
}

async function total() {
    
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

main();