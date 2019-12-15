/*Dashboard3 Init*/
 
"use strict"; 
$(document).ready(function() {
	/*Toaster Alert*/
	$.toast({
		heading: 'Well done!',
		text: '<p>You have successfully completed level 1.</p><button class="btn btn-primary btn-sm mt-10">Play again</button>',
		position: 'top-right',
		loaderBg:'#f68daf',
		class: 'jq-toast-primary',
		hideAfter: 3500, 
		stack: 6,
		showHideTransition: 'fade'
	});
	
	/*Owl Carousel*/
	$('#owl_demo_1').owlCarousel({
		items: 1,
		animateOut: 'fadeOut',
		loop: true,
		margin: 10,
		autoplay: true,
		mouseDrag: false,
		dots:false

	});
});

/*ApexCharts Start*/
var options1 = {
		chart: {
			height: 373,
			type: 'bar',
		},
		colors: ['#f68daf'],
		plotOptions: {
			bar: {
				dataLabels: {
					position: 'top', // top, center, bottom
				},
			}
		},
		dataLabels: {
			enabled: true,
			formatter: function (val) {
				return val + "%";
			},
			offsetY: -20,
			style: {
				fontSize: '12px',
			}
		},
		series: [{
			name: 'Inflation',
			data: [2.3, 3.1, 4.0, 10.1, 4.0, 3.6, 3.2, 2.3, 1.4, 0.8, 0.5, 0.2]
		}],
		xaxis: {
			categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
			position: 'top',
			labels: {
				offsetY: -18,

			},
			axisBorder: {
				show: false
			},
			axisTicks: {
				show: false
			},
			tooltip: {
				enabled: true,
				offsetY: -35,

			}
		},
		fill: {
		  colors: ['#f68daf']
		},
		yaxis: {
			axisBorder: {
				show: false
			},
			axisTicks: {
				show: false,
			},
			labels: {
				show: false,
				formatter: function (val) {
					return val + "%";
				}
			}

		},
		title: {
			text: 'Aca va cualquier cosa',
			floating: true,
			offsetY: 350,
			align: 'center',
			style: {
				color: '#5e7d8a'
			}
		}
}
var chart1 = new ApexCharts(
	document.querySelector("#e_chart_1"),
	options1
);
chart1.render();

var ts2 = 1484418600000;
var dates = [];
var spikes = [5, -5, 3, -3, 8, -8]
for (var i = 0; i < 120; i++) {
  ts2 = ts2 + 86400000;
  var innerArr = [ts2, dataSeries[1][i].value];
  dates.push(innerArr)
}

var options2 = {
  chart: {
	type: 'area',
	stacked: false,
	height: 330,
	zoom: {
	  type: 'x',
	  enabled: true
	},
	toolbar: {
		show: false
	}
  },
  colors: ['#f68daf'],
  dataLabels: {
	enabled: false
  },
  series: [{
	name: 'XYZ MOTORS',
	data: dates,
  }],
  markers: {
	size: 0,
  },
  fill: {
	type: 'gradient',
	colors: ['#f68daf'],
	gradient: {
	  shadeIntensity: 1,
	  inverseColors: false,
	  opacityFrom: 0.5,
	  opacityTo: 0,
	  stops: [0, 90, 100]
	},
  },
  yaxis: {
	min: 20000000,
	max: 250000000,
	labels: {
	  formatter: function (val) {
		return (val / 1000000).toFixed(0);
	  },
	},
	title: {
	  text: 'Price'
	},
  },
  xaxis: {
	type: 'datetime',
  },

  tooltip: {
	shared: false,
	y: {
	  formatter: function (val) {
		return (val / 1000000).toFixed(0)
	  }
	}
  },
  legend: {
	labels: {
	  useSeriesColors: true
	},
	markers: {
	  customHTML: [
		function() {
		  return ''
		}, function() {
		  return ''
		}, function() {
		  return ''
		}
	  ]
	}
  }
}
var chart2 = new ApexCharts(
  document.querySelector("#e_chart_2"),
  options2
);
chart2.render();


