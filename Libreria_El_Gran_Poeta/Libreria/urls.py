"""
URL configuration for Libreria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from LibreriaApp import views
from soporteApp.views import crear_ticket_Jefe, crear_ticket_Bodeguero, detalle_ticket, ver_tickets
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),




    path('jefe_bodega/', views.jefe_bodegas_view, name='jefe_bodega'),

    path('jefe_bodega/CRUD/bodegas/', views.listadoBodega, name='listado_bodega'),
    path('jefe_bodega/CRUD/agregarBodega/', views.agregarBodega, name='agregar_bodega'),
    path('eliminarBodega/<int:id>', views.eliminarBodega, name='eliminar_bodega'), 
    path('actualizarBodega/<int:id>', views.actualizarBodega, name='actualizar_bodega'),
      

    path('jefe_bodega/CRUD/libros/', views.listadoLibros, name='listado_libros'),
    path('jefe_bodega/CRUD/agregarLibros/', views.agregarLibros, name='agregar_libros'),
    path('eliminarLibro/<int:id>', views.eliminarLibro, name='eliminar_libro'), 
    path('actualizarLibro/<int:id>', views.actualizarLibros, name='actualizar_libro'),

    
    
    path('jefe_bodega/CRUD/autores/', views.listadoAutores, name='listado_autores'),
    path('jefe_bodega/CRUD/agregarAutores/', views.agregarAutores, name='agregar_autores'),
    path('eliminarAutores/<int:id>', views.eliminarAutores, name='eliminar_autores'),  
    path('actualizarAutores/<int:id>', views.actualizarAutores, name='actualizar_autores'),
    
    path('informe/', views.generar_informe, name='generar_informe'),




    path('bodeguero/', views.listadoLibrosBD, name='bodeguero'),  # Asegúrate de que el nombre de la vista sea correcto
    path('agregar_carrito/<int:libro_id>/', views.agregar_carrito, name='agregar_carrito'),
    path('quitar_libro/<int:libro_id>/', views.quitar_libro, name='quitar_libro'),
    path('realizar_pedido/', views.realizar_pedido, name='realizar_pedido'),

    #SOPORTE
    path('crear_ticket_jefe/', crear_ticket_Jefe, name='crear_ticket_jefe'),
    path('crear_ticket_bode/', crear_ticket_Bodeguero, name='crear_ticket_bodeguero'),
    path('tickets/', views.soporte_tickets, name='soporte_tickets'),
    path('tickets/<int:ticket_id>/', detalle_ticket, name='detalle_ticket'),
    path('tickets_Estado/', ver_tickets, name='ver_tickets'),

]
    

