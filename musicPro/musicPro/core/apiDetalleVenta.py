from pprint import pprint
import requests
import json


def getAllDetVentas():
    try:
        key="DetallesVentas"
        url="https://springbootventas.herokuapp.com/" + key
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            data = respuesta.json()
            pprint(data)
            print(print("se logró"+ str(respuesta)))
        else:
            print(print("NO se logró" + str(respuesta)))
        return data
    except Exception as e:
        print(e)

#getAllDetVentas()

def getDetVenta(id):

    try:
        url="https://springbootventas.herokuapp.com/DetalleVenta/"+ str(id)
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            print(print("se logró"+ str(respuesta)))
            data = respuesta.json()
            print(str(respuesta))
            print(data)
            return data
        else:
            print(print("NO se logró, id no encontrada"+ str(respuesta)))
        
    except Exception as e:
        print(e)

#getDetVenta(1)

def getVentaByDetalle(detalle):
    try:
        key="DetallesVenta"
        url="https://springbootventas.herokuapp.com/" + key
        data=False
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            print(print("se logró"+ str(respuesta)))
            data = respuesta.json()
            for i in data:
                if i["producto_det"] == detalle:
                    print("lo encontre")
                    data = i
                    print(data)
                    break
                else:
                    print("NO lo encontre")
                    data = False
                    pprint(data)
        else:
            print(print("NO se logró, id no encontrada"+ str(respuesta))) 
        return data
    except Exception as e:
        print(e)
        
#getVentaByDetalle("guitarra");

def loadDetVenta(producto_det,user_det,hora_det,fecha_det,tipopago_id_tpag,id_detVen):
    try:
        url="https://springbootventas.herokuapp.com/loadDetalleVenta"
        respuesta = False
    
        if len(id_detVen) <= 10:
            dato = {"producto_det": producto_det,"user_det": user_det,"hora_det": hora_det,"fecha_det": fecha_det,
            "tipopago_id_tpag": tipopago_id_tpag,"id_detVen": id_detVen}
            respuesta = requests.post(url, json = dato )
            if respuesta.status_code == 200:
                print(print("se logró"+ str(respuesta)))
            else:
                print(print("NO se logró, id no encontrada"+ str(respuesta)))
        else:
            print("el largo del rut excede el maximo")
    except Exception as e:
        print("No se logró")
        print(e)
        data = False
        pprint(data)
    return  respuesta
      
#loadDetVenta("Bateria","Vanesuki","16:38","02/01/2022","1","15")  

def updateDetVenta(id_detVen,producto_det,user_det,hora_det,fecha_det,tipopago_id_tpag):
    try:
        url="https://springbootventas.herokuapp.com/updateDetalleVenta"
        respuesta = False
    
        if len(id_detVen) <= 10:
            dato = {"id_detVen": id_detVen,"producto_det": producto_det,"user_det": user_det,"hora_det": hora_det,"fecha_det": fecha_det,
            "tipopago_id_tpag": tipopago_id_tpag}
            respuesta = requests.put(url, json = dato )
            if respuesta.status_code == 200:
                print(print("se logró"+ str(respuesta)))
            else:
                print(print("NO se logró, id no encontrada"+ str(respuesta)))
        else:
            print("el largo del rut excede el maximo")
    except Exception as e:
        print("No se logró, hubo un error")
        print(e)
        data = False
        pprint(data)
    return  respuesta  

#getAllDetVentas()
#updateDetVenta("4","Bateria","Vanesuki","11:38","02/01/2022","1")


#No funciona
def delVentaById(id):
    try:
        data = getDetVenta(id)
        respuesta = False
        url="https://springbootventas.herokuapp.com/delDetalleVenta" + str(id)
        if id >= 0:
            respuesta = requests.delete(url)
            if respuesta.status_code == 200:
                print("se logró"+ str(respuesta) + " eliminaste a : " + data["producto_det"])
                print("se logró")
            else:
                print(print("NO se logró, id no encontrada"+ str(respuesta)))
        else:
            print("id no encontrada = "+id)
        
        return respuesta
    except Exception as e:
        print("No se logró, hubo un error")
        print(e)
    

#delVentaById(4)
#getDetVenta(4)
#getAllDetVentas()