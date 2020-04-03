function buildNswTotalPlot(totalData) {

	console.log(totalData)

	const values = totalData.map(e => e.nsw_total_fires)
	const sortedValues = values.sort((x, y) => y - x)
	let max = sortedValues[0]

	let trace1 = {

		x: totalData.map(e => e.nsw_fire_year),
		y: totalData.map(e => e.nsw_total_fires),
		width: 0.5,
		name: "2002/2003",
		type: "bar",
		marker: {}
	};

	trace1.marker.color = trace1.y.map(function (v) {
		return v === max ? "orange" : "grey"
	});

	let plotData = [trace1]

	let layout = {
		margin: {
			t: 30,
			b: 100
		},
		yaxis: {
			title: "Number of Fires"
		},
		autosize: true
	}

	Plotly.newPlot("first", plotData, layout)

};


function buildQueenslandTotalPlot(totalData) {

	const values = totalData.map(e => e.queensland_total_fires)
	const sortedValues = values.sort((x, y) => y - x)
	let max = sortedValues[0]

	let trace1 = {
		x: totalData.map(e => e.queensland_fire_year),
		y: totalData.map(e => e.queensland_total_fires),
		width: 0.5,
		name: "2002/2003",
		type: "bar",
		marker: {}
	};

	trace1.marker.color = trace1.y.map(function (v) {
		return v === max ? "orange" : "grey"
	});

	let plotData = [trace1]

	let layout = {
		margin: {
			t: 30,
			b: 100
		},
		yaxis: {
			title: "Number of Fires"
		},
		autosize: true
	};

	Plotly.newPlot("second", plotData, layout)

};


function buildVictoriaTotalPlot(totalData) {

	const values = totalData.map(e => e.victoria_total_fires)
	const sortedValues = values.sort((x, y) => y - x)
	let max = sortedValues[0]

	let trace1 = {
		x: totalData.map(e => e.victoria_fire_year),
		y: totalData.map(e => e.victoria_total_fires),
		width: 0.5,
		name: "2002/2003",
		type: "bar",
		marker: {}
	};

	trace1.marker.color = trace1.y.map(function (v) {
		return v === max ? "orange" : "grey"
	});

	let plotData = [trace1]

	let layout = {
		margin: {
			t: 30,
			b: 100
		},
		yaxis: {
			title: "Number of Fires"
		},
		autosize: true
	};

	Plotly.newPlot("third", plotData, layout)

};


function buildStateStatisticsPlot(totalData) {

	let trace1 = {
		values: [totalData[17]["nsw_total_fires"], totalData[35]["queensland_total_fires"], totalData[53]["victoria_total_fires"]],
		labels: ["New South Wales", "Queensland", "Victoria"],
		textinfo: "label+percent+value",
		type: "pie",
		marker: {
			colors: [
				"rgb(71, 71, 107)",
				"rgb(133, 133, 173)",
				"rgb(179, 179, 204)",
			]
		}
	};

	let plotData = [trace1]

	let layout = {
		hovermode: false,
		showlegend: false,
		autosize: true
	};

	Plotly.newPlot("fourth", plotData, layout)

};


function buildTotalFirePlot(totalData) {

	const nswDataList = totalData.slice(0, 18)
	const nswListLength = Object.keys(nswDataList).length

	const queenslandDataList = totalData.slice(18, 36)
	const queenslandListLength = Object.keys(queenslandDataList).length

	const victoriaDataList = totalData.slice(36, 54)
	const victoriaLength = Object.keys(victoriaDataList).length

	let nswTotal = 0
	for (let i = 0; i < nswListLength; i++) {
		nswTotal += nswDataList[i]["nsw_total_fires"]
	};

	let queenslandTotal = 0
	for (let i = 0; i < queenslandListLength; i++) {
		queenslandTotal += queenslandDataList[i]["queensland_total_fires"]
	};

	let victoriaTotal = 0
	for (let i = 0; i < victoriaLength; i++) {
		victoriaTotal += victoriaDataList[i]["victoria_total_fires"]
	};

	let trace1 = {
		values: [nswTotal],
		labels: ["New South Wales"],
		textinfo: "label+value",
		type: "pie",
		marker: {
			colors: [
				"rgb(82, 82, 122)"
			]
		},
		domain: {
			row: 0,
			column: 0
		},
	};

	let trace2 = {
		values: [queenslandTotal],
		labels: ["Queensland"],
		textinfo: "label+value",
		type: "pie",
		marker: {
			colors: [
				"rgb(41, 41, 61)"
			]
		},
		domain: {
			row: 0,
			column: 1
		},
	};

	let trace3 = {
		values: [victoriaTotal],
		labels: ["Victoria"],
		textinfo: "label+value",
		type: "pie",
		marker: {
			colors: [
				"rgb(148, 148, 184)"
			]
		},
		domain: {
			row: 0,
			column: 2
		},
	};

	let plotData = [trace1, trace2, trace3]

	let layout = {
		showlegend: false,
		hovermode: false,
		grid: {
			rows: 1,
			columns: 3
		},
		autosize: true
	};

	Plotly.newPlot("fifth", plotData, layout)

};


