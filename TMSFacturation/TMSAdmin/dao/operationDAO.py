
# operationID = models.AutoField(primary_key=True)
# dateO = models.DateField()
# timeO = models.TimeField()
# adresseO = models.CharField(max_length=30)
# destinationO = models.CharField(max_length=30)
# distanceO = models.IntegerField(null=True)
# clientO = models.ForeignKey(Client ,on_delete=models.CASCADE)
# total_costO = models.DecimalField(max_digits=5, decimal_places=2 ,default=0)
from ..models import Operation, OperationInput


def create_operation(client,adresse,destination,distance):
    operation = Operation()
    operation.clientO = client
    operation.adresseO = adresse
    operation.destinationO = destination
    operation.distanceO = distance
    operation.save()

# operation_inputID = models.AutoField(primary_key=True)
#     serviceOI = models.ForeignKey(Service,on_delete=models.CASCADE)
#     QteOI = models.IntegerField()
#     priceOI = models.DecimalField(max_digits=5, decimal_places=2,default=0)
#     total_priceOI = models.DecimalField(max_digits=5, decimal_places=2,default=0)
#     operationOI = models.ForeignKey(Operation,on_delete=models.CASCADE)

def create_operation_input(operation,service,qte):
    operation_input = OperationInput()
    operation_input.operationOI = operation
    operation_input.serviceOI = service
    operation_input.QteOI = qte
    operation_input.priceOI = service.priceS
    operation_input.total_priceOI = int(operation_input.QteOI) * int(operation_input.priceOI)
    operation_input.save()

    operation.total_costO = int(operation.total_costO) + int(operation_input.total_priceOI)
    operation.save()

def delete_operation_input(operationID, operation_inputID):
    operation = Operation.objects.get(operationID=operationID)
    operation_input = OperationInput.objects.get(operation_inputID=operation_inputID)

    operation.total_costO = int(operation.total_costO) - int(operation_input.total_priceOI)
    operation.save()
    operation_input.delete()





