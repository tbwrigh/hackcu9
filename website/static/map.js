const key = 'F7ZkKpZLMp1OHNOtKj50';
const map = L.map('map', {minZoom: 3,maxZoom: 15}).setView([15, 0], 1);

const gl = L.maplibreGL({
  attribution: "\u003ca href=\"https://www.maptiler.com/copyright/\" target=\"_blank\"\u003e\u0026copy; MapTiler\u003c/a\u003e \u003ca href=\"https://www.openstreetmap.org/copyright\" target=\"_blank\"\u003e\u0026copy; OpenStreetMap contributors\u003c/a\u003e",
  style: `https://api.maptiler.com/maps/334b605c-1b46-44ff-895f-4a2324b5cf19/style.json?key=${key}`
}).addTo(map);

function getColor(i) {
  return i > 5 ? "#00ff44" : (i > 3 ? "#ff9900" : (i > 0 ? "#66bb00" : (i > -3 ? "#ffff00" : "#ff0000" ))) 
}

fetch('https://raw.githubusercontent.com/python-visualization/folium/11187ff0a83b53b2f833ce4547c4c3f195ddf95c/examples/data/world-countries.json')
  .then(response => response.json())
  .then(data => {
    // Prepare data
    const encoded_data = window.location.search.split("?data=")[1];
    const res_data = atob(encoded_data).split(",");
    const values = {};
    for (let i in res_data) {
      const parts = res_data[i].split("|");
      if (parts[0] == "United States") {
        parts[0] = "United States of America"
      }
      values[parts[0]] = parseInt(parts[1]); 
    }

    // Add values to features
    data.features.forEach(feature => {
      const country = feature.properties.name;
      feature.properties.value = values[country] || 0;
    });

    // Create GeoJSON layer with style function
    const geojsonLayer = L.geoJSON(data, {
      style: function (feature) {
        return {
          fillColor: getColor(feature.properties.value),
          weight: 1,
          opacity: 1,
          color: 'white',
          fillOpacity: 0.7
        };
      }
    }).addTo(map);

    // Add legend
    const legend = L.control({position: 'bottomright'});

    legend.onAdd = function (map) {
      const div = L.DomUtil.create('div', 'info legend');
      const grades = [-10,-3, 0, 3, 5];
      const labels = [];
      let from, to;

      for (let i = 0; i < grades.length; i++) {
        from = grades[i];
        to = grades[i + 1] - 1;
        labels.push(
          '<i style="background:' + getColor(from + 1) + '"></i> ' +
          from + (to ? ' &ndash; ' + to : '+'));
      }

      div.innerHTML = labels.join('<br>');
      return div;
    };

    legend.addTo(map);
  });