function buildNswPlot(data) {

	let trace1 = {
		x: data.map(e => e.nsw_DOY),
		y: data.map(e => e.nsw_2002_2003),
		name: "2002/2003",
		type: "scatter"
	};
	let trace2 = {
		x: data.map(e => e.nsw_DOY),
		y: data.map(e => e.nsw_2003_2004),
		name: "2003/2004",
		type: "scatter"
	};
	let trace3 = {
		x: data.map(e => e.nsw_DOY),
		y: data.map(e => e.nsw_2004_2005),
		name: "2004/2005",
		type: "scatter"
	};
	let trace4 = {
		x: data.map(e => e.nsw_DOY),
		y: data.map(e => e.nsw_2005_2006),
		name: "2005/2006",
		type: "scatter"
	};
	let trace5 = {
		x: data.map(e => e.nsw_DOY),
		y: data.map(e => e.nsw_2006_2007),
		name: "2006/2007",
		type: "scatter"
	};
	let trace6 = {
		x: data.map(e => e.nsw_DOY),
		y: data.map(e => e.nsw_2007_2008),
		name: "2007/2008",
		type: "scatter"
	};
	let trace7 = {
		x: data.map(e => e.nsw_DOY),
		y: data.map(e => e.nsw_2008_2009),
		name: "2008/2009",
		type: "scatter"
	};
	let trace8 = {
		x: data.map(e => e.nsw_DOY),
		y: data.map(e => e.nsw_2009_2010),
		name: "2009/2010",
		type: "scatter"
	};
	let trace9 = {
		x: data.map(e => e.nsw_DOY),
		y: data.map(e => e.nsw_2010_2011),
		name: "2010/2011",
		type: "scatter"
	};
	let trace10 = {
		x: data.map(e => e.nsw_DOY),
		y: data.map(e => e.nsw_2011_2012),
		name: "2011/2012",
		type: "scatter"
	};
	let trace11 = {
		x: data.map(e => e.nsw_DOY),
		y: data.map(e => e.nsw_2012_2013),
		name: "2012/2013",
		type: "scatter"
	};
	let trace12 = {
		x: data.map(e => e.nsw_DOY),
		y: data.map(e => e.nsw_2013_2014),
		name: "2013/2014",
		type: "scatter"
	};
	let trace13 = {
		x: data.map(e => e.nsw_DOY),
		y: data.map(e => e.nsw_2014_2015),
		name: "2014/2015",
		type: "scatter"
	};
	let trace14 = {
		x: data.map(e => e.nsw_DOY),
		y: data.map(e => e.nsw_2015_2016),
		name: "2015/2016",
		type: "scatter"
	};
	let trace15 = {
		x: data.map(e => e.nsw_DOY),
		y: data.map(e => e.nsw_2016_2017),
		name: "2016/2017",
		type: "scatter"
	};
	let trace16 = {
		x: data.map(e => e.nsw_DOY),
		y: data.map(e => e.nsw_2017_2018),
		name: "2017/2018",
		type: "scatter"
	};
	let trace17 = {
		x: data.map(e => e.nsw_DOY),
		y: data.map(e => e.nsw_2018_2019),
		name: "2018/2019",
		type: "scatter"
	};
	let trace18 = {
		x: data.map(e => e.nsw_DOY),
		y: data.map(e => e.nsw_2019_2020),
		name: "2019/2020",
		type: "scatter"
	};

	let plotData = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10, trace11, trace12, trace13, trace14, trace15, trace16, trace17, trace18]

	let layout = {
		margin: {
			t: 30,
			b: 100
		},
		xaxis: {
			title: "Fire Year running from July 1st to June 30th in the following year",
			tickvals: [1, 32, 63, 93, 124, 154, 185, 216, 244, 275, 305, 336],
			ticktext: ["Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar", "Apr", "May", "Jun"],
		},
		yaxis: {
			title: "Number of Fires"
		},
		autosize: true
	};

	Plotly.newPlot("seventh", plotData, layout)

};


