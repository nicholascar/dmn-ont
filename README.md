# DMN-O
An [OWL](https://en.wikipedia.org/wiki/Web_Ontology_Language) ontology version of Decision Modelling and Notation (DMN) ([spec v1.1](http://www.omg.org/spec/DMN/1.1)).

This ontology contains classes for all of the elements presented in the DMN specification. In that document they are presented as UML class objects, the XML Metadata Interchange (XMI) file for which is online at <http://www.omg.org/spec/DMN/20151101/dmn.xmi> and copied to this repository [dmn.xmi](dmn.xmi).

The purpose of this OWL version of DMN 1.1 is manifold. It will enable:

* closer comparison of DMN to other OWL-based models
	* such as the Provenance Ontology [PROV-O](https://www.w3.org/TR/prov-o/) and the [Decision Ontology](https://github.com/nicholascar/decision-o).
* testing of DMN within open source automated systems
	* within RDF graph databases
	* with the SPARQL query language
* establishing requirements, if any, for a future decision modelling system
	* that incorporates aspects of other decision modelling sytems, not just DMN
	

## Ontology document
Turtle format: [dmn.ttl](dmn.ttl)  
HTML format: [dmn.html](dmn.html)

The canonical location of this ontology online is:

<http://promsns.org/def/dmn>  

This ontology will be versioned alongside DMN so the first and current (as of June, 2017) version of this ontology is 1.1 in order to align with DMN 1.1.


## Processing scripts
Python 3.6 scripts are supplied to process the DMN XMI document into an OWL ontology. Those scripts are located in the [scripts/](scripts) folder. They only partly process the document and manual processing is required after script processing.


## Examples

*coming!*


## License
This ontology and all other content in this repository are licensed under the [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) (also [LICENSE](LICENSE)).


## Author and Contact
**Nicholas Car**  
Senior Experimental Scientist  
CSIRO Land & Water  
<nicholas.car@csiro.au>  
<http://orcid.org/0000-0002-8742-7730>
