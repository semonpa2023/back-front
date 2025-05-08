import "./Logistica.css"

import { useState, useEffect } from "react"
import { consultarLogistica } from "../../service/servicioLogistico"

export function Logistica(){

    // creo dos variables de estado para consumir el api

    const [datosLogistica, setdDatosLogistica] = useState([])
    const [carga, setCarga] = useState(false)

    useEffect(()=>{
        consultarLogistica().then((respuesta)=>{
                    console.log(respuesta)
                    setCarga(true)
                    setdDatosLogistica(respuesta)
                    })
    }, [])

    if(carga){return(

        <>

                <section className="fondo">

                </section>

            <section className="container-my-5 text-center"> 
                <section className="row p-5">
                    <div className="col-12 col-md-6">
                        <h3>Logistica web</h3>
                        <img src="../../../src/assets/4394250.png" alt="foto" className="img-fluid" />
                    </div>
                    <div className="col-12 col-md-6 align-self-center shadow p-5">
                        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Pariatur commodi deleniti accusantium quas non vel veritatis tempore quia exercitationem architecto explicabo debitis ipsa quo consequatur earum id, ipsum cum perferendis possimus laboriosam. Veniam quo, cumque sint enim, asperiores a nobis magnam rem iste impedit fugiat quae praesentium, consequatur quisquam fugit.</p>
                    </div>
                </section>
            </section>
        
            <form className="border rounded p-5">

                <div className="mb-3">
                    <input type="text" className="form-control" placeholder="Cc. Logistica"/>
                </div>

                <div className="mb-3">
                    <input type="email" className="form-control" placeholder="Correo"/>
                </div>

                <div className="mb-3">
                    <input type="text" className="form-control" placeholder="Telefono"/>
                </div>

                <div className="mb-3">
                    <input type="text" className="form-control" placeholder="receptor"/>
                </div>

                <div className="mb-3">
                    <input type="text" className="form-control" placeholder="detalles"/>
                </div>

                <button className="btn btn-primary w-100">Enviar</button>

               

            </form>

            <section className="container">
                    <section className="row row-cols-1 row-cols-md-3">
                        {
                            datosLogistica.map((logistica)=>{
                                return(
                                    <div className="col">
                                        <div className="card h-100 shadow p-3">
                                            <h3> {logistica.nombreEncargado}</h3>
                                            <h4>{logistica.correoEncargado}</h4>
                                            <hr />
                                            <h4>{logistica.contactoEncargado}</h4>
                                        </div>
                                    </div>
                                )
                            })
                        }

                    </section>

                </section>
        
        </>
    )}

    
}