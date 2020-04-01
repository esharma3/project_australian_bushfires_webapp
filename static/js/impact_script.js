// Selecting event handlers
const button = d3.select("button");
const input = d3.select("input");

// Functions for all visuals
	function animalImpactDonut(obj) {
		let plotData = [{
			type: "pie",
			hole: .8,
			values: [ obj['area_max'], 100 - obj['area_max'] ],
			labels: ["Impacted Area", "Safe Area"],
			textinfo: "label+percent",
			textposition: "outside",
			automargin: true,
			marker: {
				colors: ["red", "rain blue"]
			}
		}];

		let layout = {
			height: 400,
			width: 400,
			margin: {
			"t": 0,
			"b": 0,
			"l": 2,
			"r": 2
		}};

		Plotly.newPlot("donut", plotData, layout)
}

function animalImpactMap(obj) {
	d3.select("#map")
		.append("iframe")
		.attr("src", obj['distribution_map'])
		.attr("width", 400)
		.attr("height", 400)
		.attr("frameborder", 0)
		.attr('style', 'border:0')
		.attr('allowfullscreen', '')
		.attr('scrolling', 'no')
}

function animalImpactTable(obj) {

	// Getting my variables ready
	const table = d3.select("#table")
	table.classed("table table-hover", true)
	var thead = table.append('thead')
	var	tbody = table.append('tbody')
		
	// table body
	let row1 = tbody.append("tr")
	row1.append("td").text("Thumbnail:")
	row1.append("td").append('img').attr('src', obj['thumbnail'])

	let row2 = tbody.append("tr")
	row2.append("td").text("Common Name:")
	row2.append("td").text(obj['common_name'])

	let row3 = tbody.append("tr")
	row3.append("td").text("Scientific Name:")
	row3.append("td").text(obj['scientific_name'])

	let row4 = tbody.append("tr")
	row4.append("td").text("Type:")
	row4.append("td").text(obj['type'])

	let row5 = tbody.append("tr")
	row5.append("td").text("Protected Status:")
	row5.append("td").text(obj['protected_status'])

}

// Handler function
function handleSearchButtonClick(data) {

	// Getting value of user input
	const userInput = input.property("value")

	// Testing user input
	console.log(userInput)
	
	let filteredData = data
	let index = null
	
	if (userInput) {
		index = filteredData.map(e => e.common_name.toLowerCase()).indexOf(userInput.toLowerCase());
		// Testing index
		console.log(index)
	}
	else {
		filteredData = null 
	}

	// This should be an object of that index
	filteredData = filteredData[index]

	// Testing filtered data
	console.log(filteredData)

	animalImpactDonut(filteredData)
	animalImpactMap(filteredData)
	animalImpactTable(filteredData)
}

// Init function to load promise and pass the data to handleSearchButtonClick
function init() {
	d3.json("/impact-data").then((data) => {
		// see if data is loading
		console.log(data)
		handleSearchButtonClick(data);
		})
}

button.on("click", init);
input.on("change", init);