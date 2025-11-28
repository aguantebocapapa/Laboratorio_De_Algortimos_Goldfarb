class Medicamento:
    def __init__ (self, nombre, categoria, stock, precio, codigo_de_barras):
        self.nombre=nombre
        self.categoria=categoria
        self.stock=stock
        self.precio=precio
        self.codigo_de_barras=codigo_de_barras
    def Vender(self, cantidad):
        if self.stock-cantidad<0:
            print("No se puede realizar la venta debido a que la cantidad de stock disponible es inferior a la requerida")
        else:
            self.stock=self.stock-cantidad
            print("Compra realizada con exito, el stock restante es:", self.stock)

    def Reponer_Stock(self, cantidad):
            self.stock=self.stock+cantidad
            print("Se repuso el stock con exito, el stock restante es:", self.stock)
            
    def Stock_Critico(self):
        print(self.stock<10)
ibuprofeno=Medicamento("Ibuprofeno 600mg","Ibuprofeno",150,100.99, 8756476559)
paracetamol=Medicamento("Paracetamol 500mg", "Paracetamol",50,200, 2132987690)
