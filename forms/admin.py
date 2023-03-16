from django.contrib import admin
from forms.models import Form, Questions, Answer, Choices, Responses

# Register your models here.

admin.site.register(Form)
admin.site.register(Questions)
admin.site.register(Answer)
admin.site.register(Choices)
admin.site.register(Responses)