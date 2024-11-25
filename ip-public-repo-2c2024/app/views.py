# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def index_page(request):
    return render(request, 'index.html')

# esta función obtiene 2 listados que corresponden a las imágenes de la API y los favoritos del usuario, y los usa para dibujar el correspondiente template.
# si el opcional de favoritos no está desarrollado, devuelve un listado vacío.
def home(request):
    images = services.getAllImages()
    favourite_list = []
    return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list })



def search(request):
    # Obtener el texto ingresado en el buscador
    search_msg = request.POST.get('query', '')

    if search_msg:  # si se ingresó algún texto
        images = services.getAllImages(search_msg) #busca las imagenes segun el texto
    else:  # si no se ingreso nada
        images = services.getAllImages()  # cargar todas las imagenes

    
    favourite_list = []

    # renderiza la misma plantilla home.html con las imagenes filtradas
    return render(request, 'home.html', {'images': images, 'favourite_list': favourite_list})



# Estas funciones se usan cuando el usuario está logueado en la aplicación.
@login_required
def getAllFavouritesByUser(request):
    favourite_list = []
    return render(request, 'favourites.html', { 'favourite_list': favourite_list })

@login_required
def saveFavourite(request):
    pass

@login_required
def deleteFavourite(request):
    pass

@login_required
def exit(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('login')