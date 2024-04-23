
from transformData import TransformData

pathJson = "./data/json/promediosSipsaCiudad.json"
pathEnd = "./transformedData/json/transformedData.json"
TransformData().controller(pathJson, pathEnd)
