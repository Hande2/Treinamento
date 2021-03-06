from django.db import models

class Documento(models.Model):
    num_doc = models.CharField(max_length=50)

    def __str__(self):
        return self.num_doc


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)
    doc = models.OneToOneField(Documento, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        permissions = (
            ('deletar_clientes', 'Deletar_clientes'),
        )

    def __str__(self):
        return self.first_name + ' ' + self.last_name




#    def get_total(self):
 #       tot=0
  #      for produto in self.produtos.all():
   #         tot += produto.preco
    #    return (tot - self.desconto) - self.impostos
#
 #   def __str__(self):
  #      return self.numero


#@receiver(m2m_changed, sender=Venda.produtos.through)
#def update_vendas_total(sender, instance, **kwargs):
 #   total = instance.get_total()
  #  instance.save()

    #Venda.objects.filter(id=instance.id).update(total=total)
