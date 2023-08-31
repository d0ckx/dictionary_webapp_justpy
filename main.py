import inspect

import justpy as jp

from webapp import page
from webapp.about_page import About
from webapp.dictionary_page import Dictionary
from webapp.homepage import Home

imports = list(globals().values())

for object in imports:
    if inspect.isclass(object):
        if issubclass(object, page.Page) and object is not page.Page:
            jp.Route(object.path, object.serve)

jp.justpy()
