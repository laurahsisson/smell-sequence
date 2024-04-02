<script>
import * as d3 from "d3";
export default {
    data() {
        return {};
    },
    mounted() {
        const data = [
            { x: 20, label: "Hello", y: 30, r: 10, children: [{ x: 40, y: 32, r: 5 }] },
            { x: 30, label: "Other", y: 100, r: 10 },
            { x: 40, label: "Other", y: 8, r: 10 },
            { x: 80, label: "Other", y: 35, r: 10 },
            { x: 100, label: "Other", y: 60, r: 10 },
            { x: 105, label: "Other", y: 42, r: 10 },
            { x: 750, label: "Edge", y: 450, r: 10 },
        ];

        const svg = d3.select("svg");


        // Append parent circles
        svg.selectAll(".parentCircle")
            .data(data)
            .enter()
            .append("circle")
            .attr("class", "parentCircle")
            .attr("cx", (d) => d.x)
            .attr("cy", (d) => d.y)
            .attr("r", (d) => d.r)
            .attr("fill", "blue")
            .on("mouseover", (event, d) => {
                console.log("IN" + d.label);
            })
            .on("mouseout", (event, d) => {
                console.log("OUT" + d.label);
            });


        svg.selectAll(".parentLabel")
            .data(data)
            .enter()
            .append("text")
            .attr("class", "parentLabel")
            .attr("x", (d) => d.x)
            .attr("y", (d) => d.y - d.r - 5)
            .attr("text-anchor", "middle")
            .text((d) => d.label);

        // Append children circles
        const childGroups = svg.selectAll(".childGroup")
            .data(data.filter((d) => d.children)) // Filter out data without children
            .enter()
            .append("g")
            .attr("class", "childGroup");

        childGroups.selectAll(".childCircle")
            .data((d) => d.children)
            .enter()
            .append("circle")
            .attr("class", "childCircle")
            .attr("cx", (d) => d.x)
            .attr("cy", (d) => d.y)
            .attr("r", (d) => d.r)
            .attr("fill", "red");

        // Append lines connecting parents to children
        childGroups.each(function(parentData) {
            d3.select(this).selectAll(".connectionLine")
                .data(parentData.children)
                .enter()
                .append("line")
                .attr("class", "connectionLine")
                .attr("x1", parentData.x)
                .attr("y1", parentData.y)
                .attr("x2", (d) => d.x)
                .attr("y2", (d) => d.y)
                .attr("stroke", "black");
        });


    },
};
</script>
<template>
    <svg width="800" height="500"></svg>
</template>