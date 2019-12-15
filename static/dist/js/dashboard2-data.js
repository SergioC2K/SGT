/*Dashboard3 Init*/
 
"use strict"; 
$(document).ready(function() {
	/*Toaster Alert*/
	$.toast({
		heading: 'Oh snap!',
		text: '<p>Change a few things and try submitting again.</p>',
		position: 'bottom-right',
		loaderBg:'#f68daf',
		class: 'jq-toast-danger',
		hideAfter: 3500, 
		stack: 6,
		showHideTransition: 'fade'
	});
});

/*ApexCharts Start*/
window.Apex = {
      stroke: {
        width: 3
      },
      markers: {
        size: 0
      },
      tooltip: {
        fixed: {
          enabled: true,
        }
      }
    };
    
var randomizeArray = function (arg) {
  var array = arg.slice();
  var currentIndex = array.length,
	temporaryValue, randomIndex;

  while (0 !== currentIndex) {

	randomIndex = Math.floor(Math.random() * currentIndex);
	currentIndex -= 1;

	temporaryValue = array[currentIndex];
	array[currentIndex] = array[randomIndex];
	array[randomIndex] = temporaryValue;
  }

  return array;
}

// data for the sparklines that appear below header area
var sparklineData = [47, 45, 54, 38, 56, 24, 65, 31, 37, 39, 62, 51, 35, 41, 35, 27, 93, 53, 61, 27, 54, 43, 19, 46];
var spark1 = {
	chart: {
	type: 'area',
	height: 60,
	sparkline: {
	  enabled: true
	},
},
	colors: ['#f68daf'],
	stroke: {
		curve: 'straight',
		colors: ['#f68daf'],
	},
	fill: {
		opacity: 0.3,
		colors: ['#f68daf'],
	},
	series: [{
		data: randomizeArray(sparklineData)
	}],
	xaxis: {
	crosshairs: {
	  width: 1
	},
	},
	yaxis: {
		min: 0
	}
}
var spark2 = {
	chart: {
		type: 'area',
		height: 60,
		sparkline: {
		  enabled: true
		},
	},
	colors: ['#f68daf'],
	stroke: {
		curve: 'straight',
		colors: ['#f68daf'],
	},
	fill: {
		opacity: 0.3,
		colors: ['#f68daf'],
	},
	series: [{
		data: randomizeArray(sparklineData)
	}],
	xaxis: {
	crosshairs: {
	  width: 1
	},
	},
	yaxis: {
		min: 0
	}
}
var spark1 = new ApexCharts(document.querySelector("#spark1"), spark1);
spark1.render();
var spark2 = new ApexCharts(document.querySelector("#spark2"), spark2);
spark2.render();

	
var options1 = {
	chart: {
		height: 350,
		type: 'line',
		stacked: false,
	},
	dataLabels: {
		enabled: false
	},
	colors: ['#f68daf','#fabacf','#f36493'],
	series: [{
		name: 'Income',
		type: 'column',
		data: [1.4, 2, 2.5, 1.5, 2.5, 2.8, 3.8, 4.6]
	}, {
		name: 'Cashflow',
		type: 'column',
		data: [1.1, 3, 3.1, 4, 4.1, 4.9, 6.5, 8.5]
	}, {
		name: 'Revenue',
		type: 'line',
		data: [20, 29, 37, 36, 44, 45, 50, 58]
	}],
	stroke: {
	width: [1, 1, 4]
	},
	xaxis: {
		categories: [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016],
	},
	yaxis: [
	{
	  axisTicks: {
		show: false,
	  },
	  axisBorder: {
		show: false,
		},
	  labels: {
		style: {
		  color: '#fabacf',
		}
	  },
	  tooltip: {
		enabled: true
	  }
	},

	{
	  seriesName: 'Income',
	  opposite: true,
	  axisTicks: {
		show: true,
	  },
	  axisBorder: {
		show: false
	  },
	  labels: {
		style: {
		  color: '#f36493',
		}
	  },
	  title: {
		text: "Operating Cashflow (thousand crores)",
		style: {
		  color: '#f36493',
		}
	  },
	},
	{
	  seriesName: 'Revenue',
	  opposite: true,
	  axisTicks: {
		show: true,
	  },
	  axisBorder: {
		show: false
	  },
	  labels: {
		style: {
		  color: '#f68daf',
		},
	  }
	},
	],
	tooltip: {
	fixed: {
	  enabled: true,
	  position: 'topLeft', // topRight, topLeft, bottomRight, bottomLeft
	  offsetY: 30,
	  offsetX: 60
	},
	},
	legend: {
	show:false
	}
	}

var chart1 = new ApexCharts(
document.querySelector("#e_chart_1"),
options1
);
chart1.render();

function generateData(baseval, count, yrange) {
	var i = 0;
	var series = [];
	while (i < count) {
		var x = Math.floor(Math.random() * (750 - 1 + 1)) + 1;;
		var y = Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;
		var z = Math.floor(Math.random() * (75 - 15 + 1)) + 15;

		series.push([x, y, z]);
		baseval += 86400000;
		i++;
	}
	return series;
}

