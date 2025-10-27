import React, { useState } from "react";
import "./styles/login.css";
import { login } from "../services/authService";
import { useNavigate } from "react-router-dom";


function parseJWT(token) {
    try {
        return JSON.parse(atob(token.split(".")[1]));
    } catch (e) {
        return null;
    }
}

function Login() {
    const navigate = useNavigate();
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();
        try{
            const data = await login(email, password);
            localStorage.setItem("token", data.access_token);
            const user = parseJWT(data.access_token);
            const payload = parseJWT(data.access_token);
            console.log(payload);
            if (payload && payload.rol === 'admin') {
                navigate('/admin');
            } else {
                alert('No tienes permisos de administrador');
            }
        } catch(err){
            alert(err.message);
        }
    };

    return (
        <div className="login-page">
            <form className="login-form" onSubmit={handleSubmit}>
                <h1 className="login-title">Iniciar sesión</h1>
                <div className="form-group">
                    <label htmlFor="email">Email</label>
                    <input
                        type="email"
                        className="form-control"
                        id="email"
                        placeholder="Email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="password">Password</label>
                    <input
                        type="password"
                        className="form-control"
                        id="password"
                        placeholder="Password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                    />
                </div>
                <button type="submit" className="btn btn-primary">
                    Iniciar sesión
                </button>
            </form>
        </div>
    );
}

export default Login;