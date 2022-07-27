/* DECLARACAO DE FUNCOES JAVASCRIPT PERSONALIZADAS */

$(document).ready(function () {
    /* Fazer fade-in da secção dos conteúdos, ao carregar cada página (a barra <nav> fica intacta) */
    /* Créditos: https://stackoverflow.com/questions/7861150/jquery-fade-in-onload */
    $(".fadeElement").hide(0).fadeIn(1000);

    // Carregar relógio com HH:mm:ss atuais e ir atualizando relogio. Créditos pelo código de base:
    // https://stackoverflow.com/questions/10470825/how-to-make-javascript-time-automatically-update
    function updateTime() {
        let horaAtual = new Date()
        let hours = horaAtual.getHours();
        let minutes = horaAtual.getMinutes();
        let seconds = horaAtual.getSeconds();

        hours = (hours < 10) ? "0" + hours : hours;
        minutes = (minutes < 10) ? "0" + minutes : minutes;
        seconds = (seconds < 10) ? "0" + seconds : seconds;
        document.getElementById('span-horas').innerHTML = hours + ":" + minutes + ":" + seconds;
    }

    setInterval(updateTime, 1000);

    // Se a página contém botões de eliminar, configurar para que o seu onclick solicite confirmacao do user

    let botaoEliminar = document.querySelector('#btnEliminar');
    if (botaoEliminar != null) {
        document.querySelector('#btnEliminar').onclick = () => {
            return confirm('Tem a certeza que pretende eliminar?');
        }
    }
});


