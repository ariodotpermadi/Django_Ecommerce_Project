from django.contrib import admin
from .models import category, customer, product, order

# Untuk menampilkan data models di admin web

admin.site.register(category)
admin.site.register(customer)
admin.site.register(product)
admin.site.register(order)
