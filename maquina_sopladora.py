class MaquinaSopladoraBotellas:
    def __init__(self, temperatura_ideal, presion_ideal, tiempo_base_soplado):
        self.temperatura_ideal = temperatura_ideal  
        self.presion_ideal = presion_ideal         
        self.tiempo_base_soplado = tiempo_base_soplado  
        self.temperatura_actual = 30
        self.presion_actual = 5      
        
    def get_temperatura_ideal(self):
        return self._temperatura_ideal
    def set_temperatura_ideal(self, valor):
        if valor < 0:
            raise ValueError("La temperatura no puede ser menor a 0°C")
        self._temperatura_ideal = valor
        
    def get_presion_ideal(self):
        return self._temperatura_actual
    def set_presion_ideal(self, valor):
        if valor < 0:
            raise ValueError("la presion no puede ser menor a 0°C")
        self._presion_ideal = valor

    def get_temperatura_actual(self):
        return self._temperatura_actual
    def set_temperatura_actual(self, valor):
        if valor < 0:
            raise ValueError("La temperatura no puede ser menor a 0°C")
        self._temperatura_actual = valor
    def get_presion_actual(self):
        return self._presion_actual
    def set_presion_actual(self, valor):
        if valor < 0:
            print("La presión no puede ser negativa.")
        else:
            self._presion_actual = valor
    def get_tiempo_base_soplado(self):
        return self._tiempo_base_soplado
    def set_tiempo_base_soplado(self, valor):
        if valor < 3:
            print("el tiempo de soplado no puede ser menor a 3seg.")
        else:
            self._tiempo_base_soplado = valor

    def ajustar_temperatura(self):
        if self.temperatura_actual < self.temperatura_ideal:
            aumento_temp = min(self.temperatura_ideal - self.temperatura_actual, 5)
            self.temperatura_actual += aumento_temp
            print(f"Incrementando la temperatura a {self.temperatura_actual}°C")
        elif self.temperatura_actual > self.temperatura_ideal:
            disminucion_temp = min(self.temperatura_actual - self.temperatura_ideal, 5)
            self.temperatura_actual -= disminucion_temp
            print(f"Disminuyendo la temperatura a {self.temperatura_actual}°C")
        else:
            print("La temperatura es ideal.")
    
    def ajustar_presion(self):
        if self.presion_actual < self.presion_ideal:
            aumento_temperatura = min(self.presion_ideal - self.presion_actual, 1)
            self.presion_actual += aumento_temperatura
            print(f"Incrementando la presión a {self.presion_actual} bar")
        elif self.presion_actual > self.presion_ideal:
            disminucion_temp = min(self.presion_actual - self.presion_ideal, 1)
            self.presion_actual -= disminucion_temp
            print(f"Disminuyendo la presión a {self.presion_actual} bar")
        else:
            print("La presión es ideal.")
    
    def calcular_tiempo_soplado(self, tamaño_botella): 
        tiempo_soplado = self.tiempo_base_soplado * (tamaño_botella / 1000)  
        print(f"El tiempo de soplado para una botella de {tamaño_botella} ml es {tiempo_soplado:.2f} segundos.")
        return tiempo_soplado

    def __str__(self):
        return (f"Maquina Sopladora: \n"
                f"Temperatura actual: {self.temperatura_actual}°C (Ideal: {self.temperatura_ideal}°C)\n"
                f"Presión actual: {self.presion_actual} bar (Ideal: {self.presion_ideal} bar)\n")


maquina = MaquinaSopladoraBotellas(temperatura_ideal=120, presion_ideal=30, tiempo_base_soplado=5)


print(maquina)  
maquina.ajustar_temperatura()  
maquina.ajustar_presion()      
maquina.calcular_tiempo_soplado(1500)  

print(maquina)
        
          