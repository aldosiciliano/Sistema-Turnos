import React, { useState } from 'react';

function TurnoForm() {
    const [paciente, setPaciente] = useState('');
    const [profesional, setProfesional] = useState('');
    const [fechaHora, setFechaHora] = useState('');
    const [estado, setEstado] = useState('Pendiente');
    const [observaciones, setObservaciones] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        // Aquí va la lógica para enviar los datos al backend
        console.log({ paciente, profesional, fechaHora, estado, observaciones });
    };

    return (
        <form onSubmit={handleSubmit}>
            <div className="form-group mb-3">
                <label htmlFor="paciente">Paciente (nombre del paciente)</label>
                <input
                    type="text"
                    className="form-control"
                    id="paciente"
                    placeholder="Ingrese paciente"
                    value={paciente}
                    onChange={e => setPaciente(e.target.value)}
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
