// This function will build the Australia Map and display locations of fires
function buildAUSmap(totalData) {

	let trace1 = {
	    lat: totalData.map(e => e.latitude),
        lon: totalData.map(e => e.longitude),
        z: totalData.map(e => e.count),
        hovertemplate: 'Location: (%{lat},%{lon})' + '<br>' + 'Number of Fires: %{count}',
	    type: "densitymapbox"
    };

    let plotData = [trace1]

    let layout = {
        hovermode:'closest',
        dragmode: "zoom",      
        mapbox: {
            style: 'stamen-terrain',
            center: { lat: -24.2, lon: 135 },
            zoom: 3
        },
        margin: { r: 0, t: 60, b: 0, l: 120 }
    };

    Plotly.newPlot("plot", plotData, layout)
}

// This function will take the data generated from the html route
// plug it into the above function and plot as desired
function init() {

	console.log("hello")

    // Contains the JSON version of data
	d3.json("/aus_fire_map").then((data) => {

		console.log("hello again")
        buildAUSmap(data)
    })

}

init();