var options2 = {
	chart: {
		height: 315,
		type: 'bubble',
		toolbar: {
			show: false
		}
	},
	colors: ['#f68daf','#fabacf','#f36493'],
	dataLabels: {
		enabled: false
	},
	series: [{
			name: 'Bubble1',
			data: generateData(new Date('11 Feb 2017 GMT').getTime(), 20, {
				min: 10,
				max: 60
			})
		},
		{
			name: 'Bubble2',
			data: generateData(new Date('11 Feb 2017 GMT').getTime(), 20, {
				min: 10,
				max: 60
			})
		},
		{
			name: 'Bubble3',
			data: generateData(new Date('11 Feb 2017 GMT').getTime(), 20, {
				min: 10,
				max: 60
			})
		},
		{
			name: 'Bubble4',
			data: generateData(new Date('11 Feb 2017 GMT').getTime(), 20, {
				min: 10,
				max: 60
			})
		}
	],
	fill: {
		opacity: 0.8
	},
	title: {
		show:false
	},
	xaxis: {
		tickAmount: 12,
		type: 'category',
	},
	yaxis: {
		max: 70
	},
	legend: {
		show:false
	}
}
var chart2 = new ApexCharts(
	document.querySelector("#e_chart_2"),
	options2
);
chart2.render();
 
var options3 = {
	chart: {
		height: 397,
		type: 'line',
		shadow: {
			enabled: false,
			top: 3,
			left: 2,
			blur: 3,
			opacity: 1
		},
		toolbar: {
			show: false
		}
	},
	colors: ["#f68daf"],
	stroke: {
		width: 7,   
		curve: 'smooth',
		colors: ['#f68daf'],
	},
	series: [{
		name: 'Likes',
		data: [4, 3, 10, 9, 29, 19, 22, 9, 12, 7, 19, 5, 13, 9, 17, 2, 7, 5]
	}],
	xaxis: {
		type: 'datetime',
		categories: ['1/11/2000', '2/11/2000', '3/11/2000', '4/11/2000', '5/11/2000', '6/11/2000', '7/11/2000', '8/11/2000', '9/11/2000', '10/11/2000', '11/11/2000', '12/11/2000', '1/11/2001', '2/11/2001', '3/11/2001','4/11/2001' ,'5/11/2001' ,'6/11/2001'],
	},
	fill: {
		type: 'gradient',
		gradient: {
			shade: 'dark',
			shadeIntensity: 1,
			type: 'horizontal',
			opacityFrom: 0,
			opacityTo: 1,
			stops: [0, 100, 100, 100]
		},
	},
	markers: {
		size: 4,
		opacity: 0.9,
		colors: ["#f68daf"],
		strokeColor: "#fff",
		strokeWidth: 2,
		 
		hover: {
			size: 7,
		}
	},
	yaxis: {
		min: -10,
		max: 40,
		title: {
			text: 'Engagement',
		},                
	}
}
var chart3 = new ApexCharts(
	document.querySelector("#e_chart_3"),
	options3
);
chart3.render();
/*ApexCharts End*/    
  
