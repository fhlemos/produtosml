#!/bin/bash

KEYWORD=""
FILE_DEFAULT="result.json"

echo "The result will be saved in the file: ${FILE_DEFAULT}"
read -p "Enter keyword for search: " KEYWORD

scrapy crawl mercadolivre -a keyword=${KEYWORD} -o ${FILE_DEFAULT}

echo "Done (${SECONDS} seconds)"
