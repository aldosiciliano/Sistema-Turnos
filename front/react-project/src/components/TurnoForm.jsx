import React, { useState } from 'react';
import './styles/TurnoForm.css';
import { createTurno } from '../services/turnoService';
import { createPatient, findPatientByDni } from '../services/pacienteService';

function TurnoForm() {
    const [nombre, setNombre] = useState('');
    const [apellido, setApellido] = useState('');
    const [dni, setDni] = useState('');
    const [telefono, setTelefono] = useState('');
    const [fechaNacimiento, setFechaNacimiento] = useState('');
    const [error, setError] = useState(null);
    const [fechaHora, setFechaHora] = useState('');
    const [estado, setEstado] = useState('');
    const [observaciones, setObservaciones] = useState('');
    const [profesional, setProfesional] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError(null);
        let id_paciente = null;
        try {
            let paciente = await findPatientByDni(dni);
            if (paciente) {
                id_paciente = paciente.id_paciente;
            } else {
                paciente = await createPatient({ 
                    nombre, 
                    apellido, 
                    dni, 
                    telefono, 
                    fecha_nacimiento: fechaNacimiento 
                });
                id_paciente = paciente.id_paciente;
            }
            // Crear el turno usando el servicio
            await createTurno({
                id_paciente,
                profesional,
                fechaHora,
                estado,
                observaciones
            });
            alert('Turno creado exitosamente');
            setNombre(''); 
            setApellido(''); 
            setDni('');
            setTelefono('');
            setFechaNacimiento('');
            setProfesional(''); 
            setFechaHora(''); 
            setEstado(''); 
            setObservaciones('');
        } catch (err) {
            setError(err.message || 'Error general');
        }
    };

    return (
        <form className="form-turno" onSubmit={handleSubmit}>
            <div className="form-group mb-3">
                <label htmlFor="nombre">Nombre</label>
                <input
                    type="text"
                    className="form-control"
                    id="nombre"
                    placeholder="Ingrese nombre"
                    value={nombre}
                    onChange={e => setNombre(e.target.value)}
                    required
                />
            </div>
            <div className="form-group mb-3">
                <label htmlFor="apellido">Apellido</label>
                <input
                    type="text"
                    className="form-control"
                    id="apellido"
                    placeholder="Ingrese apellido"
                    value={apellido}
                    onChange={e => setApellido(e.target.value)}
                    required
                />
            </div>
            <div className="form-group mb-3">
                <label htmlFor="dni">DNI</label>
                <input
                    type="text"
                    className="form-control"
                    id="dni"
                    placeholder="Ingrese DNI"
                    value={dni}
                    onChange={e => setDni(e.target.value)}
                    required
                />
            </div>
            <div className="form-group mb-3">
                <label htmlFor="telefono">Teléfono</label>
                <input
                    type="tel"
                    className="form-control"
                    id="telefono"
                    placeholder='Ingrese telefono'
                    value={telefono}
                    onChange={e => setTelefono(e.target.value)}
                    required
                />
            </div>
            <div className="form-group mb-3">
                <label htmlFor="fechaNacimiento">Fecha de Nacimiento</label>
                <input
                    type="date"
                    className="form-control"
                    id="fechaNacimiento"
                    placeholder='Ingrese fecha de nacimiento'
                    value={fechaNacimiento}
                    onChange={e => setFechaNacimiento(e.target.value)}
                    required
                />
            </div>
            <div className="form-group mb-3">
                <label htmlFor="profesional">Profesional</label>
                <select
                    className="form-control"
                    id="profesional"
                    value={profesional}
                    onChange={e => setProfesional(e.target.value)}
                    required
                >
                    <option value="">Seleccione un profesional</option>
                    <option value="1">Dr. Juan Pérez</option>
                    <option value="2">Dra. Ana Gómez</option>
                </select>
            </div>
            <div className="form-group mb-3">
                <label htmlFor="fechaHora">Fecha y Hora</label>
                <input
                    type="datetime-local"
                    className="form-control"
                    id="fechaHora"
                    value={fechaHora}
                    onChange={e => setFechaHora(e.target.value)}
                    required
                />
            </div>
            <div className="form-group mb-3">
                <label htmlFor="estado">Estado</label>
                <select
                    className="form-control"
                    id="estado"
                    value={estado}
                    onChange={e => setEstado(e.target.value)}
                >
                    <option value="Pendiente">Pendiente</option>
                    <option value="Confirmado">Confirmado</option>
                    <option value="Cancelado">Cancelado</option>
                    <option value="Atendido">Atendido</option>
                </select>
            </div>
            <div className="form-group mb-3">
                <label htmlFor="observaciones">Observaciones</label>
                <textarea
                    className="form-control"
                    id="observaciones"
                    rows="3"
                    value={observaciones}
                    onChange={e => setObservaciones(e.target.value)}
                />
            </div>
            <button type="submit" className="btn btn-primary">Crear Turno</button>
        </form>
    );
}

export default TurnoForm;
