class Cuenta:
    
    def __init__(self,saldo):
        self.__saldo=saldo
        
    def get_saldo(self):
        return self.__saldo
     
    def set_saldo(self,valor):
        if valor>=0:
            self.__saldo=valor
    
#crear mi objeto
mi_cuenta=Cuenta(100)   
mi_cuenta.set_saldo(500)
print(mi_cuenta.get_saldo())