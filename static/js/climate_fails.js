function buildComparisonPlot(combinedData) {

	d3.json("/annual_total_fire_counts").then((totalData) => {

		let xValue = ["2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019"]

		let trace1 = {
			x: xValue,
			y: totalData.map(e => e.nsw_total_fires / 10000),
			name: "Number of Fires/10000 - New South Wales (scaled)",
			type: 'scatter',
			marker: {
				color: "red"
			}
		}

		let trace2 = {
			x: xValue,
			y: totalData.map(e => e.queensland_total_fires / 10000).slice(18, 36),
			name: "Number of Fires/10000 - Queensland (scaled))",
			type: 'scatter',
			marker: {
				color: "orange"
			}
		}

		let trace3 = {
			x: xValue,
			y: totalData.map(e => e.victoria_total_fires / 10000).slice(36, 55),
			name: "Number of Fires/10000 - Victoria (scaled)",
			type: 'scatter',
			marker: {
				color: "brown"
			}
		}

		let trace4 = {

			x: combinedData.map(e => e.max_temp_anomaly_year).slice(92, 110),
			y: combinedData.map(e => e.max_temp_anomaly_celcius).slice(92, 110),
			name: "Annual Max Temp Anomaly in °Celsius",
			type: 'scatter',
			marker: {
				color: "black"
			}
		};

		let trace5 = {
			x: combinedData.map(e => e.annual_rainfall_anomaly_year).slice(552, 570),
			y: combinedData.map(e => e.annual_rainfall_anomaly_mm / 100).slice(552, 570),
			name: "Annual Rainfall Anomaly/100 in mm (scaled)",
			type: 'scatter',
			marker: {
				color: "blue"
			}
		};

		let plotData = [trace1, trace2, trace3, trace4, trace5]

		let layout = {
			autosize: true,
			title: "Australian Bushfires & Temperature/Rainfall Anomaly Pattern (2002-2020)",
			xaxis: {
				type: 'category',
			},
			yaxis: {
				title: "Max Temperature/ Rainfall/ Fire Count"
			}
		}

		Plotly.newPlot("climate_first", plotData, layout)

		para = "The extreme heat in Australia is not just a fluke. There are unique patterns in rain and temperature that converge to scorch the continent. " +
			"Australia is deep in the throes of the accelerating climate crisis, facing not just extreme heat but changes in rainfall patterns. These shifts in " +
			"turn stand to worsen problems like drought and wildfires. Taken together, Australia serves as a microcosm of all the complicated ways that climate " +
			"variables interact making climate as one of the dominent catalyst responsible for the significant increase in the Australian bushfires. " +
			"The year 2019 shows a drastic increase in maximum tempearture and a significant drop in annual rainfall that together served as a catalyst " +
			"causing a surge in number of bushfires across Australia specially is New South Wales and Victoria."

		d3.select("p").text("")
		d3.select("p").append("text").text(para)
	})
}


