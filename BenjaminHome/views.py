from django.shortcuts import render

# Create your views here.
def home(request): 
    return render(request, 'home/home.html')

def pelis(request):
    peliculas_recomendadas = []
    for data_genero in (datos_accion(), datos_comedia(), datos_drama()):
        for pelicula in data_genero['peliculas'][:3]:
            pelicula['genero'] = data_genero['genero']
            peliculas_recomendadas.append(pelicula)

    return render(request, 'home/peliculas.html', {
        'genero': 'Películas',
        'peliculas': peliculas_recomendadas,
    })

def accion(request):
    return render(request, 'home/accion.html', datos_accion())

def drama(request):
    return render(request, 'home/drama.html', datos_drama())

def comedia(request):
    return render(request, 'home/comedia.html', datos_comedia())

def datos_accion():
    data = {
        'genero': 'Acción',
        'peliculas': [
            {
                'nombre': 'Gladiator',
                'año': 2000,
                'imagen': 'accion/gladiador.jpg',
                'descripcion': 'Un victorioso general romano es traicionado tras la muerte del emperador y reducido a la esclavitud, jurando venganza en el Coliseo.'
            },
            {
                'nombre': 'The Dark Knight',
                'año': 2008,
                'imagen': 'accion/batman.jpg',
                'descripcion': 'Batman enfrenta su mayor desafío cuando el Guasón desata el caos psicológico y la anarquía en la ciudad de Gótica.'
            },
            {
                'nombre': 'Inception',
                'año': 2010,
                'imagen': 'accion/inception.jpg',
                'descripcion': 'Un ladrón especializado en robar secretos del subconsciente durante el sueño recibe la misión de implantar una idea en la mente de un objetivo.'
            },
            {
                'nombre': 'John Wick',
                'año': 2014,
                'imagen': 'accion/john.jpg',
                'descripcion': 'Un exasesino a sueldo sale de su retiro para cazar a los criminales que le quitaron lo único que le quedaba de su difunta esposa.'
            },
            {
                'nombre': 'Mad Max: Fury Road',
                'año': 2015,
                'imagen': 'accion/madmax.jpg',
                'descripcion': 'En un desierto postapocalíptico, Max se une a Imperator Furiosa para escapar de un tirano y sus huestes a bordo de un camión blindado.'
            },
            {
                'nombre': 'Spider-Man: Into the Spider-Verse',
                'año': 2018,
                'imagen': 'accion/spider.jpg',
                'descripcion': 'El joven Miles Morales asume la identidad de Spider-Man y debe unir fuerzas con versiones de otras dimensiones para detener una amenaza multiversal.'
            },
            {
                'nombre': 'Top Gun: Maverick',
                'año': 2022,
                'imagen': 'accion/top_gun.jpg',
                'descripcion': 'Tras más de 30 años de servicio, Pete "Maverick" Mitchell entrena a una graduación de pilotos de élite para una misión casi imposible.'
            },
            {
                'nombre': 'Misión: Imposible - Sentencia Mortal',
                'año': 2023,
                'imagen': 'accion/mision.jpg',
                'descripcion': 'Ethan Hunt y su equipo deben enfrentarse a una poderosa inteligencia artificial fuera de control mientras intentan evitar que caiga en manos de una peligrosa organización.'
            },
            {
                'nombre': 'Dune: Part Two',
                'año': 2024,
                'imagen': 'accion/dune.jpg',
                'descripcion': 'Paul Atreides se une a Chani y a los Fremen mientras busca venganza contra los conspiradores que destruyeron a su familia.'
            },
            {
                'nombre': 'Deadpool & Wolverine',
                'año': 2024,
                'imagen': 'accion/deadpool.jpg',
                'descripcion': 'Un apático Deadpool recluta a un reacio Wolverine de otro universo para enfrentar una amenaza existencial que pone en riesgo su mundo.'
            },
        ]
    }
    return data

