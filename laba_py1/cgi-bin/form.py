#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage()

text1 = form.getvalue("fruit")

print("Content-type: text/html\n")
print("<p></p><p>Любимый фрукт: {}</p>".format(text1))
print("""<!DOCTYPE HTML>
<html>
	
    	<head>
    	<meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
         <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
        integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        	<title>Любимый фрукт</title>
    	</head>
    <body>
	<div>
	
        	<form action="/cgi-bin/form.py">
            		<select class="form-control mb-2" name="fruit" onchange="this.form.submit();">
                		<option value ="Выберите">Развернуть список</option>
                		<option value ="Яблоко">Яблоко</option>
                		<option value ="Апельсин">Апельсин</option>
                		<option value ="Банан">Банан</option>
                		<option value ="Гранат">Гранат</option>
                		<option value ="Персик">Персик</option>
            		</select>
				<button class="btn btn btn-primary mr-1" type="submit">Отправить</button>
            	<input  class="btn btn-primary" type="submit" value="Сбросить" name ="reset">
        	</form>
    
	</div>	
	</body>


</html>""")
