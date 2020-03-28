function animalImpactDonut(totalData) {

  let plotData = [{
    type: "pie",
    hole: .8,
    values: [totalData.map => (e => e.impact_list['area_max']), 10],
    labels: ["Impacted Area", "Safe Area"],
    textinfo: "label+percent",
    textposition: "outside",
    automargin: true
  }]

  let layout = {
    height: 400,
    width: 400,
    margin: {"t": 0, "b": 0, "l": 2, "r": 2}
    }

  Plotly.newPlot("first", plotData, layout)

}

function init() {

  console.log("hello")
  // console.log("hello again")

  d3.json("/impact").then((data) => {

  console.log("hello again")
  animalImpactDonut(data)
  })
}

init();