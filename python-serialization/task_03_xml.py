#!/usr/bin/python3
''' module documentation '''
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    '''
    function to serialise a Python dictionary and serialise it into XML
    
    Arguments:
        dictionary (dict): a Python dictionary
        filename (str): the file to print to
    '''
    root = ET.Element("root")
    for key in dictionary:
        ET.SubElement(root, key).text = dictionary[key]

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    '''
    function to take data from an XML file deserialise it
    
    Arguments:
        filename (str): the file to read from

    Returns:
        (dict): a deserialised python dictionary
    '''
    data = {}
    tree = ET.parse(filename)
    root = tree.getroot()
    for child in root:
        data[child.tag] = child.text
    return data