function buildQueenslandPlot(data) {

	let months = ["Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar", "Apr", "May", "Jun"]

	let trace1 = {
		x: data.map(e => e.queensland_DOY),
		y: data.map(e => e.queensland_2002_2003),
		name: "2002/2003",
		type: "scatter"
	};
	let trace2 = {
		x: data.map(e => e.queensland_DOY),
		y: data.map(e => e.queensland_2003_2004),
		name: "2003/2004",
		type: "scatter"
	};
	let trace3 = {
		x: data.map(e => e.queensland_DOY),
		y: data.map(e => e.queensland_2004_2005),
		name: "2004/2005",
		type: "scatter"
	};
	let trace4 = {
		x: data.map(e => e.queensland_DOY),
		y: data.map(e => e.queensland_2005_2006),
		name: "2005/2006",
		type: "scatter"
	};
	let trace5 = {
		x: data.map(e => e.queensland_DOY),
		y: data.map(e => e.queensland_2006_2007),
		name: "2006/2007",
		type: "scatter"
	};
	let trace6 = {
		x: data.map(e => e.queensland_DOY),
		y: data.map(e => e.queensland_2007_2008),
		name: "2007/2008",
		type: "scatter"
	};
	let trace7 = {
		x: data.map(e => e.queensland_DOY),
		y: data.map(e => e.queensland_2008_2009),
		name: "2008/2009",
		type: "scatter"
	};
	let trace8 = {
		x: data.map(e => e.queensland_DOY),
		y: data.map(e => e.queensland_2009_2010),
		name: "2009/2010",
		type: "scatter"
	};
	let trace9 = {
		x: data.map(e => e.queensland_DOY),
		y: data.map(e => e.queensland_2010_2011),
		name: "2010/2011",
		type: "scatter"
	};
	let trace10 = {
		x: data.map(e => e.queensland_DOY),
		y: data.map(e => e.queensland_2011_2012),
		name: "2011/2012",
		type: 'scatter'
	};
	let trace11 = {
		x: data.map(e => e.queensland_DOY),
		y: data.map(e => e.queensland_2012_2013),
		name: "2012/2013",
		type: "scatter"
	};
	let trace12 = {
		x: data.map(e => e.queensland_DOY),
		y: data.map(e => e.queensland_2013_2014),
		name: "2013/2014",
		type: "scatter"
	};
	let trace13 = {
		x: data.map(e => e.queensland_DOY),
		y: data.map(e => e.queensland_2014_2015),
		name: "2014/2015",
		type: "scatter"
	};
	let trace14 = {
		x: data.map(e => e.queensland_DOY),
		y: data.map(e => e.queensland_2015_2016),
		name: "2015/2016",
		type: "scatter"
	};
	let trace15 = {
		x: data.map(e => e.queensland_DOY),
		y: data.map(e => e.queensland_2016_2017),
		name: "2016/2017",
		type: "scatter"
	};
	let trace16 = {
		x: data.map(e => e.queensland_DOY),
		y: data.map(e => e.queensland_2017_2018),
		name: "2017/2018",
		type: "scatter"
	};
	let trace17 = {
		x: data.map(e => e.queensland_DOY),
		y: data.map(e => e.queensland_2018_2019),
		name: "2018/2019",
		type: "scatter"
	};
	let trace18 = {
		x: data.map(e => e.queensland_DOY),
		y: data.map(e => e.queensland_2019_2020),
		name: "2019/2020",
		type: "scatter"
	};


	let plotData = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10, trace11, trace12, trace13, trace14, trace15, trace16, trace17, trace18]

	let layout = {
		margin: {
			t: 30,
			b: 100
		},
		xaxis: {
			title: "Fire Year running from July 1st to June 30th in the following year",
			tickvals: [1, 32, 63, 93, 124, 154, 185, 216, 244, 275, 305, 336],
			ticktext: ["Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar", "Apr", "May", "Jun"],
		},
		yaxis: {
			title: "Number of Fires"
		},
		autosize: true
	};

	Plotly.newPlot("eighth", plotData, layout)

};


