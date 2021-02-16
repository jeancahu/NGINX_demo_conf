#!/bin/bash

#$QUERY_STRING

now="$(date)"

echo \
"Content-type: text/html

<html>
    <head>
         <title>Hello World - CGI app</title>
    </head>
    <body>

         <h2>Hello World!</h2>
         Computer name : ${HOSTNAME}<br/>
         The current date and time : ${now}<br/>
    </body>
</html>"
