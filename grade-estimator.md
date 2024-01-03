---
layout: page
title: Grade Estimator
nav_exclude: true
---

# Grade Estimator

<script>
function getValue(s) {
	return document.getElementById(s).value;
}

function calculate() {
	var proj = getValue("proj") / 125.0;
	var hw = getValue("hw") / 100.0;
  var mt1 = getValue("mt1") / 100.0;
	var finalExam = getValue("finalExam") / 100.0;

  /*Programming Assignments (25%)
    Homework (20%)
    Midterm (20%)
    Final exam (35%) */

  // var courseGrade = 0.25 * proj + 0.15 * hw + 0.15 * (wa1 + wa2 + wa3 + wa4) / 4.0 + 0.1 * mt1 + 0.1 * mt2 + 0.25 * finalExam;
  var courseGrade = 0.25 * proj + 0.20 * hw + 0.20 * mt1 + 0.35 * finalExam;
  courseGrade *= 100.0;

  document.getElementById('out').innerHTML = "" + courseGrade;
}
</script>

*Disclaimer:* This grade estimator is provided for informational purposes only. In the unlikely event that a bug results in a disagreement between the course policies and this tool, the grade calculated using the course policies will be the one that is submitted to the University.

<table>
  <tr>
    <td><label for="proj">Total Project Score:</label></td>
    <td><input type="number" id="proj" name="proj" min="0" max="134" step="any" value="125" size="4"> / 125.0</td>
    <td style="width:60%">Total project score includes 5 projects of up to 25 pts each, plus any extra credit e.g. from contests</td>
  </tr>
  <tr>
    <td><label for="hw">Total Homework Score:</label></td>
    <td><input type="number" id="hw" name="hw" min="0" max="100" step="any" value="100" size="4"> / 100.0</td>
    <td>You are allowed one homework drop, so this is the calculated from your 9 highest-scoring HW submissions, weighted equally. HW0 is not used for calculating your course grade.</td>
  </tr>
  <tr>
    <td><label for="mt1">Midterm Score:</label></td>
    <td><input type="number" id="mt1" name="mt1" min="0" max="100" step="any" value="100" size="4"> / 100.0</td>
    <td rowspan="2">The actual exams may not be out of 100 points, but this won't change the fact that the midterm accounts for 20% and the final exam accounts for 35% of your course grade.</td>
  </tr>
  <tr>
    <td><label for="finalExam">Final Exam Score:</label></td>
    <td><input type="number" id="finalExam" name="finalExam" min="0" max="100" step="any" value="100" size="4"> / 100.0</td>
  </tr>
  <tr>
    <td colspan="3"><b>Projected Overall Percentage: <a id="out">[press button below to calculate]</a></b></td>
  </tr>
</table> 

<button id="calculate_btn" onclick="calculate()"> Calculate Overall Percentage</button>

 <div class="row">
  <div class="column" style="float:left;width:40%">
    <table>
      <tr>
        <th>Grade</th>
        <th>Overall Percentage</th>
      </tr>
      <tr><td>A</td><td>[85, 100]</td></tr>
      <tr><td>A-</td><td>[80, 85)</td></tr>
      <tr><td>B+</td><td>[75, 80)</td></tr>
      <tr><td>B</td><td>[70, 75)</td></tr>
      <tr><td>B-</td><td>[65, 70)</td></tr>
      <tr><td>C+</td><td>[60, 65)</td></tr>
      <tr><td>C</td><td>[55, 60)</td></tr>
      <tr><td>C-</td><td>[50, 55)</td></tr>
      <tr><td>D+</td><td>[45, 50)</td></tr>
      <tr><td>D</td><td>[40, 45)</td></tr>
      <tr><td>D-</td><td>[35, 40)</td></tr>
      <tr><td>F</td><td>[0 , 35)</td></tr>
    </table>
  </div>
  <div class="column" style="width:40%">
    <table>
      <tr>
        <th>Assignments</th>
        <th>Percent of Grade</th>
      </tr>
      <tr><td>Projects</td><td>25%</td></tr>
      <tr><td>Homework</td><td>20%</td></tr>
      <tr><td>Midterm</td><td>20%</td></tr>
      <tr><td>Final Exam</td><td>35%</td></tr>
    </table>
  </div>
</div> 


<div>
The instructors may adjust grades upward based on class participation, extra credit, etc. The grade of A+ will be awarded at the instructors’ discretion based on exceptional performance.
</div>