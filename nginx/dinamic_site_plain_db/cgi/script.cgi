#!/bin/bash

numero="$( grep $QUERY_STRING ../plain.csv | cut -f 2 )"

now="$(date)"

echo \
"Content-type: text/html

<html>
    <head>
         <title>Hello World - CGI app</title>
    </head>
    <body>

         <h2>Cantidad de ${QUERY_STRING}</h2>
         ${numero}
    </body>
</html>"
