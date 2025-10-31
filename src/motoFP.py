import csv
from typing import NamedTuple
from datetime import datetime
Piloto=NamedTuple("Piloto", [("nombre", str),("escuderia", str)])

CarreraFP=NamedTuple("CarreraFP",[
        ("fecha_hora",datetime), 
        ("circuito",str),                    
        ("pais",str), 
        ("seco",bool), # True si el asfalto estuvo seco, False si estuvo mojado
        ("tiempo",float), 
        ("podio", list[Piloto])])


def lee_carreras(ruta_csv: str) -> list[CarreraFP]:
    with open(ruta_csv, encoding="utf-8",) as katana:
        lector=csv.reader(katana, delimiter ="," )
        res=[]
        next(lector)
        for fh,circu,pai,sec,tiem,pod in enumerate(lector):
            fh = datetime.strptime("%Y-%m-%d H:M")
            Circuito = str(circu)
            Pais = str(pai)
            Seco = sec == 1
            Tiempo= float(tiem)
            Podio=[]
            for piloto in pod.split(";"):
                nombre, escuderia = piloto.split("-")
                Podio.append(Piloto(nombre, escuderia))
            carrera = CarreraFP[fh, circu, pai, sec, tiem, pod] 
            res.append(carrera)   
    return res    
    
