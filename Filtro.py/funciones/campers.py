import funciones.corefile as cf


cf.MY_DATABASE='data/campus.json'
isEmpty = True


def verificarDato(valorDato, enunciadoDato, data) -> str:
    global isEmpty
    isEmpty = True
    valorDato = ""

    while (isEmpty):
        valorDato = input(f"{enunciadoDato}")
        if (valorDato != ""):
            if (enunciadoDato == "Ingrese ID del Camper : "):
                dataId = data.get(valorDato, -1)
                if (type(dataId) == dict):
                    print(f"El ID ya se encuentra registrado")
                else:
                    isEmpty = False
                if (type(dataId) == dict):
                    print(f"El ID ya se encuentra registrado")
                else:
                    isEmpty = False
            else:
                isEmpty = False
        else:
            print(f"El dato no puede estar vacio")

    return valorDato
    
def regCamper(Movistar : dict):
    header = """
    *************************************
    *       REGISTRO DE USUARIO         *
    *************************************
    """
    print(header)
    data = Movistar.get("Movistar").get("Usuario")
    valor = ""

    print(f"")
    print(f"DATOS DEL  USUARIO")
    print(f"")
    id = verificarDato(valor, "Ingrese ID del usuario : ", data)
    nombre = verificarDato(valor, "Ingrese nombre del usuario : ", data)
    apellido = verificarDato(valor, "Ingrese apellidos del usuario  : ", data)
    direccion = verificarDato(valor, "Ingrese direccion del usuario  : ", data)
    nroTelCel = verificarDato(valor, "Ingrese teléfono celular del usuario  : ", data)
    nroTelFijo = verificarDato(valor, "Ingrese teléfono fijo del usuario : ", data)
    ubicacionTelFijo = verificarDato(valor, "Ingrese si el teléfono pertenece a Casa o Trabajo : ", data)
    categoria = verificarDato(valor, "Ingrese la categoria del cliente /regular/leales/nuevos :", data )
    
    usuario = {
        "NroId" : id,
        "Nombre" : nombre,
        "Apellido" : apellido,
        "Direccion" : direccion,
        "Acudiente" : {},
        "Telecontacto" : {},
        "categoria" : categoria
    }

    

    phoneCel = {
        "id" : str((len(usuario["Telecontacto"]) + 1)),
        "nrotel" : nroTelCel,
        "ubicacion" : ""
    }

    phoneFijo = {
        "id" : str((len(usuario["Telecontacto"]) + 1)),
        "nrotel" : nroTelFijo,
        "ubicacion" : ubicacionTelFijo
    }

   
    usuario["Telecontacto"].update({str((len(usuario["Telecontacto"]) + 1)).zfill(3) : phoneCel})
    usuario["Telecontacto"].update({str((len(usuario["Telecontacto"]) + 1)).zfill(3) : phoneFijo})
    data.update({usuario["NroId"] : usuario})
    Movistar.get("Movistar").get("usuario").update(data)
    cf.UpdateFile(usuario)


def buscarCamper(idusuario : str, Movistar : dict) -> dict:
    data = Movistar.get("Movistar").get("usuario").get(idusuario, -1)
    if (type(data) != dict):
        print(f"No se encontró un Camper con este código")
        return {}
    else:
        return data