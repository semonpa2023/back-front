export function RegistroProveedor(){
    return(

        <>

            <form className="border rounded p-5">

                <div className="mb-3">
                    <input type="text" className="form-control" placeholder="Nombres"/>
                </div>

                <div className="mb-3">
                    <input type="text" className="form-control" placeholder="Documento"/>
                </div>

                <div className="mb-3">
                    <input type="text" className="form-control" placeholder="direccion"/>
                </div>

                <div className="mb-3">
                    <input type="text" className="form-control" placeholder="Ciudad"/>
                </div>

                <div className="mb-3">
                    <input type="text" className="form-control" placeholder="Representante"/>
                </div>

                <div className="mb-3">
                    <input type="text" className="form-control" placeholder="Telefono Contacto"/>
                </div>

                <div className="mb-3">
                    <input type="email" className="form-control" placeholder="correo"/>
                </div>

                <div className="mb-3">
                    <input type="date" className="form-control" placeholder="Fecha Envio"/>
                </div>

                <div className="mb-3">
                    <input type="number" className="form-control" placeholder="Costo Envio"/>
                </div>

                <div className="mb-3">
                    <textarea type="text" className="form-control" placeholder="Descripcion"/>
                </div>

                <button className="btn btn-primary w-100">Enviar</button>

               

            </form>
        
        
        </>

    )
}