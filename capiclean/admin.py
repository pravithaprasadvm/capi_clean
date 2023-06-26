from django.contrib import admin
from .models import Register
from .models import Contact
from .models import Carrer
from .models import Apply

# Register your models here.
admin.site.register(Register)
admin.site.register(Contact)
admin.site.register(Carrer)
admin.site.register(Apply)
