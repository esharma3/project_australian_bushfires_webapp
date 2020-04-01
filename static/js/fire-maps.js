// This function will build the Australia Map and display locations of fires
function buildAUSmap(totalData) {

	let trace1 = {
	    lat: totalData.map(e => e.latitude),
        lon: totalData.map(e => e.longitude),
        hovertemplate: 'Location: (%{lat},%{lon})' + '<br>' +
        'Brightness: %{text}' + '<br>', 
	    type: "scattermapbox",
	   	marker: {color: "red", size: 7}
	};

    let plotData = [trace1]

    let layout = {
        hovermode:'closest',
        dragmode: "zoom",      
        mapbox: {
            style: "white-bg",
            layers: [
                {
                    sourcetype: "raster",
                    source: ["https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"],
                    below: "traces"
                }
            ],
            center: { lat: -24.2, lon: 135 },
            zoom: 3
        },
        hoverlabel: {
            bgcolor: "black",
            bordercolor: "black",
            font: {color: 'white'}
        },
        margin: { r: 0, t: 0, b: 0, l: 0 }
    };

    Plotly.newPlot("plot", plotData, layout)
}

// This function will take the data generated from the html route
// plug it into the above function and plot as desired
function init() {

	console.log("hello")

    // Contains the JSON version of data
	d3.json("/aus_fire_history").then((data) => {

		console.log("hello again")
        buildAUSmap(data)
    })

}

init();