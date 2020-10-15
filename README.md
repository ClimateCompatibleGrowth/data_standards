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

*Involve stakeholders in your project from the beginning*

* Design project to allow transfer of data and code to stakeholders
* Involve stakeholders in development of models, assumptions, scenarios and results
* Build capacity to better understand, use and promote use of tools, methods, data and results

## retrievability

*Ensure that data, source code and results can be easily found, accessed, downloaded and viewed*

* Ensure original data can be accessed upon close of the project
* Copy and archive data that comes from unreliable resources
* Archive data (e.g. on Zenodo), register a DOI, and use an appropriate data license

## repeatability

*Ensure that results can be reproduced from data and assumptions, ideally automatically*

* Use a workflow management tool (such as [snakemake](https://snakemake.readthedocs.io/en/stable/)) 
  to automate each of the steps in the analysis
* Document which version of each software package is required to run the analysis
* Use an environment manager such as [miniconda](https://docs.conda.io/en/latest/miniconda.html), 
  [docker](https://www.docker.com/), or [singularity](https://sylabs.io/) to ensure that the analysis can
  be easily reused

## reusability

*Ensure the data, results and source code can be used by others*

* Document and publish assumptions together with results
* Publish data behind results with a permissive license allowing reuse (e.g. CC-BY 4.0)
* Publish source code under an open-source license (e.g. MIT, Apache 2.0 etc.)
* Publish documentation on how to re-run the analysis
* Use [semantic versioning](https://semver.org/) to tag your source code
* Use version control e.g. [git and Github](http://github.com) to track the history of your source code

## reconstructability

*Ensure that an entire analysis can be replicated, through documentation of primary data collection, processing, models*

* Document collection and processing of primary data
* Adopt a modular approach to analysis which allows interchange of data and models
* Use a workflow management system to automate, version and document the generation of results from data and models

## interoperability

*Enable the transfer of data, assumptions and results to other projects, analyses and models*

* Do not use proprietary file formats to store data (such as Excel *.xlsx)
* Where possible, use csv files, or an open-source format such as feather, HD5
* Ideally, use [Tabular Data Packages](https://specs.frictionlessdata.io/tabular-data-package/#language) 
  which store data in comma-separated values (CSV) format and metadata in a JSON file
* Store data in CSV files in long format (e.g. headers for GDP statistics should be `Country`,`Parameter`,`Year`,`Value`
  rather than `Country`,`1990`, `1995`, `2000`, `2005`, `2010`)
* Use existing standards, for example, adopt ISO conventions for [country codes](https://github.com/datasets/country-codes), 
  always use SI units

## auditability

*Work transparently and openly*

* Design the project with an audit in mind. How can you change your work patterns to make it easier for an external
  partners to see what you have done?
* Comes for free with many of the steps above.

## License

This text is licensed under a CC-BY-4.0 Attribution license.
