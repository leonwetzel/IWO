# IWO
Repository containing code for both data preparation and analysis of police statements
from the Municipality of Groningen. All scripts have been developed by Leon Wetzel, for
the course *Introduction to research methods* of the University of Groningen.

## Preparation

The script `main.python` contains code for cleaning and preparing the data file from the
 open data portal of the Municipality of Groningen. The first two rows are merged and
 form the column names. Other operations include the removal of unnecessary rows and the
  addition of a row for the designation of area types.

## Analysis

The page ```index.html``` is the result of the R markdown script that was created for
the analysis and display of the results of the statistical tests. It contains the output
from the various R scripts that have been called upon the data, such as t-tests and
Mann-Whitney U tests. Various graphs and tables are also displayed throughout the page
 for clarification.
