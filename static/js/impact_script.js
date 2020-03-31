const input = d3.select("input")
const button = d3.select("button")

let userInput = input.property("value")

// if (userInput === data.includes(userInput))

function buildGraphics() {
	d3.json("/impact-data").then((data) => {

		function animalImpactDonut(data) {
			let plotData = [{
				type: "pie",
				hole: .8,
				values: [ data.filter(e => e.area_max), 100 - data.filter(e => e.area_max) ],
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
	
		function animalImpactMap(data) {
			d3.select("#map")
				.append("iframe")
				.attr("src", data.filter(e => e.distribution_map))
				.attr("width", 400)
				.attr("height", 400)
				.attr("frameborder", 0)
				.attr('style', 'border:0')
				.attr('allowfullscreen', '')
				.attr('scrolling', 'no')
		}
	
		function animalImpactTable(data) {
	
			// Getting my variables ready
			const table = d3.select("#table")
			table.classed("table table-hover", true)
			var thead = table.append('thead')
			var	tbody = table.append('tbody')
	
			// table hear
			thead.append('tr')
			.selectAll('th')
			.text("This is a header")
			thead.append('tr')
				.selectAll('th')
				.text("This is another header")
			
			let row1 = tbody.append("tr")
			row1.append("td").text("Thumbnail:")
			row1.append("td").append('img').attr('src', data.filter(e => e.thumbnail))
	
			let row2 = tbody.append("tr")
			row2.append("td").text("Common Name:")
			row2.append("td").text(data.filter(e => e.common_name))
	
			let row3 = tbody.append("tr")
			row3.append("td").text("Scientific Name:")
			row3.append("td").text(data.filter(e => e.scientific_name))
	
			let row4 = tbody.append("tr")
			row4.append("td").text("Type:")
			row4.append("td").text(data.filter(e => e.type))
	
			let row5 = tbody.append("tr")
			row5.append("td").text("Protected Status:")
			row5.append("td").text(data.filter(e => e.protected_status))
	
		}
	})
	animalImpactDonut();
	animalImpactMap();
	animalImpactTable();
}


function init() {
	d3.json("/impact-data").then((data) => {
		if (userInput === data.map(e => e.common_name) ) {
			console.log(data)
			input.on("change", buildGraphics());
			button.on("click", buildGraphics());
		}
	})
}

init();