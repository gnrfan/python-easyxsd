EasyXSD
=======

Easy XML Schema Definition (XSD) validation of XML documents based on ```lxml```.

Usage:

```python
>>> from easyxsd import *
>>> xsd = xsd_from_file('/path/to/files/definitions.xsd')
>>> xml = xml_from_file('/path/to/files/valid-example.xml')
>>> xsd.validate(xml)
True
>>> xml = xml_from_file('/path/to/files/invalid-example.xml')
>>> xsd.validate(xml)
False
```

The ```xml``` and ```xsd``` objects are ```lxml```'s ```lxml.etree._ElementTree```
and ```lxml.etree.XMLSchema``` objects respectively.

More information on the available API:

    **validate(xml, xsd)**
        Receives an lxml.etree._ElementTree object as first parameter
        and an lxml.etree.XMLSchema object as second parameter and
        returns True or False respectively as the XSD validation of the
        XML succeeds or fails.
    
    **validate_from_files(xmlfilepath, xsdfilepath)**
        Receives a string with a file path to a valid XML document 
        as first parameter and another string with a file path to a valid
        XSD document as second parameter and validates the first according 
        to the latter returning True or False respectively as the validation
        succeeds or fails.
    
    **validate_from_strings(xmlstr, xsdstr)**
        Receives a string containing a valid XML document as first parameter
        and another string containing a valid XSD document as second parameter
        and validates the first according to the latter returning True or False
        respectively as the validation succeeds or fails.

    **validate_with_errors(xml, xsd)**
        Returns a tuple with a boolean product of the XSD validation as
        the first element and the error log object as the second element.
    
    **validate_xml_string_from_xsd_file(xmlstr, xsdfilepath)**
        Validates a string containing an XML document as the first parameter
        with an XSD document contained in the file path passed as the
        second parameter.
    
    **xml_from_file(filepath)**
        Returns an lxml.etree._ElementTree object from a file
        containing a valid XML document.
    
    **xml_from_string(xmlstr)**
        Returns an lxml.etree._ElementTree object from a string
        containing a valid XML document.
    
    **xsd_error_as_simple_string(error)**
        Returns a string based on an XSD error object with the format
        LINE:COLUMN:LEVEL_NAME:DOMAIN_NAME:TYPE_NAME:MESSAGE.
    
    **xsd_error_log_as_simple_strings(error_log)**
        Returns a list of strings representing all the errors of an XSD
        error log object.

(c) 2014 - Antonio Ognio <antonio@ognio.com>
