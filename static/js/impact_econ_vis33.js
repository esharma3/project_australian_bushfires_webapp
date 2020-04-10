d3.json("/econ-impact").then((fireData) => {
    console.log(fireData)
    
var trace1 = {
    x: fireData.map(e => e.year).slice(1,67),
    y: fireData.map(e => e.acres_burned).slice(1,67),
    mode: 'markers',
    type: 'scatter',
    name: 'Acres Burned',
    text: ['Acres Burned-Year'],
    marker: { size: 6 }

};
    var data = [trace1];
    var layout = {
		title: {
		  text:'Major Australian Bushfires- Acres Burned by Year',
		  font: {
			family: 'Arial Black, monospace',
			size: 16
		  },
		  xref: 'paper',
		  x: 0.05,
		},
		xaxis: {
		  title: {
			text: 'Year',
			font: {
			  family: 'Arial Black, monospace',
			  size: 10,
			  color: '#7f7f7f'
			}
		  },
		},
        yaxis: {
            type: 'log',
            autorange: true,
            title: {
			text: 'Acres Burned',
			font: {
			  family: 'Arial Black, monospace',
			  size: 10,
			  color: '#7f7f7f'
			}
		  }
		}
	  };
		  
Plotly.newPlot('Historic-Bushfires-Acres-Burned', data, layout)
});

d3.json("/econ-impact").then((fireData) => {
    console.log(fireData)
trace1 = {
    type: 'scatter',
    x: fireData.map(e => e.year).slice(1,69),
    y: fireData.map(e => e.homes_destroyed).slice(1,69),
    fill: 'tonexty',
    mode: 'none',
    name: 'Homes Destroyed',
    connectgaps: true,
    line: {
      color: 'rgb(219, 64, 82)',
      width: 2
    }
  };
  
trace2 = {
    type: 'scatter',
    x: fireData.map(e => e.year).slice(1,69),
    y: fireData.map(e => e.human_fatalities).slice(1,69),
    fill: 'tozeroy',
    mode: 'none',
    name: 'Human Fatalities',
    connectgaps: true,
    line: {
      color: 'rgb(55, 128, 191)',
      width: 2
    }
  };
  var data = [trace1, trace2];
  var layout = {
    title: {
      text:'Major Australian Bushfires- Human and Homes Lost by Year',
      font: {
        family: 'Arial Black, monospace',
        size: 16
      },
      xref: 'paper',
      x: 0.05,
    },
    xaxis: {
      title: {
        text: 'Year',
        font: {
          family: 'Arial Black, monospace',
          size: 10,
          color: '#7f7f7f'
        }
      },
    },
    yaxis: {
        type: 'log',
        autorange: true,
        title: {
        text: 'Homes/Lives Lost',
        font: {
          family: 'Arial Black, monospace',
          size: 10,
          color: '#7f7f7f'
        }
      }
    }
  };
  
Plotly.newPlot('Historic-Bushfires-Homes-Lives-Lost', data, layout);
});
d3.json("/econ-impact").then((fireData) => {
    console.log(fireData)
trace1 = {
    type: 'scatter',
    x: fireData.map(e => e.year).slice(137,197),
    y: fireData.map(e => e.gdp_current_us_dol).slice(137,197),
    mode: 'line',
    name: 'Australian GDP-B US Dollars',
    connectgaps: true,
    line: {
      color: 'rgb(219, 64, 82)',
      width: 2
    }
  };
  var data = [trace1];
  var layout = {
    title: {
      text:'Major Australian Bushfires- Australian GDP/Year',
      font: {
        family: 'Arial Black, monospace',
        size: 16
      },
      xref: 'paper',
      x: 0.05,
    },
    xaxis: {
      title: {
        text: 'Year',
        font: {
          family: 'Arial Black, monospace',
          size: 10,
          color: '#7f7f7f'
        }
      },
    },
    yaxis: {
        autorange: true,
        title: {
        text: 'Australian GDP-B US Dollars',
        font: {
          family: 'Arial Black, monospace',
          size: 10,
          color: '#7f7f7f'
        }
            },
        }
    }
Plotly.newPlot('Historic-Bushfires-GDP', data, layout);
});
