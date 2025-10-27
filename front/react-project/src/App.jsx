import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Login from './components/Login';
import AdminPanel from './components/AdminPanel';

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Login />} />
                <Route path="/login" element={<Login />} />
                <Route path="/admin" element={<AdminPanel />} />
            </Routes>
        </BrowserRouter>
    );
}

export default App;
