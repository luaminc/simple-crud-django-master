from django.conf.urls import url, include
from apps.proveedores import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'proveedores'

proveedores_patterns = [
    url(r'^inicio/$', views.proveedor_list, name='home'),
    url(r'^(?P<pk>[0-9]+)/$', views.proveedor_detail, name='proveedores-detail'),
    url(r'^crear/$', views.proveedor_create, name='proveedores-create'),
    url(r'^(?P<pk>[0-9]+)/editar/$', views.proveedor_update, name='proveedores-edit'),
    url(r'^(?P<pk>[0-9]+)/eliminar/$', views.proveedor_delete, name='proveedores-delete')
]

urlpatterns = [
    url(r'^$', views.log_in, name='log-in'),
    url(r'^log-out/$', views.log_out, name='log-out'),
    url(r'^categorias/$', views.category_list, name='category-list'),
    url(r'^proveedores/', include(proveedores_patterns))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)