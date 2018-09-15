---
title: CS8, Fall 2018, Mirza 
---

<header>
<h1> {{site.course}}, {{site.quarter}}</h1>
</header>

<div id="info" data-role="collapsible" data-collapsed="false" >
<h2>Course Information</h2>
<ul>
{% for item in site.info %}
<li><a href="{{item.url}}"  data-ajax="false">{{item.title }}</a></li>
{% endfor %}
</ul>
</div>

<div data-role="collapsible" data-collapsed="false">
<h2 id="labs">Labs:</h2>
{% include lab_table.html %}
</div>



<div data-role="collapsible" data-collapsed="false">
<h2 id="homework">Homework:</h2>
{% include hwk_table.html %}
</div>

<div data-role="collapsible" data-collapsed="false">
<h2 id="exams">Exams</h2>
{%include exam_table.html %}
</div>

<div data-role="collapsible" data-collapsed="false">
<h2 id="teams">Lectures</h2>
{%include lectures_table.html %}
</div>
