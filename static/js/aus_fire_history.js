// TBD

// let newPlot = d3.select('plot')
let loadFile = Papa.parse("data/aus_fire_locations/australia.csv", {
	download: true,
	step: function(row) {
		console.log("Row:", row.data);
	},
	complete: function() {
		console.log("All done!");
	}
});
Plotly.d3.csv('data/aus_fire_locations/australia.csv',
	function(err, rows) {
		function unpack(rows, key) {
			return rows.map(function(row) {
				return row[key];
			});
		}

        var data = [
            {
                type: "scattermapbox",
                text: unpack(rows, "bright_ti4"),
                lon: unpack(rows, "longitude"),
                lat: unpack(rows, "latitude"),
                marker: { color: "fuchsia", size: 4 }
            }
        ];

        var layout = {
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
            margin: { r: 0, t: 0, b: 0, l: 0 }
        };

Plotly.newPlot('plot', data, layout);
	}
);