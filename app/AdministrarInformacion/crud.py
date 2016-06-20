from crudbuilder.abstract import BaseCrudBuilder
from app.morbilidadSV.models import Morbilidad

class PersonCrud(BaseCrudBuilder):
    model = Morbilidad
    search_feilds = ['nombre']
    tables2_fields = ('nombre', 'nom_departamento')
    tables2_css_class = "table table-bordered table-condensed"
    tables2_pagination = 10  # default is 10
    modelform_excludes = ['created_by', 'updated_by']
    

    @classmethod
    def custom_queryset(cls, request, **kwargs):
        """Define your own custom queryset for list view"""
        qset = cls.model.objects.all()
        return qset