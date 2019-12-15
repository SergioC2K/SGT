function soloLetras(e) {
    key = e.keyCode || e.which;
    tecla = String.fromCharCode(key).toLowerCase();
    letras = " áéíóúabcdefghijklmnñopqrstuvwxyz";
    especiales = "8-37-39-46";

    tecla_especial = false
    for (var i in especiales) {
        if (key == especiales[i]) {
            tecla_especial = true;
            break;
        }
    }

    if (letras.indexOf(tecla) == -1 && !tecla_especial) {
        //document.getElementById('respuesta').innerHTML = "Solo se permiten letras";
        return false;
    } else {
        document.getElementById('respuesta').innerHTML = "";
    }

}

function soloNumeros(e) {
    key = e.keyCode || e.which;
    tecla = String.fromCharCode(key).toLowerCase();
    letras = " 12345678901234554575668514664211243";
    especiales = "8-37-39-46";

    tecla_especial = false
    for (var i in especiales) {
        if (key == especiales[i]) {
            tecla_especial = true;
            break;
        }
    }

    if (letras.indexOf(tecla) == -1 && !tecla_especial) {
        //  document.getElementById('otro').innerHTML = "Solo se permiten numeros";
        return false;
    } else {
        document.getElementById('otro').innerHTML = "";
    }
}

function Registrar() {
    var cedula = "", first_name = "", last_name = "", username = "", telefono_fijo = "", email = "", celular = "",
        celular_telemercadeo, cargo = "", password = "", cedula_confirmacion = "";

    cedula = document.getElementById('cedula').value;
    first_name = document.getElementById('first_name').value;
    last_name = document.getElementById('last_name').value;
    username = document.getElementById('username').value;
    telefono_fijo = document.getElementById('telefono_fijo').value;
    email = document.getElementById('email').value;
    celular = document.getElementById('celular').value;
    celular_telemercadeo = document.getElementById('celular_telemercadeo').value;
    cargo = document.getElementById('cargo').value;
    password = document.getElementById('password').value;
    cedula_confirmacion = document.getElementById('cedula_confirmacion').value;

    if (cedula != "" && first_name != "" && last_name != "" && username != "" && telefono_fijo != "" && email != "" && celular != ""
        && celular_telemercadeo != "" && cargo != "" && password != "" && cedula_confirmacion != "") {

       alert('registro exitoso');
    } else {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Something went wrong!',
            footer: '<a href>Why do I have this issue?</a>'
        })
    }

}