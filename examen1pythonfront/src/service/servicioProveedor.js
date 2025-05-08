export async function consultarProveedores() {
 //1 construir el endpoint

 const URL = "http://localhost:8000/consultarProveedores";
 //2. activar la peticion

 let peticion={
   method: 'GET',
 }
 //3. activo el consumo de la peticion

 let respuesta = await fetch(URL, peticion);
 let proveedoresConsultados = await respuesta.json();

 console.log (proveedoresConsultados);

 return proveedoresConsultados;

}
