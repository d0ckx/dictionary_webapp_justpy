import justpy as jp

from webapp.about_page import About
from webapp.dictionary_page import Dictionary
from webapp.homepage import Home

jp.Route(Home.path, Home.serve)
jp.Route(About.path, About.serve)
jp.Route(Dictionary.path, Dictionary.serve)

jp.justpy()
