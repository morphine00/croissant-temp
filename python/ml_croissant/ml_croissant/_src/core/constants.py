"""constants module."""

from etils import epath
import rdflib
from rdflib import namespace
from rdflib import term

# MLCommons-defined URIs (still draft).
ML_COMMONS = rdflib.Namespace("http://mlcommons.org/schema/")
ML_COMMONS_APPLY_TRANSFORM = ML_COMMONS.applyTransform
ML_COMMONS_CSV_COLUMN = ML_COMMONS.csvColumn
ML_COMMONS_DATA = ML_COMMONS.data
ML_COMMONS_DATA_EXTRACTION = ML_COMMONS.dataExtraction
ML_COMMONS_DATA_TYPE = ML_COMMONS.dataType
ML_COMMONS_FILE_PROPERTY = ML_COMMONS.fileProperty
ML_COMMONS_FIELD = ML_COMMONS.field
ML_COMMONS_FIELD_TYPE = ML_COMMONS.Field
# ML_COMMONS.format is understood as the `format` method on the class Namespace.
ML_COMMONS_FORMAT = term.URIRef("http://mlcommons.org/schema/format")
ML_COMMONS_INCLUDES = ML_COMMONS.includes
ML_COMMONS_JSON_PATH = ML_COMMONS.jsonPath
ML_COMMONS_PATH = ML_COMMONS.path
ML_COMMONS_RECORD_SET = ML_COMMONS.recordSet
ML_COMMONS_RECORD_SET_TYPE = ML_COMMONS.RecordSet
ML_COMMONS_REFERENCES = ML_COMMONS.references
ML_COMMONS_REGEX = ML_COMMONS.regex
# ML_COMMONS.replace is understood as the `replace` method on the class Namespace.
ML_COMMONS_REPLACE = term.URIRef("http://mlcommons.org/schema/replace")
ML_COMMONS_SEPARATOR = ML_COMMONS.separator
ML_COMMONS_SOURCE = ML_COMMONS.source
ML_COMMONS_SUB_FIELD = ML_COMMONS.subField

# RDF standard URIs.
# For "@type" key:
RDF_TYPE = namespace.RDF.type

# Schema.org standard URIs.
SCHEMA_ORG_CITATION = namespace.SDO.citation
SCHEMA_ORG_CONTAINED_IN = namespace.SDO.containedIn
SCHEMA_ORG_CONTENT_SIZE = namespace.SDO.contentSize
SCHEMA_ORG_CONTENT_URL = namespace.SDO.contentUrl
SCHEMA_ORG_DATASET = namespace.SDO.Dataset
SCHEMA_ORG_DATA_TYPE_BOOL = namespace.SDO.Boolean
SCHEMA_ORG_DATA_TYPE_DATE = namespace.SDO.Date
SCHEMA_ORG_DATA_TYPE_FLOAT = namespace.SDO.Float
SCHEMA_ORG_DATA_TYPE_INTEGER = namespace.SDO.Integer
SCHEMA_ORG_DATA_TYPE_TEXT = namespace.SDO.Text
SCHEMA_ORG_DATA_TYPE_URL = namespace.SDO.URL
SCHEMA_ORG_DESCRIPTION = namespace.SDO.description
SCHEMA_ORG_DISTRIBUTION = namespace.SDO.distribution
SCHEMA_ORG_EMAIL = namespace.SDO.email
SCHEMA_ORG_ENCODING_FORMAT = namespace.SDO.encodingFormat
SCHEMA_ORG_LICENSE = namespace.SDO.license
SCHEMA_ORG_NAME = namespace.SDO.name
SCHEMA_ORG_SHA256 = namespace.SDO.sha256
SCHEMA_ORG_URL = namespace.SDO.url

# Schema.org URIs that do not exist yet in the standard.
SCHEMA_ORG = rdflib.Namespace("https://schema.org/")
SCHEMA_ORG_KEY = SCHEMA_ORG.key
SCHEMA_ORG_FILE_OBJECT = SCHEMA_ORG.FileObject
SCHEMA_ORG_FILE_SET = SCHEMA_ORG.FileSet
SCHEMA_ORG_MD5 = SCHEMA_ORG.md5

