"""
Neste arquivo fica o que você quer que o admin do Django gerencie para você
"""
from django.contrib import admin
from app_pessoa.models import Tipoveiculo, Marcaveiculo, Veiculo


class TipoAdmin(admin.ModelAdmin):
    """
    Classe responsável por definir como você quer gerenciar o modelo de dados da Tabela Pessoa
    """
    # list display = lista exibir, como deve ficar a visualização dos dados da tabela
    list_display = ('id','tipo')

# para que o django entenda que você quer que ele mostre uma classe no admin, basta registrar e referenciar
# as classes que você criou, primeiro o Modelo de dados, e depois a Classe para esse modelo.
admin.site.register(Tipoveiculo, TipoAdmin)

class MarcaAdmin(admin.ModelAdmin):
    list_display = ('id', 'marca')

admin.site.register(Marcaveiculo, MarcaAdmin)


class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('id', 'Id_tipo', 'Id_marca')

admin.site.register(Veiculo, VeiculoAdmin)
