/*Sparkline Init*/
"use strict";
var sparklineLogin = function() { 
	if( $('#sparkline_1').length > 0 ){
		$("#sparkline_1").sparkline([2,4,4,6,8,5,6,4,8,6,6,2 ], {
			type: 'line',
			width: '100%',
			height: '50',
			resize: true,
			lineWidth: '1',
			lineColor: '#f68daf',
			fillColor: '#feeff4',
			spotColor:'00acf0',
			spotRadius:'2',
			minSpotColor: '#f68daf',
			maxSpotColor: '#f68daf',
			highlightLineColor: 'rgba(0, 0, 0, 0)',
			highlightSpotColor: '#f68daf'
		});
	}	
	if( $('#sparkline_2').length > 0 ){
		$("#sparkline_2").sparkline([0,2,8,6,8,5,6,4,8,6,6,2 ], {
			type: 'bar',
			width: '100%',
			height: '50',
			barWidth: '5',
			resize: true,
			barSpacing: '5',
			barColor: '#f68daf',
			highlightSpotColor: '#f68daf'
		});
	}	
	if( $('#sparkline_3').length > 0 ){
		$("#sparkline_3").sparkline([20,4,4], {
			type: 'pie',
			width: '50',
			height: '50',
			resize: true,
			sliceColors: ['#f68daf', '#fabacf', '#feeff4']
		});
	}
	if( $('#sparkline_7').length > 0 ){
		$('#sparkline_7').sparkline([15, 23, 55, 35, 54, 45, 66, 47, 30], {
			type: 'line',
			width: '100%',
			height: '50',
			chartRangeMax: 50,
			resize: true,
			lineWidth: '1',
			lineColor: '#f68daf',
			fillColor: '#feeff4',
			spotColor:'00acf0',
			spotRadius:'2',
			minSpotColor: '#f68daf',
			maxSpotColor: '#f68daf',
			highlightLineColor: 'rgba(0, 0, 0, 0)',
			highlightSpotColor: '#f68daf'
		});
		$('#sparkline_7').sparkline([0, 13, 10, 14, 15, 10, 18, 20, 0], {
			type: 'line',
			width: '100%',
			height: '50',
			chartRangeMax: 40,
			lineWidth: '1',
			lineColor: '#f68daf',
			fillColor: '#feeff4',
			spotColor:'00acf0',
			composite: true,
			spotRadius:'2',
			minSpotColor: '#f68daf',
			maxSpotColor: '#f68daf',
			highlightLineColor: 'rgba(0, 0, 0, 0)',
			highlightSpotColor: '#f68daf'
		});
	}	
}
sparklineLogin();
 
var sparkResize;
$(window).on("resize",function(){
	clearTimeout(sparkResize);
	sparkResize = setTimeout(sparklineLogin, 200);
});
