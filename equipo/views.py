from django.shortcuts import render


def portafolio_view(request):
    integrantes = [
        {
            'nombre': 'Nicolay',
            'foto': 'equipo/foto1.jpg',
            'descripcion': 'Estudiante y trabajador,.',
            'hobbies': ['Amante de mis gatos', 'Videojuegos', 'Anime'],
            'deportes': ['Fútbol', 'Trecking'],
            'musica': ['Rock', 'Electrónica', 'Rap', 'de todo un poco'],
            'correo': 'nicolayamon@gmail.com',
            'telefono': '+56995619788',
            'portafolio': 'https://nicolayamon.github.io/portafolioOficial/',
            'fondo': 'equipo/wallpaper1.jpg'   # Aquí el fondo para Niko
        },
        {
            'nombre': 'Rodrigo',
            'foto': 'equipo/foto2.jpg',
            'descripcion': 'Trabajo, estudio y tengo una PYME.',
            'hobbies': ['Diseño 3D', 'Tocar Piano', 'Viajar'],
            'deportes': ['Muay Thai', 'Kick Boxing'],
            'musica': ['Rock', 'Metal', 'Music Clásica'],
            'correo': 'rodrigo13barra@gmail.com',
            'telefono': '+56976035321',
            'portafolio': 'https://rodbrok.github.io/Portafolio/',
            'fondo': 'equipo/wallpaper2.jpg'   # Fondo para mi
        }
    ]

    return render(request, 'equipo/portafolio.html', {'integrantes': integrantes})
