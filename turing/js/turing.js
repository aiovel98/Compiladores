var estadoActual = "";
var i, longitudW;


function capturar() {
    w = document.getElementById("cadena").value;
    document.getElementById("resultado").innerHTML=("");
    document.getElementById("final").innerHTML=("");
    longitudW = (w.length);
    w = addBL(w);
    w = addBR(w);

    var x = document.getElementById("s");
    x.innerHTML = ("Cadena: " + w);
    w = w.split('');
    estado_q0(w, 1);
}

function addBL(w) {
    /* Recorro el array de derecha a izquierda y desplazo
   * los caracteres una posicion a la derecha */
    for (i = w.length; i > 0; i--) {
        w[i] = w[i - 1];
    }
    /* Concateno la cadena w con un blanco por la izquierda. */
    w = '_' + w;
    return w;
}

function addBR(w) {
    /* Concateno la cadena w con un blanco por la derecha. */
    return w.concat("_");
}

function printLog(w, ea, i, x, m, e) {
    var resultado = document.getElementById("resultado");
    w = w.join('');
    resultado.innerHTML += ("Cadena es:" + w + ", estoy en: " + ea + ", leo: " + w[i] + ", posicion: " + i + ", lo cambio por: " + x + ", me muevo a la: " + m + " y me voy al estado: " + e + "<br>");
}

function estado_q0(w, i) {
    estadoActual = "q0";
    if (w[i] == 'a') {
        if (w[i + 1] == '_') {
            printLog(w, estadoActual, i, 'a', 'R', "q2");
            w[i] = 'a';
            w = estado_q1(w, i += 1);
        } else {
            printLog(w, estadoActual, i, 'a', 'R', "q1");
            w[i] = 'a';
            w = estado_q1(w, i += 1);
        }
    } else if (w[i] == 'b') {
        w = estado_q1(w, i);
    } else if (w[i] == '_') {
        estado_q2(w, i - 1);
    } else {
        var err = "No coincide con el diccionario {a,b}";
        error(err);
    }
    return w;
}
function estado_q1(w, i) {
    estadoActual = "q1";
    if (w[i] == 'b') {
        if (w[i + 1] == '_') {
            printLog(w, estadoActual, i, 'a', 'R', "q2");
            w[i] = 'a';
            w = estado_q0(w, i += 1);
        } else {
            printLog(w, estadoActual, i, 'a', 'R', "q0");
            w[i] = 'a';
            w = estado_q0(w, i += 1);
        }
    } else if (w[i] == 'a') {
        w = estado_q0(w, i);
    } else if (w[i] == '_') {
        estado_q2(w, i - 1);
    } else {
        var err = "No coincide con el diccionario {a,b}";
        error(err);
    }
    return w;
}

function estado_q2(w, i) {
    estadoActual = "q2";
    for (i; i > 0; i--) {
        printLog(w, estadoActual, i, 'a', 'L', "q2");
    }
    var x = document.getElementById("final");
    x.innerHTML = ("<br>Cinta terminada.");
}

function error(x) {
    var y = document.getElementById("resultado");
    y.innerHTML=("Error: " + x + "<br>");
}