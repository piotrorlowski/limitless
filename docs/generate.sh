#! /bin/bash

pandoc README.md -o README.pdf --pdf-engine=wkhtmltopdf --template=docs/template.html
