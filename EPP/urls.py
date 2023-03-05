from django.urls import path
from .views import *


urlpatterns = [
    path("productos", index_admin, name="home"),
    path("agregar_producto", agregar_productos, name="addProduct"),
    path("actualizar_producto", actualizar_producto, name="updateProduct"),
    path("eliminar_producto", eliminar_producto, name="deleteProduct")
]