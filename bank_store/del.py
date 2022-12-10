from models import Bank

queryset = Bank.objects.create(id=63,name = 'BOI')  
queryset.save()