def datos_comedia():
    data = {
        'genero': 'Comedia',
        'peliculas': [
{
                'nombre': 'La familia de mi novia',
                'año': 2000,
                'imagen': 'comedia/familia.jpg',
                'descripcion': 'Un enfermero intenta causar una buena impresión a los padres de su novia durante un fin de semana, pero su suegro es un exagente de la CIA implacable.'
            },
            {
                'nombre': 'Super cool',
                'año': 2007,
                'imagen': 'comedia/supercool.jpg',
                'descripcion': 'Dos amigos de la preparatoria con pocas habilidades sociales intentan conseguir alcohol para una fiesta antes de graduarse e ir a universidades distintas.'
            },
            {
                'nombre': '¿Qué pasó ayer?',
                'año': 2009,
                'imagen': 'comedia/quepaso.jpg',
                'descripcion': 'Tres amigos despiertan en Las Vegas tras una salvaje despedida de soltero sin recordar nada de la noche anterior y descubren que el novio ha desaparecido.'
            },
            {
                'nombre': 'Son como niños',
                'año': 2010,
                'imagen': 'comedia/soncomo1.jpg',
                'descripcion': 'Cinco amigos de la infancia se reúnen 30 años después junto a sus familias para pasar el fin de semana del 4 de julio tras la muerte de su entrenador de básquetbol.'
            },
            {
                'nombre': 'Comando Especial',
                'año': 2012,
                'imagen': 'comedia/comando.jpg',
                'descripcion': 'Dos policías novatos son enviados de encubierto a una escuela secundaria para desmantelar una red de narcotráfico adoptando identidades de estudiantes.'
            },
            {
                'nombre': 'Son como niños 2',
                'año': 2013,
                'imagen': 'comedia/soncomo2.jpg',
                'descripcion': 'Lenny se muda con su familia de regreso a su pueblo natal para estar cerca de sus amigos, pero enfrentan nuevos retos en el último día de clases.'
            },
            {
                'nombre': 'Noche de juegos',
                'año': 2018,
                'imagen': 'comedia/noche.jpg',
                'descripcion': 'Un grupo de amigos que se reúne periódicamente para noches de juegos se ve envuelto en un misterio real cuando uno de ellos es secuestrado por ladrones.'
            },
{
                'nombre': '¿Y dónde están las rubias?',
                'año': 2004,
                'imagen': 'comedia/dondeestan.jpg',
                'descripcion': 'Dos agentes del FBI caídos en desgracia se disfrazan de dos jóvenes millonarias para protegerlas de un plan de secuestro y salvar sus carreras.'
            },
            {
                'nombre': 'Free Guy: Tomando el control',
                'año': 2021,
                'imagen': 'comedia/free.jpg',
                'descripcion': 'Un cajero de banco descubre que en realidad es un personaje secundario sin importancia dentro de un videojuego de mundo abierto.'
            },
            {
                'nombre': 'Barbie',
                'año': 2023,
                'imagen': 'comedia/barbie.jpg',
                'descripcion': 'Sufriendo una crisis existencial inesperada, Barbie abandona su mundo perfecto en Barbieland para emprender un viaje hacia el mundo real junto a Ken.'
            },
        ]
    }
    return data

def datos_drama():
    data = {
        'genero': 'Drama',
        'peliculas': [
           {
                'nombre': 'En busca de la felicidad',
                'año': 2006,
                'imagen': 'drama/busca.jpg',
                'descripcion': 'Un padre que enfrenta graves dificultades económicas lucha por construir un futuro mejor para su hijo mientras intenta salir adelante.'
            },

            {
                'nombre': 'El niño con el pijama de rayas',
                'año': 2008,
                'imagen': 'drama/nino.jpg',
                'descripcion': 'Un niño alemán desarrolla una amistad con un niño judío que vive al otro lado de la cerca de un campo de concentración durante la Segunda Guerra Mundial.'
            },

            {
                'nombre': 'La red social',
                'año': 2010,
                'imagen': 'drama/red.jpg',
                'descripcion': 'Mark Zuckerberg crea una de las redes sociales más importantes del mundo, mientras enfrenta conflictos con sus amigos y antiguos socios.'
            },

            {
                'nombre': 'El lobo de Wall Street',
                'año': 2013,
                'imagen': 'drama/lobo.jpg',
                'descripcion': 'Un ambicioso corredor de bolsa construye una enorme fortuna mediante negocios fraudulentos, llevando una vida marcada por los excesos y la corrupción.'
            },

            {
                'nombre': 'Whiplash: Música y obsesión',
                'año': 2014,
                'imagen': 'drama/whi.jpg',
                'descripcion': 'Un joven baterista busca convertirse en uno de los mejores músicos mientras soporta las exigencias extremas de un exigente profesor.'
            },

            {
                'nombre': 'La La Land: Ciudad de sueños',
                'año': 2016,
                'imagen': 'drama/la.jpg',
                'descripcion': 'Un músico de jazz y una aspirante a actriz se enamoran mientras persiguen sus sueños en la ciudad de Los Ángeles.'
            },

            {
                'nombre': 'Nace una estrella',
                'año': 2018,
                'imagen': 'drama/nace.jpg',
                'descripcion': 'Un famoso músico descubre el talento de una joven cantante y la ayuda a alcanzar la fama mientras ambos enfrentan los problemas de sus propias vidas.'
            },

            {
                'nombre': 'Joker',
                'año': 2019,
                'imagen': 'drama/joker.jpg',
                'descripcion': 'Un hombre marginado por la sociedad enfrenta el rechazo y la soledad hasta convertirse en una figura criminal que aterroriza Ciudad Gótica.'
            },

            {
                'nombre': 'La ballena',
                'año': 2022,
                'imagen': 'drama/ballena.jpg',
                'descripcion': 'Un profesor que vive aislado debido a su grave obesidad intenta reconstruir la relación con su hija adolescente antes de que sea demasiado tarde.'
            },

            {
                'nombre': 'Anatomía de una caída',
                'año': 2023,
                'imagen': 'drama/anatomia.jpg',
                'descripcion': 'Una escritora se convierte en la principal sospechosa tras la misteriosa muerte de su esposo y debe demostrar su inocencia durante un complejo juicio.'
            },
        ]
    }
    return data