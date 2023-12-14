function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

document.getElementById("formSenha").addEventListener('submit', async (event) => {
    event.preventDefault();

    let csrftoken = getCookie('csrftoken')
    var senhaAtual = document.getElementById('senha-atual').value;
    var novaSenha = document.getElementById('nova-senha').value;

    await axios.post(`/api/mudar_senha?senha_atual=${senhaAtual}&nova_senha=${novaSenha}`, {
        headers: {
            'X-CSRFToken': csrftoken,
        },
    }).then((response) => {
        if (response.status === 200) {
            let div_response = document.getElementById("div-response");

            div_response.innerHTML = `
                <span style="background-color: limegreen; color: aliceblue;">Senha alterada com sucesso!</span>
            `
        } else if (response.status === 400) {
            let div_response = document.getElementById("div-response");

            div_response.innerHTML = `
            <span style="background-color: rgb(252, 74, 34); color: aliceblue;">Senha atual incorreta!</span>
            `
        }
    })
})