// Selecting event handlers
const button = d3.select("button");
const input = d3.select("input");


// Functions for all visuals
	function animalImpactDonut(obj) {

		// Resetting output
		document.getElementById("donut").innerHTML = "";	
		document.getElementById("roo-img").innerHTML = "";
		document.getElementById("roo-text").innerHTML = "";

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
			title: {
				text:'Affected Habitat %',
				font: {
					family:"Helvetica Neue",
					// BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,Noto Sans,sans-serif
					size: "30px", 
					color: "#999999",
					weight: "light"
					
				}
			},
			margin: {
			"t": 0,
			"b": 0,
			"l": 2,
			"r": 2
		}};

		Plotly.newPlot("donut", plotData, layout)
}

function animalImpactMap(obj) {

	// Resetting output
	document.getElementById("map").innerHTML = "";
	document.getElementById("roo-img").innerHTML = "";
	document.getElementById("roo-text").innerHTML = "";
	d3.select("#map").append("h4").text("Species habitat").attr("align", "center");

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
	
	// Resetting output
	document.getElementById("table").innerHTML = "";
	document.getElementById("roo-img").innerHTML = "";
	document.getElementById("roo-text").innerHTML = "";

	d3.select("#table").append("h4").text("Species deets").attr("align", "center");

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

	let row6 = tbody.append("tr")
	row6.append("td").text("Taxonomy ID:")
	row6.append("td").text(obj['taxon_id'])

}

function concernedRoo() {

	// Resetting output
	document.getElementById("donut").innerHTML = "";
	document.getElementById("map").innerHTML = "";
	document.getElementById("table").innerHTML = "";
	document.getElementById("roo-img").innerHTML = "";
	document.getElementById("roo-text").innerHTML = "";

	d3.select('#roo-img')
	  .append("img")
	  .attr("src", 'https://pngimg.com/uploads/kangaroo/kangaroo_PNG4.png')
	  .attr("width", 350, "height", "auto")
	  .attr("vertical-lign", "center")

	d3.select('#roo-text')
	  .append("h3").text("You lost, mate? try searching again. G'day!")
}

// Handler function
function handleSearchButtonClick(data) {

	// Getting value of user input
	const userInput = input.property("value")

	// Testing user input
	console.log(userInput)
	
	let filteredData = data
	let index = null
	
	// Checks for user input to match common name
	if (isNaN(userInput)) {
		index = filteredData.map(e => e.common_name.toLowerCase()).indexOf(userInput.toLowerCase());
		// Testing index
		console.log(index) 
		if (index === -1) {
			index = filteredData.map(e => e.scientific_name.toLowerCase()).indexOf(userInput.toLowerCase());
		} 
	// checks for user input to match taxonomy id
	} else {
		index = filteredData.map(e => String(e.taxon_id)).indexOf(userInput);
		// Testing index
		console.log(index)
	}

	// This should be an object of that index
	filteredData = filteredData[index]

	// Testing filtered data
	console.log(filteredData)

	if (filteredData != null) {
		animalImpactDonut(filteredData)
		animalImpactMap(filteredData)
		animalImpactTable(filteredData)
	} else {
		concernedRoo()
	}
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