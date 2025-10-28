export async function findPatientByDni(dni) {
    const res = await fetch('http://localhost:8000/pacientes/');
    if (!res.ok) throw new Error('No se pudo obtener la lista de pacientes');
    const pacientes = await res.json();
    return pacientes.find(p => p.dni === dni) || null;
}

export async function createPatient({ nombre, apellido, dni, telefono, fecha_nacimiento }) {
    const res = await fetch('http://localhost:8000/pacientes/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ nombre, apellido, dni, telefono, fecha_nacimiento })
    });
    if (!res.ok) throw new Error('Error creando paciente');
    return await res.json();
}
