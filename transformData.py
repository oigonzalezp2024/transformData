
import json

class TransformData:

    def controller(self, pathJson:str, pathEnd:str)->None:
        inputData = self.readFileJson(pathJson)
        outputData = self.businessLogic(inputData)
        content = json.dumps(outputData, sort_keys=True, indent=4)
        self.createFileJson(pathEnd, content)

    def readFileJson(self, pathJson:str)->object:
        f = open(pathJson,"r")
        content = f.read()
        f.close()
        response = json.loads(content)
        return response

    def createFileJson(self, pathJson:str, content:str)->None:
        f = open(pathJson,"w")
        f.write(content)
        f.close()

    def businessLogic(self, data:object)->list:
        casos = []
        ciudades = []
        objs = {}
        for i in data:
            obj = {}
            ciudad = self.transMunicipio(str(i['ciudad']))
            producto = self.transProducto(str(i['producto']))
            fechaCaptura = self.transFechaMesIni(str(i['fechaCaptura']))
            precio = int(i['precioPromedio'])
            caso = str(ciudad+producto.capitalize())

            if(ciudad not in ciudades):
                rr = 2
                for i in ciudades:
                    if(i in ciudad):
                        rr = 1
                        break
                    if(ciudad in i):
                        rr = 1
                        ciudad = i
                        caso = str(ciudad+producto.capitalize())
                        break
                if(rr==2):
                    ciudades.append(ciudad)

            if(caso not in casos):
                casos.append(caso)
                casos = set(casos)
                casos = list(casos)
                obj["city"] = ciudad
                obj["product"] = producto
                obj["date"] = fechaCaptura
                obj["suptitle"] = str("Webservice SIPSA DANE")
                obj["title"] = str("Mercado de "+producto+" en "+ciudad)
                obj["xlabel"] = "dias del mes de abril"
                obj["ylabel"] = "precios"
                obj["x"] = [fechaCaptura]
                obj["y"] = [precio]
                objs[caso] = obj
            else:
                xs = list(objs[caso]["x"])
                xs.append(fechaCaptura)
                ys = list(objs[caso]["y"])
                ys.append(precio)
                objs[caso]["x"] = xs 
                objs[caso]["y"] = ys
                objs[caso]["date"] = self.transFechaMesIni(str(i['fechaCaptura']))

        dataT = []
        for key in objs:
            dataT.append(objs[key])
            
        return dataT

    def transMunicipio(self, data:str)->str:
        datar = str(data).split(",")
        txt = str(datar[0]).lower()
        txt = txt.replace("á", "a")
        txt = txt.replace("é", "e")
        txt = txt.replace("í", "i")
        txt = txt.replace("ó", "o")
        txt = txt.replace("ú", "u")
        txt = txt.replace("(", "_")
        txt = txt.replace("ñ", "n")
        txt = txt.replace(")", "")
        txt = txt.replace(" ", "")
        return txt
    
    def transProducto(self, data:str)->str:
        datar = str(data).split(",")
        txt = str(datar[0]).lower()
        txt = txt.replace("á", "a")
        txt = txt.replace("é", "e")
        txt = txt.replace("í", "i")
        txt = txt.replace("ó", "o")
        txt = txt.replace("ú", "u")
        txt = txt.replace("(", "_")
        txt = txt.replace("ñ", "n")
        txt = txt.replace(")", "")
        txt = txt.replace(" ", "_")
        txt = txt.replace("/", "")
        txt = txt.replace("*", "")
        return txt
    
    def transFechaMesIni(self, data:str)->str:
        datar = str(data)
        return datar[0:10]  
