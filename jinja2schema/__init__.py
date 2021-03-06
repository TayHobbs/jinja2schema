# coding: utf-8
"""

jinja2schema
============

Type inference for Jinja2 templates.

See http://jinja2schema.rtfd.org/ for documentation.

:copyright: (c) 2014 Anton Romanovich
:license: BSD

"""

__title__ = 'jinja2schema'
__author__ = 'Anton Romanovich'
__license__ = 'BSD'
__copyright__ = 'Copyright 2014 Anton Romanovich'
__version__ = '0.1.1'
__version_info__ = tuple(int(i) for i in __version__.split('.'))


from .config import Config
from .core import (parse, infer, infer_from_ast, to_json_schema,
                   JSONSchemaDraft4Encoder, StringJSONSchemaDraft4Encoder)
from .exceptions import InferException, MergeException, InvalidExpression, UnexpectedExpression