function buildPollutantPlot(combinedData) {

	d3.json("/annual_total_fire_counts").then((totalData) => {

		let xValue = ["2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019"]

		let trace1 = {
			x: xValue,
			y: totalData.map(e => e.nsw_total_fires / 1000),
			name: "Number of Fires x 10000 (New South Wales)",
			type: 'scatter',
			marker: {
				color: "red"
			}
		}

		let trace2 = {
			x: xValue,
			y: totalData.map(e => e.queensland_total_fires / 1000).slice(18, 36),
			name: "Number of Fires x 10000 (Queensland)",
			type: 'scatter',
			marker: {
				color: "orange"
			}
		}

		let trace3 = {
			x: xValue,
			y: totalData.map(e => e.victoria_total_fires / 1000).slice(36, 55),
			name: "Number of Fires x 10000 (Victoria)",
			type: 'scatter',
			marker: {
				color: "brown"
			}
		}

		let trace4 = {

			x: combinedData.map(e => e.air_pollutant_year).slice(939, 956),
			y: combinedData.map(e => e.CO2_ppm / 10).slice(939, 956),
			width: 0.7,
			name: "CO2 (ppm) / 10 (scaled)",
			type: 'scatter',
			marker: {
				color: "black"
			}
		}

		let trace5 = {

			x: combinedData.map(e => e.air_pollutant_year).slice(939, 956),
			y: combinedData.map(e => e.CH4_ppb / 100).slice(939, 956),
			width: 0.7,
			name: "CH4 (ppb)/100 (scaled)",
			type: 'scatter',
			marker: {
				color: "grey"
			}
		}

		let trace6 = {

			x: combinedData.map(e => e.air_pollutant_year).slice(939, 956),
			y: combinedData.map(e => e.N2O_ppb / 10).slice(939, 956),
			width: 0.7,
			name: "N2O (ppb)/10 (scaled)",
			type: 'scatter',
			marker: {
				color: "blue"
			}
		}

		let plotData = [trace1, trace2, trace3, trace4, trace5, trace6]

		let layout = {
			title: "Australian Bushfires & Greenhouse Gases (2002-2020)",
			xaxis: {
				type: 'category',
			},
			yaxis: {
				title: "Gas (ppm/ppb)/ Fire Count"
			},
			autosize: true
		}

		Plotly.newPlot("climate_first", plotData, layout)
	})

	para = "The bushfires have not only been made more likely and intense by climate change, they also add to it. " +
		"Fires contribute to Australia's greenhouse gas emissions. Australia has one of the highest per capita emissions of carbon dioxide in the " +
		"world. Wildfires also release air pollutants like carbon monoxide and nitrous oxide, which can harm the health of residents nearby and " +
		"firefighters on the front lines. Until the 2019–2020 Australian bushfire season, the forests in Australia were thought " +
		"to reabsorb all the carbon released in bushfires across the country. This would mean the forests " +
		"achieved net zero emissions. However, global warming is making bushfires burn more intensely and frequently and the 2019–2020 bushfires " +
		"emitted 400 megatonnes of carbon dioxide into the atmosphere in its first quarter itself. " +
		"This has increased Australia’s annual greenhouse gas emissions, " +
		"contributing to global warming, and heighten the likelihood of recurring megafires that will release yet more emissions creating a deeply concerning " +
		"climate feedback loop."

	d3.select("p").text("")
	d3.select("p").append("text").text(para)
}


function buildMaxTempPlot(combinedData) {

	let xValue = combinedData.map(e => e.max_temp_anomaly_year)
	let yValue = combinedData.map(e => e.max_temp_anomaly_celcius)

	let trace1 = {
		x: xValue,
		y: yValue,
		width: 0.7,
		type: 'bar',
		marker: {}
	};

	trace1.marker.color = trace1.y.map(function (v) {
		return v < 0 ? 'blue' : 'red'
	});

	let plotData = [trace1]

	let layout = {
		title: "Australia Maximum Temperature Anomaly in °Celsius (1910 - 2019)",
		xaxis: {
			type: 'category',
		},
		yaxis: {
			title: "Temperature Anomaly (°Celsius)"
		},
		autosize: true
	}

	Plotly.newPlot("climate_first", plotData, layout)

	para = "Australia’s climate is notorious for its volatility, but the summer of 2019 showed the highest change in the maximum temperature anomaly " +
		"as seen in last several years. The year 2019 shows the highest increase of 2.09° Celsius in Australia’s overall " +
		"Maximum temperature since 1910. Since 2013, there is almost constant increase in maximum temperature anomaly. " +
		"The graph above also shows the gradual increase in the country’s maximum temperature with first half of the 20th century being a lot cooler than the second " +
		"half of the century. The 21st century marks the beginning of significant and persistent increased anomaly in maximum temperature."

	d3.select("p").text("")
	d3.select("p").append("text").text(para)
}


