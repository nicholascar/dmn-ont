import xml.etree.ElementTree as ET
from rdflib import Graph, URIRef, RDF, RDFS, XSD, OWL, Literal
import re
import os


def make_owl_class(graph, ns, class_name):
    this_uri = URIRef(ns + class_name)
    graph.add((this_uri, RDF.type, OWL.Class))
    label = ' '.join(re.findall('[A-Z][^A-Z]*', class_name))
    graph.add((this_uri, RDFS.label, Literal(label, datatype=XSD.string)))
    graph.add((this_uri, RDFS.isDefinedBy, URIRef(ns)))


def make_dmn_classes(g, ns, xml_file):
    tree = ET.parse(xml_file)

    for c in tree.findall(
            './/packagedElement[@xmi:type="uml:Class"]',
            namespaces={
                'xmi': "http://www.omg.org/spec/XMI/20110701",
                'uml': "http://www.omg.org/spec/UML/20110701"
            }
    ):
        make_owl_class(g, ns, c.get('name'))

        if c.get('name') is not None:
            make_properties_for_class(g, ns, c)


def make_properties_for_class(graph, ns, parent):
    for child in parent:
        if child.tag == 'ownedAttribute' \
                and child.get('{http://www.omg.org/spec/XMI/20110701}type') == 'uml:Property' \
                and child.get('name') is not None:
                make_owl_property(graph, ns, child, parent)


def camel_case_split(s):
    matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', s)
    return [m.group(0) for m in matches]


def make_owl_property(graph, ns, node, parent):
    # substitution in order to remove an extra linbreak for input
    this_uri = URIRef(ns + re.sub('\s+', '', node.get('name')))
    graph.add((this_uri, RDFS.isDefinedBy, URIRef(ns)))
    graph.add((this_uri, RDFS.domain, URIRef(ns + parent.get('name'))))
    label = ' '.join(camel_case_split(node.get('name').strip())).lower()
    graph.add((this_uri, RDFS.label, Literal(label, datatype=XSD.string)))

    for n in node:
        if n.tag == 'lowerValue':
            pass  # there seems to be no actual lower value set, only a type: uml:LiteralInteger
        elif n.tag == 'type':
            if n.get('href') == 'http://www.omg.org/spec/UML/20110701/PrimitiveTypes.xmi#String':
                graph.add((this_uri, RDF.type, OWL.DatatypeProperty))
                graph.add((this_uri, RDFS.range, XSD.string))
            elif node.get('href') == 'http://www.omg.org/spec/UML/20110701/PrimitiveTypes.xmi#Boolean':
                graph.add((this_uri, RDF.type, OWL.DatatypeProperty))
                graph.add((this_uri, RDFS.range, XSD.boolean))
            else:
                graph.add((this_uri, RDF.type, OWL.ObjectProperty))


def make_dmn_properties(g, ns, xml_file):
    tree = ET.parse(xml_file)

    for c in tree.findall(
            './/ownedAttribute[@xmi:type="uml:Property"]',
            namespaces={
                'xmi': "http://www.omg.org/spec/XMI/20110701",
                'uml': "http://www.omg.org/spec/UML/20110701"
            }):
        if c.get('name') is not None:
            print(c.getparent())
            make_owl_property(g, ns, c)


if __name__ == '__main__':
    this_dir = os.path.dirname(os.path.realpath(__file__))
    g = Graph()
    ns = 'http://promsns.org/def/dmn#'
    xml_file = os.path.join(os.path.dirname(this_dir), 'dmn.xmi')
    make_dmn_classes(g, ns, xml_file)

    # write graph to file
    open(os.path.join(this_dir, './dmn-body.ttl'), 'w').write(g.serialize(format='turtle').decode('utf-8'))
