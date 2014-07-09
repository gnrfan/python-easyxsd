from lxml import etree

def xml_from_string(xmlstr):
    """
    Returns an lxml.etree._ElementTree object from a string
    containing a valid XML document.
    """
    try:
        return etree.XML(str(xmlstr).strip())
    except etree.XMLSyntaxError:
        return None


def xml_from_file(filepath):
    """
    Returns an lxml.etree._ElementTree object from a file
    containing a valid XML document.
    """
    try:
        return etree.parse(filepath)
    except etree.XMLSyntaxError:
        return None


def xsd_from_string(xsdstr):
    """
    Returns an lxml.etree.XMLSchema object from a string
    containing a valid XML document.
    """
    try:
        xml = etree.XML(str(xsdstr).strip())
        return etree.XMLSchema(xml)
    except etree.XMLSyntaxError:
        return None


def xsd_from_file(filepath):
    """
    Returns an lxml.etree.XMLSchema object from a file
    containing a valid XML document.
    """
    try:
        xml = etree.parse(filepath)
        return etree.XMLSchema(xml)
    except etree.XMLSyntaxError:
        return None

def validate(xml, xsd):
    """
    Receives an lxml.etree._ElementTree object as first parameter
    and an lxml.etree.XMLSchema object as second parameter and
    returns True or False respectively as the XSD validation of the
    XML succeeds or fails.
    """
    return xsd.validate(xml)

def validate_from_strings(xmlstr, xsdstr):
    """
    Receives a string containing a valid XML document as first parameter
    and another string containing a valid XSD document as second parameter
    and validates the first according to the latter returning True or False
    respectively as the validation succeeds or fails.
    """
    xml = xml_from_string(xmlstr)
    xsd = xsd_from_string(xsdstr)
    return validate(xml, xsd)

def validate_from_files(xmlfilepath, xsdfilepath):
    """
    Receives a string with a file path to a valid XML document 
    as first parameter and another string with a file path to a valid
    XSD document as second parameter and validates the first according 
    to the latter returning True or False respectively as the validation
    succeeds or fails.
    """
    xml = xml_from_file(xmlfilepath)
    xsd = xsd_from_file(xsdfilepath)
    return validate(xml, xsd)

def validate_xml_string_from_xsd_file(xmlstr, xsdfilepath):
    """
    Validates a string containing an XML document as the first parameter
    with an XSD document contained in the file path passed as the
    second parameter.
    """
    xml = xml_from_string(xmlstr)
    xsd = xsd_from_file(xsdfilepath)
    return validate(xml, xsd)

def validate_with_errors(xml, xsd):
    """
    Returns a tuple with a boolean product of the XSD validation as
    the first element and the error log object as the second element.
    """
    validation = xsd.validate(xml)
    return (validation, xsd.error_log, )

def xsd_error_as_simple_string(error):
    """
    Returns a string based on an XSD error object with the format
    LINE:COLUMN:LEVEL_NAME:DOMAIN_NAME:TYPE_NAME:MESSAGE.
    """
    parts = [
        error.line,
        error.column,
        error.level_name,
        error.domain_name,
        error.type_name,
        error.message
    ]
    return ':'.join([str(item) for item in parts])

def xsd_error_log_as_simple_strings(error_log):
    """
    Returns a list of strings representing all the errors of an XSD
    error log object.
    """
    return [xsd_error_as_simple_string(e) for e in error_log]
