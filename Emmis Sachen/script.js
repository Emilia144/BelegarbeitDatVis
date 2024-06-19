const mapContainer = d3.select('#map');
d3.json('https://observablehq.com/@d3/world-map-svg').then(function(geojsonData){
    const projection = d3.geoNaturalEarth1().fitSize([width, height], geojsonData)

    const pathGenerator = d3.geoPath().projection(projection);

    mapContainer.selectAll('path')
        .data(geojsonData.features)
        .enter()
        .append('path')
        .attr('d', pathGenerator)
})