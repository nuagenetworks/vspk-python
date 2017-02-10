# -*- coding: utf-8 -*-

import sphinx_rtd_theme

extensions = []
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'VSPK'
copyright = u'2016, Nuage Networks'
author = u'Nuage Networks'
version = u'4.0.7'
release = u'1'
language = None
exclude_patterns = []
pygments_style = 'sphinx'
todo_include_todos = False

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme_options = {
    'sticky_navigation': False,
}

htmlhelp_basename = 'VSPK'
html_search_language = 'en'
html_show_sphinx = False

latex_documents = [
    (master_doc, 'VSPK.tex', u'VSPK Documentation',
     u'Nuage Networks', 'manual'),
]
man_pages = [
    (master_doc, 'VSPK', u'VSPK Documentation',
     [author], 1)
]

texinfo_documents = [
    (master_doc, 'VSPK', u'VSPK Documentation',
     author, 'Nuage Networks', 'VSD API Python client',
     'Miscellaneous'),
]
