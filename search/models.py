# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class PageRank(models.Model):
    idurl = models.OneToOneField('Urls', models.DO_NOTHING, db_column='idurl', primary_key=True)
    nota = models.FloatField()

    class Meta:
        managed = False
        db_table = 'page_rank'


class PalavraLocalizacao(models.Model):
    idpalavra_localizacao = models.AutoField(primary_key=True)
    idurl = models.ForeignKey('Urls', models.DO_NOTHING, db_column='idurl')
    idpalavra = models.ForeignKey('Palavras', models.DO_NOTHING, db_column='idpalavra')
    localizacao = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'palavra_localizacao'


class Palavras(models.Model):
    idpalavra = models.AutoField(primary_key=True)
    palavra = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'palavras'


class UrlLigacao(models.Model):
    idurl_ligacao = models.AutoField(primary_key=True)
    idurl_origem = models.ForeignKey('Urls', models.DO_NOTHING, db_column='idurl_origem', related_name='topico_url_origem')
    idurl_destino = models.ForeignKey('Urls', models.DO_NOTHING, db_column='idurl_destino', related_name='topico_url_destino')

    class Meta:
        managed = False
        db_table = 'url_ligacao'


class UrlPalavra(models.Model):
    idurl_palavra = models.AutoField(primary_key=True)
    idpalavra = models.ForeignKey(Palavras, models.DO_NOTHING, db_column='idpalavra')
    idurl_ligacao = models.ForeignKey(UrlLigacao, models.DO_NOTHING, db_column='idurl_ligacao')

    class Meta:
        managed = False
        db_table = 'url_palavra'

class Urls(models.Model):
    idurl = models.AutoField(primary_key=True)
    url = models.CharField(max_length=2000, blank=True, null=True)
    descricao = models.CharField(max_length=200, blank=True, null=True)
    meta = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.url
        
    class Meta:
        managed = True
        db_table = 'urls'