function buildVictoriaPlot(data) {

	let trace1 = {
		x: data.map(e => e.victoria_DOY),
		y: data.map(e => e.victoria_2002_2003),
		name: "2002/2003",
		type: "scatter"
	};
	let trace2 = {
		x: data.map(e => e.victoria_DOY),
		y: data.map(e => e.victoria_2003_2004),
		name: "2003/2004",
		type: "scatter"
	};
	let trace3 = {
		x: data.map(e => e.victoria_DOY),
		y: data.map(e => e.victoria_2004_2005),
		name: "2004/2005",
		type: "scatter"
	};
	let trace4 = {
		x: data.map(e => e.victoria_DOY),
		y: data.map(e => e.victoria_2005_2006),
		name: "2005/2006",
		type: "scatter"
	};
	let trace5 = {
		x: data.map(e => e.victoria_DOY),
		y: data.map(e => e.victoria_2006_2007),
		name: "2006/2007",
		type: "scatter"
	};
	let trace6 = {
		x: data.map(e => e.victoria_DOY),
		y: data.map(e => e.victoria_2007_2008),
		name: "2007/2008",
		type: "scatter"
	};
	let trace7 = {
		x: data.map(e => e.victoria_DOY),
		y: data.map(e => e.victoria_2008_2009),
		name: "2008/2009",
		type: "scatter"
	};
	let trace8 = {
		x: data.map(e => e.victoria_DOY),
		y: data.map(e => e.victoria_2009_2010),
		name: "2009/2010",
		type: "scatter"
	};
	let trace9 = {
		x: data.map(e => e.victoria_DOY),
		y: data.map(e => e.victoria_2010_2011),
		name: "2010/2011",
		type: "scatter"
	};
	let trace10 = {
		x: data.map(e => e.victoria_DOY),
		y: data.map(e => e.victoria_2011_2012),
		name: "2011/2012",
		type: "scatter"
	};
	let trace11 = {
		x: data.map(e => e.victoria_DOY),
		y: data.map(e => e.victoria_2012_2013),
		name: "2012/2013",
		type: "scatter"
	};
	let trace12 = {
		x: data.map(e => e.victoria_DOY),
		y: data.map(e => e.victoria_2013_2014),
		name: "2013/2014",
		type: "scatter"
	};
	let trace13 = {
		x: data.map(e => e.victoria_DOY),
		y: data.map(e => e.victoria_2014_2015),
		name: "2014/2015",
		type: "scatter"
	};
	let trace14 = {
		x: data.map(e => e.victoria_DOY),
		y: data.map(e => e.victoria_2015_2016),
		name: "2015/2016",
		type: "scatter"
	};
	let trace15 = {
		x: data.map(e => e.victoria_DOY),
		y: data.map(e => e.victoria_2016_2017),
		name: "2016/2017",
		type: "scatter"
	};
	let trace16 = {
		x: data.map(e => e.victoria_DOY),
		y: data.map(e => e.victoria_2017_2018),
		name: "2017/2018",
		type: "scatter"
	};
	let trace17 = {
		x: data.map(e => e.victoria_DOY),
		y: data.map(e => e.victoria_2018_2019),
		name: "2018/2019",
		type: "scatter"
	};
	let trace18 = {
		x: data.map(e => e.victoria_DOY),
		y: data.map(e => e.victoria_2019_2020),
		name: "2019/2020",
		type: "scatter"
	};


	let plotData = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10, trace11, trace12, trace13, trace14, trace15, trace16, trace17, trace18]

	let layout = {
		margin: {
			t: 30,
			b: 100
		},
		xaxis: {
			title: "Fire Year running from July 1st to June 30th in the following year",
			tickvals: [1, 32, 63, 93, 124, 154, 185, 216, 244, 275, 305, 336],
			ticktext: ["Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar", "Apr", "May", "Jun"],
		},
		yaxis: {
			title: "Number of Fires"
		},
		autosize: true
	};

	Plotly.newPlot("nineth", plotData, layout)

};

// main - function that gets initiated when the page is loaded
function init() {

	d3.json("/annual_total_fire_counts").then((totalData) => {
		buildNswTotalPlot(totalData)
		buildQueenslandTotalPlot(totalData)
		buildVictoriaTotalPlot(totalData)
		buildStateStatisticsPlot(totalData)
		buildTotalFirePlot(totalData)
	})

	d3.json("/fire_count_data").then((data) => {

		buildNswPlot(data)
		buildQueenslandPlot(data)
		buildVictoriaPlot(data)
	})

	// update the layout to resize when the window is resized
	window.addEventListener('resize', function() { 
		Plotly.Plots.resize("first"); 
	});
	window.addEventListener('resize', function() { 
		Plotly.Plots.resize("second"); 
	});
	window.addEventListener('resize', function() { 
		Plotly.Plots.resize("third"); 
	});
	window.addEventListener('resize', function() { 
		Plotly.Plots.resize("fourth"); 
	});
	window.addEventListener('resize', function() { 
		Plotly.Plots.resize("fifth"); 
	});
	window.addEventListener('resize', function() { 
		Plotly.Plots.resize("seventh"); 
	});
	window.addEventListener('resize', function() { 
		Plotly.Plots.resize("eighth"); 
	});
	window.addEventListener('resize', function() { 
		Plotly.Plots.resize("nineth"); 
	});

};

// calling the init function when page is loaded
init();