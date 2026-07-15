const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

$("#boton").click(function () {
    alert("El correo fue enviado correctamente");
});

$("#ingredientes-rojo").on("click", function () {
    $(this).css({
        "color": "red"
    });
});


$("#preparacion-rojo").on("click", function () {
    $(this).css({
        "color": "red"
    });
});

$("#activar-toggle-1").on("click", function () {
    $("#toggle-1").toggle("slow", function () {
    });
});

$("#activar-toggle-2").on("click", function () {
    $("#toggle-2").toggle("slow", function () {
    });
});

$("#activar-toggle-3").on("click", function () {
    $("#toggle-3").toggle("slow", function () {
    });
});