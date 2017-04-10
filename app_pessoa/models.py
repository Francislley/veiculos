"""path
Aqui deve ficar tudo que for referente ao modelo de dados.
Tabelas do banco representadas na forma de classes.
Tabelas abstratas representadas na forma de classes.

Mais informações aqui https://docs.djangoproject.com/pt-br/1.10/topics/db/models/
"""
from django.db import models


class Tipoveiculo(models.Model):
    """
    Classe referente a tabela Tipo de Veículo
    """
    tipo = models.CharField('Tipo do Veículo', max_length=150)

    def __str__(self):
        return '{} - {}'. format(self.id, self.tipo)

class Marcaveiculo(models.Model):
    """
    Classe referente a tabela Marca do Veículo
    """
    marca = models.CharField('Marca do Veículo', max_length=30)

    def __str__(self):
        return '{} - {}'. format(self.id, self.marca)

class Veiculo(models.Model):
    """
    Classe referente a tabela Veículo
    """
    Id_tipo = models.ForeignKey (Tipoveiculo)
    Id_marca = models.ForeignKey (Marcaveiculo)
    modelo = models.CharField ('Modelo do Veículo', max_length=100)
    placa = models.CharField ('Placa do Veículo', max_length=10)
    cor = models.CharField('Cor do Veículo', max_length=15)

    def __str__(self):
        return '{} - {}'. format(self.id, self.Id_tipo, self.Id_marca, self.modelo, self.placa, self.cor)

#Teste de Save