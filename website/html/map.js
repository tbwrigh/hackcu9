// create map
const map = L.map('map', {minZoom: 3, maxZoom: 20}).setView([0, 0], 1);

// add base layer
const gl = L.maplibreGL({
  attribution: "\u003ca href=\"https://www.maptiler.com/copyright/\" target=\"_blank\"\u003e\u0026copy; MapTiler\u003c/a\u003e \u003ca href=\"https://www.openstreetmap.org/copyright\" target=\"_blank\"\u003e\u0026copy; OpenStreetMap contributors\u003c/a\u003e",
  style: `https://api.maptiler.com/maps/334b605c-1b46-44ff-895f-4a2324b5cf19/style.json?key=${key}`
}).addTo(map);

// define colors for choropleth
const colors = ['#ffffcc', '#c2e699', '#78c679', '#31a354', '#006837'];

// define function to get color based on data value
function getColor(d) {
  return d > 100000 ? colors[4] :
         d > 50000 ? colors[3] :
         d > 10000 ? colors[2] :
         d > 1000 ? colors[1] :
         colors[0];
}

// define function to style layer
function style(feature) {
  return {
    fillColor: getColor(feature.properties.data),
    weight: 1,
    opacity: 1,
    color: 'white',
    fillOpacity: 0.7
  };
}

// define function to highlight feature on hover
function highlightFeature(e) {
  const layer = e.target;

  layer.setStyle({
    weight: 2,
    color: '#666',
    dashArray: '',
    fillOpacity: 0.7
  });

  if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
    layer.bringToFront();
  }
}

// define function to reset layer style on mouseout
function resetHighlight(e) {
  geojson.resetStyle(e.target);
}

// define function to zoom to feature on click
function zoomToFeature(e) {
  map.fitBounds(e.target.getBounds());
}

// define function to add event listeners to layer
function onEachFeature(feature, layer) {
  layer.on({
    mouseover: highlightFeature,
    mouseout: resetHighlight,
    click: zoomToFeature
  });
}

// load geojson data for countries
const geojson = L.geoJson(null, {
  style: style,
  onEachFeature: onEachFeature
}).addTo(map);

// add data to geojson layer
const countriesData = [
  { name: 'United States', data: 25000 },
  { name: 'Canada', data: 5000 },
  { name: 'Mexico', data: 1000 },
  // add more countries here
];

// loop through countriesData and get polygon coordinates for each country using the countriesDict
for (let i = 0; i < countriesData.length; i++) {
  const countryName = countriesData[i].name;
  const countryData = countriesData[i].data;
  const countryCoords = countriesDict[countryName];

  if (countryCoords) {
    const feature = {
      "type": "Feature",
      "properties": {
        "data": countryData
      },
      "geometry": countryCoords
    };

    geojson.addData(feature);
  }
}