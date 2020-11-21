import requests

url = "http://www.cmfchile.cl/institucional/mercados/entidad.php?mercado=V&rut=9559&grupo=&tipoentidad=FIRES&row=AAAw%20cAAhAABP4RAA3&vig=VI&control=svs&pestania=7"
url_2 = "http://www.cmfchile.cl"
cabeceras = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

datos = {
	'dia1' : '01',
	'mes1' : '01',
	'anio1' : '2020',
	'dia2' : '17',
	'mes2' : '10',
	'anio2' : '2020',
	'sub_consulta_fi' : 'Consultar',
	'enviado' : '1'

}




r = requests.post(url,headers=cabeceras,data=datos)

print(r.content.decode())


