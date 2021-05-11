# Operacion-Fuego-de-Quasar

En este repositorio se encuentra el codigo, de las lambdas que se ejecutan al realizar una 
peticion al API Gateway configurado en AWS.

Endpoints:
- https://x0ndgoaat7.execute-api.us-east-1.amazonaws.com/ML/topsecret
- https://x0ndgoaat7.execute-api.us-east-1.amazonaws.com/ML/topsecret_split/

En el primer endpoint se puede, se realiza una peticion de tipo POST, junto con el siguiente cuerpo:
```json
{
    "satellites": [
        {
            "name": "kenoby",
            "distance": 100,
            "message": [
                "este",
                "",
                "",
                "mensaje",
                ""
            ]
        },
        {
            "name": "skywalker",
            "distance": 115.5,
            "message": [
                "",
                "es",
                "",
                "",
                "secreto"
            ]
        },
        {
            "name": "sato",
            "distance": 142.7,
            "message": [
                "este",
                "",
                "un",
                "",
                ""
            ]
        }
    ]
}
```


En el segundo endpoint se pueden realizar dos tipos de peticiones, GET y POST. El POST guarda los datos enviados al endpoint, con el nombre que se envia en el parametro final de 
la ruta.

https://x0ndgoaat7.execute-api.us-east-1.amazonaws.com/ML/topsecret_split/kenoby

El objeto que se debe enviar debe cumplir las siguientes caracteristicas.
```json
{
            "name": "kenoby",
            "distance": 100,
            "message": [
                "este",
                "",
                "",
                "mensaje",
                ""
            ]
        }
```

El GET valida los datos almacenados y genera una respuesta igual al primer endpoint.

https://x0ndgoaat7.execute-api.us-east-1.amazonaws.com/ML/topsecret_split/

El objetitivo del primer endpoint y el GET del segundo, es retornar un objeto similar al siguiente:
```json
{
    "location": {
        "x": -487.2859125,
        "y": 1557.014225
    },
    "message": "este es un mensaje secreto"
}
```