var options3 = {
	chart: {
		height: 350,
		type: 'line',
		shadow: {
			enabled: true,
			top: 18,
			left: 7,
			blur: 10,
			opacity: 1
		},
		toolbar: {
			show: false
		}
	},
	colors: ['#f68daf','#fabacf'],
	dataLabels: {
		enabled: true,
	},
	stroke: {
		curve: 'smooth'
	},
	series: [{
			name: "High - 2013",
			data: [28, 29, 33, 36, 32, 32, 33]
		},
		{
			name: "Low - 2013",
			data: [12, 11, 14, 18, 17, 13, 13]
		}
	],
	grid: {
		borderColor: '#e7e7e7',
		row: {
			colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
			opacity: 0.5
		},
	},
	markers: {
		
		size: 6
	},
	xaxis: {
		categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
		title: {
			text: 'Month'
		}
	},
	yaxis: {
		title: {
			text: 'Temperature'
		},
		min: 5,
		max: 40
	},
	legend: {
		position: 'top',
		horizontalAlign: 'right',
		floating: true,
		offsetY: -25,
		offsetX: -5
	}
}
var chart3 = new ApexCharts(
	document.querySelector("#e_chart_3"),
	options3
);
chart3.render();

var options4 = {
  chart: {
	type: 'line',
	width: 100,
	height: 35,
	sparkline: {
	  enabled: true
	}
  },
  colors: ['#f68daf'],
  series: [{
	data: [25, 66, 41, 89, 63, 25, 44, 12, 36, 9, 54]
  }],
  tooltip: {
	fixed: {
	  enabled: false
	},
	x: {
	  show: false
	},
	y: {
	  title: {
		formatter: function (seriesName) {
		  return ''
		}
	  }
	},
	marker: {
	  show: false
	}
  }
    }
var chart4 = new ApexCharts(
	document.querySelector("#sparkline_1"),
	options4
);
chart4.render();

var options5 = {
  chart: {
	type: 'line',
	width: 100,
	height: 35,
	sparkline: {
	  enabled: true
	}
  },
  colors: ['#f68daf'],
  series: [{
	data: [12, 14, 2, 47, 42, 15, 47, 75, 65, 19, 14]
  }],
  tooltip: {
	fixed: {
	  enabled: false
	},
	x: {
	  show: false
	},
	y: {
	  title: {
		formatter: function (seriesName) {
		  return ''
		}
	  }
	},
	marker: {
	  show: false
	}
  }
    }
new ApexCharts(document.querySelector("#sparkline_2"), options5).render();

var options6 = {
  chart: {
	type: 'line',
	width: 100,
	height: 35,
	sparkline: {
	  enabled: true
	}
  },
  colors: ['#f68daf'],
  series: [{
	data: [22, 14, 2,27, 12, 15,7, 75, 20, 15, 12]
  }],
  tooltip: {
	fixed: {
	  enabled: false
	},
	x: {
	  show: false
	},
	y: {
	  title: {
		formatter: function (seriesName) {
		  return ''
		}
	  }
	},
	marker: {
	  show: false
	}
  }
    }
new ApexCharts(document.querySelector("#sparkline_3"), options6).render();

var options7 = {
  chart: {
	type: 'line',
	width: 100,
	height: 35,
	sparkline: {
	  enabled: true
	}
  },
  colors: ['#f68daf'],
  series: [{
	data: [10, 14, 2,47, 12, 15,17, 5, 10,25,2]
  }],
  tooltip: {
	fixed: {
	  enabled: false
	},
	x: {
	  show: false
	},
	y: {
	  title: {
		formatter: function (seriesName) {
		  return ''
		}
	  }
	},
	marker: {
	  show: false
	}
  }
    }
new ApexCharts(document.querySelector("#sparkline_4"), options7).render();
/*ApexCharts End*/