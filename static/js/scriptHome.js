let loggedIn = false; // Estado de inicio de sesión

function login() {
    // Aquí puedes agregar la lógica para autenticar al usuario
    // Si la autenticación es exitosa, cambia el estado de inicio de sesión
    loggedIn = true;
    
    // Mostrar el botón de "Cerrar Sesión"
    document.getElementById("logout").style.display = "block";

    // Cerrar el modal
    $('#loginModal').modal('hide');

    return false; // Evitar el envío del formulario para esta demostración
}

function logout() {
    loggedIn = false;
    document.getElementById("logout").style.display = "none";
    alert("Has cerrado sesión");
}
