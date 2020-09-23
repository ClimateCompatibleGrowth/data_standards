# data_standards
Data Standards for Energy System Planning Tools and Methodologies

This project will implement the u4RIA principles. 

Below I outline a number of practical implications of the 7 principles for which U4RIA is an acronym:

1. ubuntu (community)
2. retrievability
3. repeatability
4. reusability
5. reconstructability
6. interoperability
7. auditability

For an explaination of u4RIA, see the paper (forthcoming).

## ubuntu (community)

* Design project to allow transfer of data and code to stakeholders
* Involve stakeholders in development of models, assumptions, scenarios and results
* Build capacity to better understand, use and promote use of tools, methods, data and results

## retrievability

* Ensure original data can be access upon close of the project
* Copy and archive data that comes from unreliable resources
* Archive data and use an appropriate license

## repeatability

* Use a workflow management tool (such as snakemake) to automate each of the steps in the analysis
* Document which version of each software package is required to run the analysis
* Use an environment manager such as miniconda or docker to ensure that the analysis can
  be easily reused

## reusability

* Document and publish assumptions together with results
* Publish data behind results with a permissive license allowing reuse (e.g. CC-BY 4.0)
* Publish source code under an open-source license (e.g. MIT, Apache 2.0 etc.)
* Publish documentation on how to re-run the analysis

## reconstructability

* Document which data was used for which purpose (comes for free if you use a workflow manager)

## interoperability

* Do not use proprietary file formats to store data (such as Excel *.xlsx)
* Where possible, use csv files, or an open-source format such as feather, HD5
* Ideally, use Tabular Data Packages which store data in csvs and metadata in a JSON file
* Store data in CSV files in long format (e.g. headers for GDP statistics should be `Country`,`Year`,`Value`
  rather than `Country`, `GDP`, `1990`, `1995`, `2000`, `2005`, `2010`)

## auditability

* Design the project with an audit in mind. How can you change your work patterns to make it easier for an external
  partners to see what you have done?
* Comes for free with many of the steps above.