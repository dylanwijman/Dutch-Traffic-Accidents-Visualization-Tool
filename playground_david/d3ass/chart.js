/* 
Author: David Zomerdijk
Description: using d3 to visualize a chart
*/
var dataset = [10, 14, 4, 4, 17, 6, 7, 8 ,9 ,10 ,11 ,3 ];
var dates = [ "Jan", "Feb", "Mar",  "Apr","May","Jun","Jul","aug", "Sep","Oct","Nov","Dec"  ];
//Width and height
var w = 500;
var h = 100;
var barPadding = 2;
var scaling = 5;
var padding = 25;


var svg = d3.select("body")
            .append("svg")
            .attr("width", w)
            .attr("height", h);

var yScale = d3.scale.linear()
	.domain([0, d3.max(dataset)])
	.range([h-padding, 0]);


svg.selectAll("rect")
   .data(dataset)
   .enter()
   .append("rect")
   .attr("x", function(d, i) { return padding + i * ((w -padding)/ dataset.length);}) //Bar width of 20 plus 1 for padding
   .attr("y", function(d) {return yScale(d); }) //Height minus data value
   //.attr("y", function(d) {return h - padding  - d * scaling ; }) //Height minus data value
   .attr("width", (w -padding) / dataset.length - barPadding)
   .attr("height", function(d) {return h- padding - yScale(d)  ; })//Just the data value
   .attr("fill", function(d) { return "rgb(" + ( d * 20) +",0," + (200 - d*20) + ")";});


// svg.append("g")
//     .call(d3.svg.axis()
//                 .scale(xScale)
//                 .orient("bottom"));


   //add labels

   svg.selectAll("text")
	   .data(dataset)
	   .enter()
	   .append("text")
	   .text(function(d) {  return d; })
	   //.attr("x", function(d, i) {return i * (w / dataset.length) + 5;  })
   	   //.attr("y", function(d) { return h - padding - (d * 4) + 15;})
   	   .attr("font-family", "sans-serif")
	   .attr("font-size", "11px")
	   .attr("fill", "white")
	   .attr("text-anchor", "middle")
	   .attr("x", function(d, i) 
	   			{return padding + i * ((w -padding) / dataset.length) + (w / dataset.length - barPadding) / 2;
    	})
	   .attr("y", function(d) 
        		{return yScale(d)  + 14;  //15 is now 14
    	});

var xScale = d3.scale.ordinal()
	.domain(dates)
	.rangeBands([0, w-padding ]);

var xAxis = d3.svg.axis().scale(xScale).orient("bottom").tickSize(0).tickPadding(10); //



svg.append("g")
	.attr("class", "axis")
	.attr("transform", "translate("+ padding +"," + (h - padding) + ")")
	.call(xAxis);


var yAxis = d3.svg.axis()
              .scale(yScale)
              .orient("left")
              .ticks(5);

//Create Y axis
svg.append("g")
    .attr("class", "axis")
    .attr("transform", "translate(" + padding + ",0)")
    .call(yAxis);








// ---------------------------------
// example using divs
// ---------------------------------

// var dataset = [1, 2, 3, 4, 5, 6, 7, 8 ,9 ,10 ,11 ,12 ];
// d3.select("body")
// 	//.selectAll("p")   //for text example
// 	.selectAll("div")
// 	.data(dataset)
// 	.enter()
// 	//.append("p") for text example
// 	.append("div")
// 	.attr("class", "bar")
// 	.style("height", function(d) { return (d * 10) + "px";});
// 	//.classed("bar", true)
// 	//.text( function(d) { return  "I can count up to " + d; }); //for text example