function buildMinTempPlot(combinedData) {

	let xValue = combinedData.map(e => e.min_temp_anomaly_year)
	let yValue = combinedData.map(e => e.min_temp_anomaly_celcius)

	let trace1 = {

		x: xValue,
		y: yValue,
		width: 0.7,
		type: 'bar',
		marker: {}
	};

	trace1.marker.color = trace1.y.map(function (v) {
		return v < 0 ? 'blue' : 'red'
	});

	let plotData = [trace1]

	let layout = {
		title: "Australia Minimum Temperature Anomaly in °Celsius (1910 - 2019)",
		xaxis: {
			type: 'category',
		},
		yaxis: {
			title: "Temperature Anomaly (°Celsius)"
		},
		autosize: true
	}

	Plotly.newPlot("climate_first", plotData, layout)

	para = "Australia’s climate shows an accelerating anomaly in not just the maximum temperature but the minimum tempearture too. " +
		"There has been an almost persistent increase in the minimum teperature anomaly since 1980. The year 1998 shows the highest anomaly of 1.26° " +
		" Celsisus. " +
		"The above graph also shows the gradual increase in the country’s minimum temperature anomaly with first half of the 20th century being a lot cooler than the second " +
		"half of the century. The 21st century marks the beginning of significant and persistent increased anomaly in minimum temperature."

	d3.select("p").text("")
	d3.select("p").append("text").text(para)
}


function buildMeanTempPlot(combinedData) {

	let xValue = combinedData.map(e => e.mean_temp_anomaly_year)
	let yValue = combinedData.map(e => e.mean_temp_anomaly_celcius)

	let trace1 = {

		x: xValue,
		y: yValue,
		width: 0.7,
		type: 'bar',
		marker: {}
	};

	trace1.marker.color = trace1.y.map(function (v) {
		return v < 0 ? 'blue' : 'red'
	});

	let plotData = [trace1]

	let layout = {
		title: "Australia Mean Temperature Anomaly in °Celsius (1910 - 2019)",
		xaxis: {
			type: 'category',
		},
		yaxis: {
			title: "Temperature Anomaly (°Celsius)"
		},
		autosize: true
	}

	Plotly.newPlot("climate_first", plotData, layout)

	para = "Australia experienced the hottest year on record in 2019, which had a mean temperature of 1.52° Celsius above the mean calculated for 1961 to 1990. " +
		"The year that delivered crippling drought, heatwaves, temperature records and devastating bushfires was 0.19°C hotter than 2013, the previous " +
		"record holder. The second hottest year was 2013, followed by 2005, 2018 and 2017." +

		d3.select("p").text("")
	d3.select("p").append("text").text(para)
}


function buildAnnualRainPlot(combinedData) {

	let xValue = combinedData.map(e => e.annual_rainfall_year)
	let yValue = combinedData.map(e => e.annual_rainfall_mm)

	let trace1 = {

		x: xValue,
		y: yValue,
		width: 0.7,
		type: 'bar',
		marker: {
			color: "blue"
		}
	};


	let plotData = [trace1]

	let layout = {
		title: "Australia Annual Rainfall in Millimetre (1900 - 2019)",
		xaxis: {
			type: 'category',
		},
		yaxis: {
			title: "Annual Rainfall (mm)"
		},
		autosize: true
	}

	Plotly.newPlot("climate_first", plotData, layout)

	para = "Australia had its driest ever year in 2019, with rainfall 40% lower than average, based on records going back to 1900. " +
		"The year 2019 recorded an annual average rainfall of 277.72 mm, the lowest since 1900."

	d3.select("p").text("")
	d3.select("p").append("text").text(para)
}


function buildRainAnomalyPlot(combinedData) {

	let xValue = combinedData.map(e => e.annual_rainfall_anomaly_year)
	let yValue = combinedData.map(e => e.annual_rainfall_anomaly_mm)

	let trace1 = {

		x: xValue,
		y: yValue,
		width: 0.7,
		type: 'bar',
		marker: {}
	};

	trace1.marker.color = trace1.y.map(function (v) {
		return v < 0 ? 'blue' : 'red'
	});

	let plotData = [trace1]

	let layout = {
		title: "Australia Annual Rainfall Anomaly in Millimetre (1900 - 2019)",
		xaxis: {
			type: 'category',
		},
		yaxis: {
			title: "Rainfall Anomaly (mm)"
		},
		autosize: true
	}

	Plotly.newPlot("climate_first", plotData, layout)

	para = "Australia had its driest ever year in 2019, with the highest ever drop of 187.47 mm in annual rainfall since 1900. " +
		"The graph shows more negative anomaly than positive in last 120 years indicating that for the country, that faces drought, " +
		"there has been more decrease in rainfall than increase."

	d3.select("p").text("")
	d3.select("p").append("text").text(para)
}


