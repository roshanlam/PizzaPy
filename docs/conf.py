
extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.coverage']

templates_path = ['_templates']


source_suffix = '.rst'


master_doc = 'index'

# General information about the project.
project = u'pizzapy'
copyright = u'2019, Roshan Lamichhane'
author = u'Roshan Lamichhane'


version = u'0.0.2'

release = u'0.0.2'

language = None

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


pygments_style = 'sphinx'

todo_include_todos = False


html_theme = 'alabaster'



html_static_path = ['_static']


html_sidebars = {
    '**': [
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}


htmlhelp_basename = 'pizzapydoc'



latex_elements = {
   
}

latex_documents = [
    (master_doc, 'pizzapy.tex', u'pizzapy Documentation',
     u'Arie van Luttikhuizen, Grant Gordon', 'manual'),
]



man_pages = [
    (master_doc, 'pizzapy', u'pizzapy Documentation',
     [author], 1)
]

texinfo_documents = [
    (master_doc, 'pizzapy', u'pizzapy Documentation',
     author, 'pizzapy', 'One line description of project.',
     'Miscellaneous'),
]
