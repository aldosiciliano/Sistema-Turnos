export async function login(email, password) {
    const formData = new URLSearchParams();
    formData.append('username', email);
    formData.append('password', password);

   const response = await fetch('http://localhost:8000/auth/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: formData
    });

    if (!response.ok) throw new Error('Login incorrecto');
    return await response.json();
}