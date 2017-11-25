function bubbleChart() {
    var width = 10000,
        height = 10000,
        maxRadius = 10000,
        columnForColors = "category",
        columnForRadius = "views";

    function chart(selection) {
        var data = selection.enter().data();
        var div = selection,
            svg = div.selectAll('svg');
        svg.attr('width', width).attr('height', height);

        var tooltip = selection
            .append("div")
            .style("position", "absolute")
            .style("visibility", "hidden")
            .style("color", "white")
            .style("padding", "12px")
            .style("background-color", "#626D72")
            .style("border-radius", "12px")
            .style("text-align", "center")
            .style("font-family", "monospace")
            .style("width", "400px")
            .text("");


        var simulation = d3.forceSimulation(data)
            .velocityDecay(0.2)
            .force("collide", d3.forceManyBody().strength([-50]))
            .force("x", d3.forceX().strength(0.2))
            .force("y", d3.forceY().strength(0.2))
            //.force("collide",dc.forceCollide())
            .on("tick", ticked);


        function ticked(e) {

            node.attr("cx", function(d) {
                    return d.x;
                 })
                .attr("cy", function(d) {
                    return d.y;
                });
        }

        var colorCircles = d3.scaleOrdinal(d3.schemeCategory10);
        var scaleRadius = d3.scaleLinear().domain([d3.min(data, function(d) {
            return +d[columnForRadius];
        }), d3.max(data, function(d) {
            return +d[columnForRadius];
        })]).range([7, 25])    //5,18

        var node = svg.selectAll("circle")
            .sort(data)
            .data(data)
            .enter()
            .append("circle")
            .attr('r', function(d) {
                return scaleRadius(d[columnForRadius])
            })
            .style("fill", function(d) {
                return colorCircles(d[columnForColors])
            })
            .style('stroke','none')
            .attr('transform', 'translate(' + [width/2 , height/2 ] + ')')
            .on("mouseover", function(d) {
                d3.select(this)
                    .style('stroke','Black')
                tooltip.html(d[columnForColors] + "<br>" + d.title + "<br>" + d[columnForRadius] + " Packets");
                return tooltip.style("visibility", "visible");
            })
            .on("mousemove", function() {
                return tooltip.style("top", (d3.event.pageY - 10) + "px").style("left", (d3.event.pageX + 10) + "px");
            })
            .on("mouseout", function() {
                d3.select(this)
                    .style('stroke','none')
                return tooltip.style("visibility", "hidden");
            })
            .on("click",function(){
                d3.select(this)
                    .style('stroke','Black')

            });


    }



    chart.width = function(value) {
        if (!arguments.length) {
            return width;
        }
        width = value;
        return chart;
    };

    chart.height = function(value) {
        if (!arguments.length) {
            return height;
        }
        height = value;
        return chart;
    };


    chart.columnForColors = function(value) {
        if (!arguments.columnForColors) {
            return columnForColors;
        }
        columnForColors = value;
        return chart;
    };

    chart.columnForRadius = function(value) {
        if (!arguments.columnForRadius) {
            return columnForRadius;
        }
        columnForRadius = value;
        return chart;
    };

    return chart;
}