function buildSSTPlot(combinedData) {

	let xValue = combinedData.map(e => e.sea_surface_temp_anomaly_year)
	let yValue = combinedData.map(e => e.sea_surface_temp_anomaly_celcius)

	let trace1 = {

		x: xValue,
		y: yValue,
		width: 0.7,
		type: 'bar',
		marker: {}
	};

	trace1.marker.color = trace1.y.map(function (v) {
		return v < 0 ? 'blue' : 'red'
	});

	let plotData = [trace1]

	let layout = {
		title: "Australia Sea Surface Temperature Anomaly in °Celsius (1900-2019)",
		xaxis: {
			type: 'category',
		},
		yaxis: {
			title: "Temperature Anomaly (°Celsius)"
		},
		autosize: true
	}

	Plotly.newPlot("climate_first", plotData, layout)

	para = "Australia is facing constant increase in its Sea Surface Temperature since 1995. The year 2016 reported the highest anomaly " +
		" of 0.78° Celsius. From 1900 till 1970, the country had cooler Sea Surface Temperature with persistent negative anomalies but post 1970 " +
		" the country started having high positive anomalies indicating higher Sea Surface Temperatures."

	d3.select("p").text("")
	d3.select("p").append("text").text(para)
}


function buildCO2Plot(combinedData) {

	let trace1 = {

		x: combinedData.map(e => e.air_pollutant_year),
		y: combinedData.map(e => e.CO2_ppm),
		width: 0.7,
		name: "2002/2003",
		type: 'scatter',
		marker: {
			color: "grey"
		}
	};

	let plotData = [trace1]

	let layout = {
		title: "Australia Carbon Dioxide Level in Parts-Per-Million (1978-2019)",
		xaxis: {
			type: 'category',
		},
		yaxis: {
			title: "Carbon Dioxide (ppm)"
		},
		autosize: true
	}

	Plotly.newPlot("climate_first", plotData, layout)

	para = "The historic wildfires in Australia likely unleashed about 900 million tons of carbon dioxide into the atmosphere, " +
		"equivalent to nearly double the country's total yearly fossil fuel emissions. The graph shows a continuos increase in the " +
		"Carbon Dioxide level each year with 2019 reporting about 407 parts-per-million Carbon Dioxide level in the country."

	d3.select("p").text("")
	d3.select("p").append("text").text(para)
}


function buildCH4Plot(combinedData) {

	let trace1 = {

		x: combinedData.map(e => e.air_pollutant_year),
		y: combinedData.map(e => e.CH4_ppb),
		width: 0.5,
		name: "2002/2003",
		type: 'scatter',
		marker: {
			color: "black"
		}
	};

	let plotData = [trace1]

	let layout = {
		title: "Australia Methane (CH4) Level in Parts-Per-Billion (1978-2019)",
		xaxis: {
			type: 'category',
		},
		yaxis: {
			title: "CH4 (Methane) (ppb)"
		},
		autosize: true
	}

	Plotly.newPlot("climate_first", plotData, layout)

	para = "Methane (CH4) is 85% of natural gas, leaks, and has a Global Warming Potential (GWP) 105 times that of the same mass of carbon dioxide " +
		"(CO2) on a 20 year time frame with aerosol impacts included. Like Carbon Dioxide, there is a continuos increase in reported levels of Methane " +
		"in the atmosphere with the year 2019 showing approximately 1817 parts-per-billion Methane levels."

	d3.select("p").text("")
	d3.select("p").append("text").text(para)
}


