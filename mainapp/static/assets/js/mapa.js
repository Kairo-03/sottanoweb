document.addEventListener("DOMContentLoaded", function () {
    var mymap = L.map('map').setView([TU_LATITUD, TU_LONGITUD], 13); // Reemplaza TU_LATITUD y TU_LONGITUD con las coordenadas de tu ubicación
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(mymap);

    // Agrega un marcador en la ubicación especificada
    var marker = L.marker([TU_LATITUD, TU_LONGITUD]).addTo(mymap);
    marker.bindPopup("¡Hola! Esta es tu ubicación.").openPopup();
});