import React from "react";
import { Link } from "react-router-dom";

function ProfilePage() {
    // Exemple de données utilisateur (à récup avec le backend)
    const userInfo = {
        name: "Nom",
        firstName: "Prénom",
        username: "NomUtilisateur",
        email: "utilisateur@example.com",
        creditCard: "CreditCard"
    };

    // Exemple de données d'événements (à récup dynamiquement)
    const userEvents = [
        { id: 1, name: "Tournoi FIFA 2025", date: "20 janvier 2025",code: "codeEvent1", qrCode: "monQrCode1" },
        { id: 2, name: "Championnat Call of Duty", date: "25 janvier 2025",code: "codeEvent2", qrCode: "monQrCode2" },
        { id: 3, name: "Compétition Fortnite", date: "30 janvier 2025",code: "codeEvent3", qrCode: "monQrCode3" },
    ];

    const containerStyle = {
        minHeight: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        backgroundColor: "#1a1a1a",
    };

    const boxStyle = {
        backgroundColor: "#000",
        color: "#fff",
        padding: "40px 30px",
        borderRadius: "10px",
        boxShadow: "0px 0px 20px rgba(255, 255, 255, 0.2)",
        maxWidth: "600px",
        width: "100%",
        textAlign: "center",
    };

    const titleStyle = {
        marginBottom: "20px",
        color: "#ffcc00",
        fontFamily: 'Arial Black, Gadget, sans-serif',
    };

    const sectionTitleStyle = {
        color: "#ffcc00",
        fontFamily: 'Arial Black, Gadget, sans-serif',
        textAlign: "left",
        marginBottom: "15px",
    };

    const textStyle = {
        marginBottom: "10px",
        textAlign: "left",
        fontFamily: 'Arial, sans-serif',
    };

    const tableStyle = {
        width: "100%",
        borderCollapse: "collapse",
        marginTop: "20px",
        textAlign: "left",
        color: "#fff",
    };

    const tableHeaderStyle = {
        borderBottom: "2px solid #ffcc00",
    };

    const tableRowStyle = {
        borderBottom: "1px solid #555",
    };

    const backButtonStyle = {
        backgroundColor: "#ff0000",
        color: "#fff",
        border: "none",
        padding: "10px 20px",
        borderRadius: "5px",
        marginTop: "20px",
        cursor: "pointer",
        fontFamily: 'Arial Black, Gadget, sans-serif',
    };

    const qrCodeStyle = {
        width: "80px",
        height: "80px",
    };

    return (
        <div style={containerStyle}>
            <div style={boxStyle}>
                <h1 style={titleStyle}>Profil de l'utilisateur</h1>

                {/* Section des informations de l'utilisateur */}
                <section>
                    <h2 style={sectionTitleStyle}>Informations personnelles</h2>
                    <p style={textStyle}><strong>Nom :</strong> {userInfo.name}</p>
                    <p style={textStyle}><strong>Prénom :</strong> {userInfo.firstName}</p>
                    <p style={textStyle}><strong>Nom d'utilisateur :</strong> {userInfo.username}</p>
                    <p style={textStyle}><strong>Email :</strong> {userInfo.email}</p>
                    <p style={textStyle}><strong>Carte bancaire :</strong> {userInfo.creditCard}</p>
                </section>

                {/* Section des événements de l'utilisateur */}
                <section>
                    <h2 style={sectionTitleStyle}>Événements payés</h2>
                    {userEvents.length > 0 ? (
                        <table style={tableStyle}>
                            <thead>
                            <tr style={tableHeaderStyle}>
                                <th>Nom</th>
                                <th>Date</th>
                                <th>Code-Event</th>
                                <th>QR Code</th>
                            </tr>
                            </thead>
                            <tbody>
                            {userEvents.map((event) => (
                                <tr key={event.id} style={tableRowStyle}>
                                    <td>{event.name}</td>
                                    <td>{event.date}</td>
                                    <td>{event.code}</td>
                                    <td>
                                        <img src={event.qrCode} alt={`QR Code for ${event.name}`} style={qrCodeStyle} />
                                    </td>
                                </tr>
                            ))}
                            </tbody>
                        </table>
                    ) : (
                        <p style={textStyle}>Aucun événement payé pour le moment.</p>
                    )}
                </section>

                {/* Bouton retour */}
                <Link to="/">
                    <button style={backButtonStyle}>Retour Menu</button>
                </Link>
            </div>
        </div>
    );
}

export default ProfilePage;