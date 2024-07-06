//Para ocultar el mensaje temporal después de 5 segundos
$(document).ready(() => {
  setTimeout(() => {
    document.getElementById("mensaje-temporal").style.display = "none";
  }, 5000);
});