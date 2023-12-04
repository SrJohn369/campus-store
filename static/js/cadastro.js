var cell = document.getElementById('telefone');

cell.addEventListener(
    'input', () => {
        var limparValor = cell.value.replace(/\D/g, "").substring(0, 11);
        var numeroArray = limparValor.split("");
        var numeroFormatado = ""

        if (numeroArray.length > 0) {
            numeroFormatado += `(${numeroArray.slice(0,2).join("")})`;
        }
        if (numeroArray.length > 2) {
            numeroFormatado += ` ${numeroArray.slice(2, 3).join("")} `;
        }
        if (numeroArray.length > 3) {
            numeroFormatado += `${numeroArray.slice(3, 7).join("")}-`;
        }
        if (numeroArray.length > 7) {
            numeroFormatado += `${numeroArray.slice(7, 11).join("")}`;
        }

        cell.value = numeroFormatado;
    }
);