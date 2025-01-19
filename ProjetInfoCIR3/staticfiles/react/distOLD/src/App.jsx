import './App.css'
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import HomePage from './HomePage.jsx'
import SignUpPage from './SignUpPage.jsx'
import LoginAccountPage from './LoginAccountPage.jsx'
import ProfilePage from './ProfilePage.jsx'
import CreateEventPage from './CreateEventPage.jsx'
import JoinEventPage from './JoinEventPage.jsx'
import ShowEventPage from './ShowEventPage.jsx'
import TicketOfficePage from "./TicketOfficePage.jsx";

function App() {
    return (
        <BrowserRouter>
            <div className="app-container">
                <Routes>
                    <Route path="/" element={<HomePage />} />
                    <Route path="/sign-up-account" element={<SignUpPage />} />
                    <Route path="/login-account" element={<LoginAccountPage />} />
                    <Route path="/profile" element={<ProfilePage />} />
                    <Route path="/create-event" element={<CreateEventPage />} />
                    <Route path="/join-event" element={<JoinEventPage />} />
                    <Route path="/show-event" element={<ShowEventPage />} />
                    <Route path="/ticket-office" element={<TicketOfficePage />} />
                </Routes>
            </div>
        </BrowserRouter>
    );
}

export default App