/*****E-Charts function start*****/
var echartsConfig = function() { 
	if( $('#e_chart_4').length > 0 ){
		var eChart_4 = echarts.init(document.getElementById('e_chart_4'));
		var option4 = {
			tooltip: {
				show: true,
				trigger: 'axis',
				backgroundColor: '#fff',
				borderRadius:6,
				padding:6,
				axisPointer:{
					lineStyle:{
						width:0,
					}
				},
				textStyle: {
					color: '#324148',
					fontFamily: '-apple-system,BlinkMacSystemFont,"Segoe UI",Nunito,"Helvetica Neue",Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji"',
					fontSize: 12
				}	
			},
			grid: {
				top: '3%',
				left: '3%',
				right: '3%',
				bottom: '3%',
				containLabel: true
			},
			xAxis: {
				type: 'category',
				boundaryGap: false,
				data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
				axisLine: {
					show:false
				},
				axisTick: {
					show:false
				},
				axisLabel: {
					textStyle: {
						color: '#5e7d8a'
					}
				}
			},
			yAxis: {
				type: 'value',
				axisLine: {
					show:false
				},
				axisTick: {
					show:false
				},
				axisLabel: {
					textStyle: {
						color: '#5e7d8a'
					}
				},
				splitLine: {
					lineStyle: {
						color: '#eaecec',
					}
				}
			},
		   
			series: [
				{
					data:[420, 332, 401, 334, 400, 330, 410],
					type: 'line',
					symbolSize: 0,
					itemStyle: {
						color: '#f68daf',
					},
					lineStyle: {
						color: '#f68daf',
						width:3,
					},
					areaStyle: {
						color: '#f68daf',
						opacity:.3
					},
				},
				{
					data: [220, 182, 291, 134, 290, 130, 210],
					type: 'line',
					symbolSize: 0,
					itemStyle: {
						color: '#fabacf',
					},
					lineStyle: {
						color: '#fabacf',
						width:3,
					},
					areaStyle: {
						color: '#fabacf', 
						opacity:.3
					},
				}
			]
		};
		eChart_4.setOption(option4);
		eChart_4.resize();
	}
	
	if( $('#e_chart_5').length > 0 ){
		var eChart_5 = echarts.init(document.getElementById('e_chart_5'));
		var option5 = {
			color: ['#ab26aa', '#d6d9da'],		
			tooltip: {
				show: true,
				trigger: 'axis',
				backgroundColor: '#fff',
				borderRadius:6,
				padding:6,
				axisPointer:{
					lineStyle:{
						width:0,
					}
				},
				textStyle: {
					color: '#324148',
					fontFamily: '-apple-system,BlinkMacSystemFont,"Segoe UI",Nunito,"Helvetica Neue",Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji"',
					fontSize: 12
				}	
			},
			
			grid: {
				top: '3%',
				left: '3%',
				right: '3%',
				bottom: '3%',
				containLabel: true
			},
			xAxis : [
				{
					type : 'category',
					data : ['2011','2012','2013','2014','2015','2016','2017','2018'],
					axisLine: {
						show:false
					},
					axisTick: {
						show:false
					},
					axisLabel: {
						textStyle: {
							color: '#5e7d8a'
						}
					}
				}
			],
			yAxis : [
				{
					type : 'value',
					axisLine: {
						show:false
					},
					axisTick: {
						show:false
					},
					axisLabel: {
						textStyle: {
							color: '#5e7d8a'
						}
					},
					splitLine: {
						lineStyle: {
							color: '#eaecec',
						}
					}
				}
			],
			series : [
				{
					name:'1',
					type:'bar',
					barMaxWidth: 30,
					data:[320, 332, 301, 334, 390, 330, 320,200],
				},
				{
					name:'2',
					type:'bar',
					barMaxWidth: 30,
					data:[120, 132, 101, 134, 90, 230, 210,180],
				}
			]
		};

		eChart_5.setOption(option5);
		eChart_5.resize();
	}

	if( $('#e_chart_9').length > 0 ){
		var eChart_9 = echarts.init(document.getElementById('e_chart_9'));
		var option8 = {
			color: ['#f68daf', '#fabacf'],
			tooltip: {
				show: true,
				trigger: 'axis',
				backgroundColor: '#fff',
				borderRadius:6,
				padding:6,
				axisPointer:{
					lineStyle:{
						width:0,
					}
				},
				textStyle: {
					color: '#324148',
					fontFamily: '-apple-system,BlinkMacSystemFont,"Segoe UI",Nunito,"Helvetica Neue",Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji"',
					fontSize: 12
				}	
			},
			grid: {
				top: '3%',
				left: '3%',
				right: '3%',
				bottom: '3%',
				containLabel: true
			},
			xAxis: [{
				type: 'value',
				axisLine: {
					show:false
				},
				axisTick: {
					show:false
				},
				axisLabel: {
					textStyle: {
						color: '#5e7d8a'
					}
				},
				splitLine: {
					lineStyle: {
						color: '#eaecec',
					}
				}
			}],
			yAxis: {
				type: 'category',
				data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun','Mon', 'Tue', 'Wed', 'Thu'],
				axisLine: {
					show:false
				},
				axisTick: {
					show:false
				},
				axisLabel: {
					textStyle: {
						color: '#5e7d8a'
					}
				}
			},
			series: [{
					name:'1',
					type:'bar',
					stack: 'st1',
					barMaxWidth: 7.5,
					data:[320, 332, 301, 334, 390, 330, 320,334, 390, 330, 320],
				},
				{
					name:'2',
					type:'bar',
					stack: 'st1',
					barMaxWidth: 7.5,
					data:[-120, -132, -101, -134, -90, -230, -210,-134, -90, -230, -210],
				}]
		};
		eChart_9.setOption(option8);
		eChart_9.resize();
	}
	
	if( $('#e_chart_10').length > 0 ){
		var eChart_10 = echarts.init(document.getElementById('e_chart_10'));
		
		var option9 = {
			tooltip: {
				show: true,
				backgroundColor: '#fff',
				borderRadius:6,
				padding:6,
				axisPointer:{
					lineStyle:{
						width:0,
					}
				},
				textStyle: {
					color: '#324148',
					fontFamily: '-apple-system,BlinkMacSystemFont,"Segoe UI",Nunito,"Helvetica Neue",Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji"',
					fontSize: 12
				}	
			},
			series: [
				{
					name:'',
					type:'pie',
					radius: ['40%', '60%'],
					color: ['#f36493', '#f68daf', '#fabacf', '#feeff4'],
					data:[
						{value:435, name:''},
						{value:679, name:''},
						{value:848, name:''},
						{value:348, name:''},
					],
					label: {
						normal: {
							formatter: '{b}\n{d}%'
						},
				  
					}
				}
			]
		};
		eChart_10.setOption(option9);
		eChart_10.resize();
	}
}
/*****E-Charts function end*****/

/*****Resize function start*****/
var echartResize;
$(window).on("resize", function () {
	/*E-Chart Resize*/
	clearTimeout(echartResize);
	echartResize = setTimeout(echartsConfig, 200);
}).resize(); 
/*****Resize function end*****/

/*****Function Call start*****/
echartsConfig();
/*****Function Call end*****/