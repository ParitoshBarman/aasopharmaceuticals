# from django.db import models

# # Create your models here.
# class AllProducts(models.Model):
#     slID = models.AutoField(primary_key=True)
#     productsname = models.CharField(max_length=50)
#     price = models.ImageField()
#     discountInPersentage = models.ImageField()
#     Qty = models.ImageField()
#     Pack = models.CharField(max_length=50)
#     Batch = models.CharField(max_length=50)
#     Exp = models.CharField(max_length=50)
#     HSN = models.ImageField()
#     MRP = models.ImageField()
#     Rate = models.ImageField()
#     SGST = models.ImageField()
#     CGST = models.ImageField()
#     Amount = models.ImageField()
    
#     def __str__(self):
#         return self.fullname