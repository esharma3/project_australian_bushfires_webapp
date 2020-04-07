// Selecting event handlers
const button_17 = d3.select("#aus-17");
const button_18 = d3.select("#aus-18");
const button_19 = d3.select("#aus-19");
const button_20 = d3.select("#aus-20");

// This function will build the Australia Map and display locations of fires
function buildAUSmap(totalData) {

	let trace1 = {
	    lat: totalData.map(e => e.latitude),
        lon: totalData.map(e => e.longitude),
        z: totalData.map(e => e.count),
        hovertemplate: 'Location: (%{lat},%{lon})' + '<br>' + 'Total Fires: %{z} per 11.1km radius',
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
};

// These functions will take the data generated from the html/json route
// plug it into the above function and plot as desired
function init_2017() {

	console.log("hello 2017")

    // Contains the JSON version of data
	d3.json("/aus_fire_map/2017").then((data) => {
		console.log("hello again 2017")
        buildAUSmap(data)
    })
};

function init_2018() {

	console.log("hello 2018")

    // Contains the JSON version of data
	d3.json("/aus_fire_map/2018").then((data) => {
		console.log("hello again 2018")
        buildAUSmap(data)
    })
};

function init_2019() {

	console.log("hello 2019")

    // Contains the JSON version of data
	d3.json("/aus_fire_map/2019").then((data) => {
		console.log("hello again 2019")
        buildAUSmap(data)
    })
};

function init_2020() {

	console.log("hello 2020")

    // Contains the JSON version of data
	d3.json("/aus_fire_map/2020").then((data) => {
		console.log("hello again 2020")
        buildAUSmap(data)
    })
};

init_2019();
button_17.on("click", init_2017);
button_18.on("click", init_2018);
button_19.on("click", init_2019);
button_20.on("click", init_2020);