// Função para verificar a largura da tela e adicionar HTML se for menor que 576 pixels
function moverHTML() {

    // Verifique se o elemento alvo existe
    var elementoAlvo = document.getElementById('redimencionar');

    // Verifique se o elemento alvo existe
    var elementoAlvo2 = document.getElementById('redimencionar2');

    // Barra de Pesquisa
    var barraDePesquisa = document.getElementById('redimencionar3');

    var burgerPesquisa = document.getElementById('redimencionarBarrapesquisa');

    // Header 
    var headerFather = document.getElementById('headerFather');

    // Nova Nav
    var novaNav = document.getElementById('redimencionar4');

    // se MENOR - Elementos de link
    if (window.innerWidth < 576) {
        if (elementoAlvo2) {
            elementoAlvo2.remove();
        }
        if (novaNav) {
            novaNav.remove();
        }
        if (barraDePesquisa) {
            barraDePesquisa.remove()
        }

        if (elementoAlvo && elementoAlvo.innerHTML.trim() === '') {
            
                // Crie o HTML que deseja adicionar
            var novoHTML = `
                <a href="${perfilURL}" class="nav-link">Login/Cadastro</a>
                <a href = "${carrinhoURL}" class="nav-link">Carinho</a>`;

                // Adicione o novo HTML ao elemento alvo
                elementoAlvo.innerHTML += novoHTML;
        } else if (!elementoAlvo) {
            var novoElemento = document.createElement('div');
            novoElemento.id = 'redimencionar';
            var elementoPai = document.getElementById('navPai');
            var elementoAntes = document.getElementById('divAcima');

            elementoPai.insertBefore(novoElemento, elementoAntes);
        }
        if (burgerPesquisa && burgerPesquisa.innerHTML.trim() === "") {
            var novoHTML = '\
            <form action="" class="d-flex m-auto" id="barraPesquisa">\
                <div class="input-group">\
                    <input type="search" name="" id="" class="form-control form-control-sm rounded-pill ps-3 pe-0" placeholder="Pesquisar...">\
                        <button type="submit" class="input-group-text border-0 bg-transparent">\
                            <i class="fas fa-search lupa"></i>\
                        </button>\
                    </div>\
            </form > ';
            burgerPesquisa.innerHTML += novoHTML;
        } else if (!burgerPesquisa) {
            var burgerPesquisa = document.createElement('div');
            burgerPesquisa.id = 'redimencionarBarrapesquisa';

            var divAcimaBarrapesquisa = document.getElementById('divAcimaBarrapesquisa');
            var navPai = document.getElementById('navPai');
            navPai.insertBefore(burgerPesquisa, divAcimaBarrapesquisa);
        }
        // se MAIOR
    } else if (window.innerWidth > 576) {
        if (elementoAlvo) {
            elementoAlvo.remove();
        }
        if (burgerPesquisa) {
            burgerPesquisa.remove();
        }
        

        if (elementoAlvo2 && elementoAlvo2.innerHTML.trim() === '') {
            // Crie o HTML que deseja adicionar
            var novoHTML = `
            <div class="navbar-nav me-auto">
                <a href="${perfilURL}" class="nav-link">
                    <i class="fas fa-user-circle"></i>
                </a>
                <a href="${carrinhoURL}" class="nav-link">
                    <i class="fas fa-shopping-cart"></i>
                </a>
            </div>` ;

            // Adicione o novo HTML ao elemento alvo
            elementoAlvo2.innerHTML += novoHTML;
        } else if (!elementoAlvo2) {
            // criar o elemento
            var novoElemento2 = document.createElement('div');
            novoElemento2.id = 'redimencionar2';
            novoElemento2.classList = 'collapse navbar-collapse m-auto'
            var elementoPai2 = document.getElementById('divPaiNav');
            var elementoAntes2 = document.getElementById('divAcimaNavPai');

            elementoPai2.insertBefore(novoElemento2, elementoAntes2);
        }
        // Para barra de Pesquisa
    }
    if (window.innerWidth > 576 && window.innerWidth < 991) {
        if (barraDePesquisa) {
            barraDePesquisa.remove()
        }
        if (burgerPesquisa) {
            burgerPesquisa.remove();
        }
        if (novaNav && novaNav.innerHTML.trim() === '') {
            var novoHTML = '\
            <nav class="navbar navbar-expand-sm navbarBg" id="redimencionar4">\
                <form action="" class="d-flex m-auto" id="barraPesquisa">\
                    <div class="input-group">\
                        <input type="search" name="" id="" class="form-control form-control-sm rounded-pill ps-3 pe-0" placeholder="Pesquisar...">\
                            <button type="submit" class="input-group-text border-0 bg-transparent">\
                                <i class="fas fa-search lupa"></i>\
                            </button>\
                        </div>\
                </form > \
            </nav >';

            // Adicione o novo HTML ao elemento alvo
            novaNav.innerHTML += novoHTML;

        } else if (!novaNav) {
            console.log("Passou no ELSE IF");
            var novaNav = document.createElement('nav');

            novaNav.id = 'redimencionar4';

            var navAcima = document.getElementById('navAcima');

            headerFather.insertBefore(novaNav, navAcima);
        }
    } else if (window.innerWidth > 991){
        if (novaNav) {
            novaNav.remove();
        }
        if (barraDePesquisa && barraDePesquisa.innerHTML.trim() === '') {
            var novoHTML = '\
                <form action="" class="d-flex m-auto" id="barraPesquisa">\
                    <div class="input-group">\
                        <input type="search" name="" id="" class="form-control form-control-sm rounded-pill ps-3 pe-0" placeholder="Pesquisar...">\
                            <button type="submit" class="input-group-text border-0 bg-transparent">\
                                <i class="fas fa-search lupa"></i>\
                            </button>\
                        </div>\
                </form > ' ;
            // Adicione o novo HTML ao elemento alvo
            barraDePesquisa.innerHTML += novoHTML;

        } else if (!barraDePesquisa) {
            var barraDePesquisa = document.createElement('div');

            barraDePesquisa.id = 'redimencionar3';

            var navAcima = document.getElementById('navAcima3');

            headerFather.insertBefore(novaNav, navAcima);
        }
    }
} 

// Adicione um ouvinte de evento para verificar a largura da tela quando a página é carregada e redimensionada
window.addEventListener('load', moverHTML);
window.addEventListener('resize', moverHTML);