# TODO(https://github.com/mlcommons/croissant/issues/171): schema.org URIs that should
# be migrated to mlcommons.org.
SCHEMA_ORG_IS_ENUMERATION = SCHEMA_ORG.isEnumeration
SCHEMA_ORG_LANGUAGE = SCHEMA_ORG["@language"]
SCHEMA_ORG_PARENT_FIELD = SCHEMA_ORG.parentField
SCHEMA_ORG_REPEATED = SCHEMA_ORG.repeated

# Croissant equivalent.
CROISSANT_APPLY_TRANSFORM = "apply_transform"
CROISSANT_CITATION = "citation"
CROISSANT_CONTAINED_IN = "contained_in"
CROISSANT_CONTENT_SIZE = "content_size"
CROISSANT_CONTENT_URL = "content_url"
CROISSANT_CSV_COLUMN = "csv_column"
CROISSANT_DATA = "data"
CROISSANT_DATA_EXTRACTION = "data_extraction"
CROISSANT_DATA_TYPE = "data_type"
CROISSANT_DESCRIPTION = "description"
CROISSANT_DISTRIBUTION = "distribution"
CROISSANT_ENCODING_FORMAT = "encoding_format"
CROISSANT_FIELD = "field"
CROISSANT_FILE_PROPERTY = "file_property"
CROISSANT_FORMAT = "format"
CROISSANT_INCLUDES = "includes"
CROISSANT_JSON_PATH = "json_path"
CROISSANT_LICENSE = "license"
CROISSANT_MD5 = "md5"
CROISSANT_NAME = "name"
CROISSANT_REFERENCES = "references"
CROISSANT_REGEX = "regex"
CROISSANT_REPLACE = "replace"
CROISSANT_SEPARATOR = "separator"
CROISSANT_SHA256 = "sha256"
CROISSANT_SOURCE = "source"
CROISSANT_URL = "url"

TO_CROISSANT = {
    ML_COMMONS_APPLY_TRANSFORM: CROISSANT_APPLY_TRANSFORM,
    ML_COMMONS_CSV_COLUMN: CROISSANT_CSV_COLUMN,
    ML_COMMONS_DATA_TYPE: CROISSANT_DATA_TYPE,
    ML_COMMONS_DATA: CROISSANT_DATA,
    ML_COMMONS_DATA_EXTRACTION: CROISSANT_DATA_EXTRACTION,
    ML_COMMONS_FIELD: CROISSANT_FIELD,
    ML_COMMONS_FILE_PROPERTY: CROISSANT_FILE_PROPERTY,
    ML_COMMONS_FORMAT: CROISSANT_FORMAT,
    ML_COMMONS_INCLUDES: CROISSANT_INCLUDES,
    ML_COMMONS_JSON_PATH: CROISSANT_JSON_PATH,
    ML_COMMONS_REFERENCES: CROISSANT_REFERENCES,
    ML_COMMONS_REGEX: CROISSANT_REGEX,
    ML_COMMONS_REPLACE: CROISSANT_REPLACE,
    ML_COMMONS_SEPARATOR: CROISSANT_SEPARATOR,
    ML_COMMONS_SOURCE: CROISSANT_SOURCE,
    SCHEMA_ORG_CITATION: CROISSANT_CITATION,
    SCHEMA_ORG_CONTAINED_IN: CROISSANT_CONTAINED_IN,
    SCHEMA_ORG_CONTENT_SIZE: CROISSANT_CONTENT_SIZE,
    SCHEMA_ORG_CONTENT_URL: CROISSANT_CONTENT_URL,
    SCHEMA_ORG_DESCRIPTION: CROISSANT_DESCRIPTION,
    SCHEMA_ORG_DISTRIBUTION: CROISSANT_DISTRIBUTION,
    SCHEMA_ORG_ENCODING_FORMAT: CROISSANT_ENCODING_FORMAT,
    SCHEMA_ORG_LICENSE: CROISSANT_LICENSE,
    SCHEMA_ORG_MD5: CROISSANT_MD5,
    SCHEMA_ORG_NAME: CROISSANT_NAME,
    SCHEMA_ORG_SHA256: CROISSANT_SHA256,
    SCHEMA_ORG_URL: CROISSANT_URL,
}

FROM_CROISSANT = {v: k for k, v in TO_CROISSANT.items()}

CROISSANT_CACHE = epath.Path("~/.cache/croissant").expanduser()
DOWNLOAD_PATH = CROISSANT_CACHE / "download"
EXTRACT_PATH = CROISSANT_CACHE / "extract"
