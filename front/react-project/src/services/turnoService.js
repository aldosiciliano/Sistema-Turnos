export async function createTurno({ id_paciente, profesional, fechaHora, estado, observaciones }) {
    const res = await fetch('http://localhost:8000/turnos/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            id_paciente,
            id_profesional: profesional,
            fecha_hora: fechaHora,
            estado,
            observaciones
        })
    });
    if (!res.ok) throw new Error('Error creando turno');
    return await res.json();
}
