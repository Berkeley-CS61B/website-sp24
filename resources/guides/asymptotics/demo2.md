---
layout: page
title: Asymptotics Demo 2
author: Josh Hug
parent: Asymptotics
has_children: false
released: false
---
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjs/5.0.4/math.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.5/d3.min.js"></script>
<script src="../../assets/js/jquery.min.js" type="text/javascript"></script>
 <script src="../../assets/css/highlight/highlight.pack.js" type="text/javascript"></script>
 <script src="../../assets/js/copy.js" type="text/javascript"></script>
 <script src="../../assets/js/function-plot.js" type="text/javascript"></script>

<div id="content-container"><main id="content">
  <header class="title">Asymptotics Demo</header>

<form id="form">
<table unlined>
<tr><td>
  <label for="fN">R(N):</label>
  </td><td>
  <input type="text" id="rN" value="2*N + 1" />
  </td>
<td>
  <label for="rN">f(N):</label>
  </td><td>  
  <input type="text" id="fN" value="N" /><br>
</td></tr>
<tr><td>
  <label for="k1">k1:</label>
    </td><td>
  <input type="text" id="k1" value="0.5" />  
</td><td>
  <label for="k2">k2:</label>
    </td><td>
  <input type="text" id="k2" value="3" /><br>
</td></tr>
<tr><td>
  <label for="maxN">maxN:</label>
    </td><td>
  <input type="text" id="maxN" value="20" />  
</td><td>
  <label for="maxY">maxY:</label>
    </td><td>

  <input type="text" id="maxY" value="20" />  
</td></tr>
</table>
  <input type="submit" value="Draw" />
</form>

<div id="plot"></div>
</main>
</div>

<p>
  Plot library: <a href="https://github.com/maurizzzio/function-plot">https://github.com/maurizzzio/function-plot</a>
</p>

<script>
  // Modified from http://gomakethings.com/how-to-get-the-value-of-a-querystring-with-native-javascript/
  var getQueryString = function(field) {
    var href = window.location.href;
    if (href[href.length - 1] === '/') {
      href = href.substring(0, href.length - 1);
    }
    var reg = new RegExp('[?&]' + field + '=([^&#]*)', 'i');
    var string = reg.exec(href);
    return string ? unescape(string[1]) : null;
  };

  function draw() {
    try {
      functionPlot({
        target: '#plot',
        yAxis: {domain: [0, document.getElementById('maxY').value]},
        xAxis: {domain: [0, document.getElementById('maxN').value]},        
        data: [{
          fn: document.getElementById('rN').value.replace(/N/g, "x"),
          sampler: 'builtIn',  // this will make function-plot use the evaluator of math.js
          graphType: 'polyline',
          color: 'red'
        },
        {
          fn: document.getElementById('k1').value + "*(" + document.getElementById('fN').value.replace(/N/g, "x") + ")",
          sampler: 'builtIn',  // this will make function-plot use the evaluator of math.js
          graphType: 'polyline',
          color: 'black'
        },
                {
          fn: document.getElementById('k2').value + "*(" + document.getElementById('fN').value.replace(/N/g, "x") + ")",
          sampler: 'builtIn',  // this will make function-plot use the evaluator of math.js
          graphType: 'polyline',
          color: 'black'
        },
]
      });
    }
    catch (err) {
      console.log(err);
      alert(err);
    }
  }

  document.getElementById('form').onsubmit = function (event) {
    event.preventDefault();
    draw();
  };

  document.getElementById('k1').value = getQueryString('k1') || 0.5;
  document.getElementById('k2').value = getQueryString('k2') || 3;
  document.getElementById('maxN').value = getQueryString('maxN') || 20;
  document.getElementById('maxY').value = getQueryString('maxY') || 20;
  document.getElementById('rN').value = getQueryString('rN') || "2*N + 1";
  document.getElementById('fN').value = getQueryString('fN') || "N";

  draw();
</script>