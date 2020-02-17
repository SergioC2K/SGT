var cajas = [];
const notaEntrega = [];
var llamadasRest = document.getElementById("cant_ll").innerHTML;
document.getElementById("llam_res").innerHTML = llamadasRest;
var usuarioPK;
var primary = [];
var daticos;


function llamadasSelecionadas() {
    cajas = selectable.getSelectedNodes();
    for (let i = 0; i < cajas.length; i++) {
        console.log(cajas[i].innerText);
        notaEntrega.push(cajas[i].childNodes[3].innerText);
    }
    daticos = notaEntrega;
    return daticos
}

function usuarioSeleccionado() {
    usuarioPK = document.getElementById('activo').childNodes[1].innerHTML;
    return usuarioPK
}

function cajas_llamadas(entrega, primary) {
    return (`<p class="nota">${entrega}</p><p hidden>${primary}</p>`)
}

function cajas_retorno(entrega, primary) {
    for (let i = 0; i < datos.length; i++) {
        var array = {};
        array.push(cajas_llamadas(entrega[i], primary[i]))
    }
    return array
}

const llamadasRecibidas = [];
$("#clickes").click(function () {
    var llamadas = llamadasSelecionadas();
    var usuarioPK = usuarioSeleccionado();
    $.ajax({
        url: urlCompleta, //TODO cambiar la url cuando ya este en produccion
        data: {
            'operador': usuarioPK,
            'llamadas': llamadas
        },
        dataType: 'json',
        success: function (data) {
            location.reload();
        },
        error: function (data) {
            alert("Ha ocurrido un error. verifique los datos enviados " + data)
        }
    });
});

document.body.addEventListener('keyup', function (e) {
    if (e.key === "D" || e.key === "d") {
        var items = document.querySelectorAll('.ui-selected');
        selectable.deselect([items])
    }
});

function unaFuncion() {
    setTimeout(function () {
            const llamadas = document.getElementsByClassName("ui-selected").length;
            document.getElementById("conteo").innerHTML = llamadas;
            var cantidadLlamadas = parseInt(document.getElementById("cant_ll").innerHTML);
            var llamadasSeleccionadas = parseInt(document.getElementById("conteo").innerHTML);
            var llamadasResastantes = cantidadLlamadas - llamadasSeleccionadas;
            var divisionUsuarios = parseInt(document.getElementsByClassName("chat_people").length) - 1;
            document.getElementById("llam_res").innerHTML = llamadasResastantes.toString();
            var restante = parseInt(document.getElementById("llam_res").innerHTML);
            var llamadasDivision = ~~(restante / divisionUsuarios);
            document.getElementById("division").innerHTML = llamadasDivision.toString();
        },
        100)
}


$(".chat_people").hover(
    function () {
        $(this).addClass('activo');

    }, function () {
        if (!$(this).hasClass('clicked')) {
            $(this).removeClass('activo');
        }
    }
);

$(".chat_people").click(function (e) {
    e.preventDefault();
    e.stopPropagation;
    $('.clicked:not(:hover)').removeClass('clicked activo');
    $(this).addClass('clicked');
    $(this).attr("id", "activo");
});

