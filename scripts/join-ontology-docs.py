from rdflib import Graph
import os

if __name__ == '__main__':
    this_dir = os.path.dirname(os.path.realpath(__file__))
    dmn_header_file = os.path.join(this_dir, 'dmn-header.ttl')
    dmn_body_file = os.path.join(this_dir, 'dmn-body.ttl')
    g = Graph().parse(dmn_header_file, format='turtle') + Graph().parse(dmn_body_file, format='turtle')

    open(os.path.join(this_dir, 'dmn-raw.ttl'), 'w').write(g.serialize(format='turtle').decode('utf-8'))