function buildN2OPlot(combinedData) {

	let trace1 = {

		x: combinedData.map(e => e.air_pollutant_year),
		y: combinedData.map(e => e.N2O_ppb),
		width: 0.7,
		name: "2002/2003",
		type: 'scatter',
		marker: {
			color: "blue"
		}
	};

	let plotData = [trace1]

	let layout = {
		title: "Australia Nitrous Oxide (N2O) Level in Parts-Per-Billion (1978-2019)",
		xaxis: {
			type: 'category',
		},
		yaxis: {
			title: "Nitrous Oxide N2O (ppb)"
		},
		autosize: true
	}

	Plotly.newPlot("climate_first", plotData, layout)

	para = "The graph shows a continuos increase in the emitted Nitrous Oxide levels with the year 2019 reporting Nitrous Oxide level of 330 parts-per-billion.  " +
		"Nitrous oxide has an atmospheric lifetime of 110 years. The process that removes nitrous oxide from the atmosphere also depletes ozone. " +
		"So nitrous oxide is not only a greenhouse gas, but also an ozone destroyer. Emissions of nitrous oxide — a greenhouse gas 300 times more potent " +
		"than carbon dioxide — are going up faster and each molecule of nitrous oxide in the atmosphere can capture 300 times more heat than a " +
		"molecule of carbon dioxide."

	d3.select("p").text("")
	d3.select("p").append("text").text(para)
}


function buildOnLoadPlot(combinedData) {

	let trace1 = {
		x: combinedData.map(e => e.max_temp_decile10_year),
		y: combinedData.map(e => e.maxtemp_total_land_area_percentage),
		name: "Annual Max Temperature (°Celsius) Decile 10",
		fill: 'tozeroy',
		type: 'scatter',
		marker: {
			color: "red"
		}
	};

	let trace2 = {
		x: combinedData.map(e => e.annual_rainfall_decile10_year).slice(810, ),
		y: combinedData.map(e => e.rainfall_total_land_area_percentage).slice(810, ),
		name: "Annual Rainfall Decile 10",
		type: 'bar',
		marker: {
			color: "blue"
		}
	};


	let plotData = [trace1, trace2]

	let layout = {
		title: "Australia - Annual Maximum Temperature & Rainfall Area in decile 10 (1910-2019)",
		xaxis: {
			type: 'category',
		},
		yaxis: {
			title: "Percentage of Total Land Area (%)",
		},
		autosize: true
	}

	Plotly.newPlot("climate_first", plotData, layout)

	para = "Climate change is influencing the frequency and severity of dangerous bushfire conditions in Australia through influencing temperature, " +
		"environmental moisture and weather patterns. There have been significant changes observed in recent decades towards more " +
		"dangerous bushfire weather conditions for various regions of Australia. " +
		"Bushfire weather conditions in future years are projected to increase in severity for many regions of Australia due to more " +
		"extreme heat events, with the rate and magnitude of change increasing with greenhouse gas concentrations (and emissions)."

	d3.select("p").text("")
	d3.select("p").append("text").text(para)

}


// main - function that gets initiated when the page is loaded
function init() {

	d3.json("/climate_data").then((combinedData) => {

		window.onload = buildOnLoadPlot(combinedData)

		d3.select("#main1-btn").on("click", function () {
			buildOnLoadPlot(combinedData)
		})

		d3.select("#main2-btn").on("click", function () {
			buildComparisonPlot(combinedData)
		})

		d3.select("#max-temp-btn").on("click", function () {
			buildMaxTempPlot(combinedData)
		})

		d3.select("#min-temp-btn").on("click", function () {
			buildMinTempPlot(combinedData)
		})

		d3.select("#mean-temp-btn").on("click", function () {
			buildMeanTempPlot(combinedData)
		})

		d3.select("#rain-btn").on("click", function () {
			buildAnnualRainPlot(combinedData)
		})

		d3.select("#rain-anomaly-btn").on("click", function () {
			buildRainAnomalyPlot(combinedData)
		})

		d3.select("#sst-btn").on("click", function () {
			buildSSTPlot(combinedData)
		})

		d3.select("#main3-btn").on("click", function () {
			buildPollutantPlot(combinedData)
		})

		d3.select("#co2-btn").on("click", function () {
			buildCO2Plot(combinedData)
		})

		d3.select("#ch4-btn").on("click", function () {
			buildCH4Plot(combinedData)
		})

		d3.select("#n2o-btn").on("click", function () {
			buildN2OPlot(combinedData)
		})

	})

	// update the layout to resize when the window is resized
	window.onresize = function () {
		Plotly.relayout('climate_first', {
			'xaxis.autorange': true,
			'yaxis.autorange': true
		})
	}

}


// calling the init function when page is loaded
init();