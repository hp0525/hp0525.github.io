---
layout: post
title: "Exploratory Analysis of UFO Sightings: Shapes and Sighting Durations Over Time"
author: "Harshal Panda"
date: 2026-11-06
---
## Introduction
In this assignment, I explore historical UFO reports to uncover patterns in reported object shapes and the statistical distribution of sighting durations across decades. Using Python, Pandas, Altair, and Vega-Lite, I transform raw data and build two complementary visualizations, including an interactive timeline selection filter.

---

## Visualization 1: Distribution of Reported UFO Shapes

<div id="vis1"></div>

### Write-up & Design Choices
* **What is being visualized:** This bar chart illustrates the frequency of different reported UFO shapes (such as triangles, circles, lights, and spheres) across the global dataset.
* **Encodings:** I utilized a quantitative encoding on the x-axis (`count():Q`) representing the total number of recorded sightings, and a nominal encoding on the y-axis (`shape:N`) sorted in descending order of frequency (`sort='-x'`) to make comparisons straightforward.
* **Colormap:** The color encoding is tied directly to the sighting count (`count():Q`) using the perceptually uniform `viridis` color scheme to emphasize higher-frequency shapes through color intensity.
* **Data Transformations:** In my Python notebook, rows containing missing or null values in the `shape` column were filtered out using `dropna()` to ensure accurate category counts before aggregation.

---

## Visualization 2: UFO Sighting Durations Over Time (Interactive)

<div id="vis2"></div>

### Write-up & Design Choices
* **What is being visualized:** This interactive visualization features a detailed scatter plot showing individual UFO sighting durations (`log10` seconds) against the parsed report year, paired with a synchronized summary timeline bar chart below it.
* **Encodings:** The scatter plot uses an ordinal year scale on the x-axis and a quantitative log-scale duration on the y-axis, with points color-encoded by `country:N` using a categorical `category10` scheme.
* **Interactivity:** I incorporated an interval brush selection (`alt.selection_interval`) across the timeline selector chart. When dragging and highlighting a specific range of years on the lower timeline widget, the upper scatter plot dynamically updates to highlight and filter data points corresponding precisely to those selected years, turning grey for unselected periods.
* **Data Transformations:** Extensive data cleaning was performed in Pandas: timestamps were parsed from strings to datetime objects, invalid or zero-second durations were filtered out, and a logarithmic transformation (`np.log10`) was applied to `duration_seconds` to effectively handle extreme right-skewness and outliers.

---

## Project Resources
You can inspect the underlying code and raw source materials via the links below:

<a class="btn" href="https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/ufo-scrubbed-geocoded-time-standardized-00.csv" target="_blank">The Data</a>
<a class="btn" href="https://github.com/hp0525/hp0525.github.io/blob/main/python_notebooks/HW5_UFO_Analysis.ipynb" target="_blank">The Analysis</a>
