import React, { useState, useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";
import { Button, AppBar, Toolbar, Typography, Card, CardContent, Grid, Container } from "@mui/material";
import { getCSRFToken } from "@/utils/csrf";

function HomePage() {
    const navigate = useNavigate(); // Utilisé pour la redirection après la déconnexion
    const [isLoggedIn, setIsLoggedIn] = useState(false); // État de connexion
    const [username, setUsername] = useState(""); // Nom d'utilisateur connecté

    // Vérifie l'état de connexion lors du montage
    useEffect(() => {
        async function checkAuthStatus() {
            try {
                const response = await fetch("/api/login/check-auth/", {
                    method: "GET",
                    headers: { "Content-Type": "application/json" },
                });
                const data = await response.json();
                setIsLoggedIn(data.authenticated); // Mets à jour si connecté
                if (data.authenticated) {
                    setUsername(data.username); // Mets à jour le nom d'utilisateur
                }
            } catch (error) {
                console.error("Erreur lors de la vérification de l'authentification :", error);
            }
        }
        checkAuthStatus();
    }, []);

    // Gère la déconnexion
    const handleLogout = async () => {
        const csrfToken = await getCSRFToken();

        if (!csrfToken) {
            console.error("CSRF Token non trouvé !");
            return;
        }

        try {
            const response = await fetch("/logout/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken, // Ajout du CSRF Token
                },
            });

            if (response.ok) {
                console.log("Déconnexion réussie");
                setIsLoggedIn(false); // Mets à jour l'état
                setUsername(""); // Réinitialise le nom d'utilisateur
                navigate("/login-account"); // Redirige vers la page de connexion
            } else {
                console.error("Erreur lors de la déconnexion :", response.status);
            }
        } catch (error) {
            console.error("Erreur réseau :", error);
        }
    };

    const tournaments = [
        { id: 1, name: "FIFA", date: "14 janvier 2025", prize: "1000€" },
        { id: 2, name: "CoD", date: "15 janvier 2025", prize: "1500€" },
        { id: 3, name: "LoL", date: "16 janvier 2025", prize: "2000€" },
    ];

    return (
        <div
            className="homepage-container"
            style={{
                backgroundColor: "#000",
                color: "#fff",
                minHeight: "100vh",
                display: "flex",
                flexDirection: "column",
                justifyContent: "space-between",
            }}
        >
            <AppBar position="static" style={{ marginBottom: "20px", backgroundColor: "#1a1a1a" }}>
                <Toolbar style={{ justifyContent: "space-between" }}>
                    <Typography variant="h5" style={{ fontWeight: "bold", fontFamily: "Arial Black, Gadget, sans-serif", color: "#fff" }}>
                        Tournois de Jeux Vidéo
                    </Typography>
                    <div>
                        {!isLoggedIn && (
                            <>
                                <Link to="/login-account" style={{ textDecoration: "none", marginRight: "10px" }}>
                                    <Button variant="contained" style={{ backgroundColor: "#ff0000", color: "#fff" }}>Se connecter</Button>
                                </Link>
                                <Link to="/sign-up-account" style={{ textDecoration: "none" }}>
                                    <Button variant="contained" style={{ backgroundColor: "#ff0000", color: "#fff" }}>Créer un compte</Button>
                                </Link>
                            </>
                        )}
                        {isLoggedIn && (
                            <>
                                <Typography style={{ display: "inline", marginRight: "10px", color: "#ffcc00" }}>
                                    Bonjour, {username}
                                </Typography>
                               <a href="/home/" style={{ textDecoration: 'none', marginRight: '10px' }}>
                                    <Button variant="outlined" style={{ color: "#fff", borderColor: "#ff0000" }}>Profile</Button>
                                </a>
                                <Button variant="text" style={{ color: "#fff" }} onClick={handleLogout}>Se déconnecter</Button>
                            </>
                        )}
                    </div>
                </Toolbar>
            </AppBar>

            <div className="hero-section" style={{ textAlign: "center", marginBottom: "40px", flexGrow: 1 }}>
                <Typography
                    variant="h2"
                    style={{
                        fontWeight: "bold",
                        fontFamily: "Arial Black, Gadget, sans-serif",
                        color: "#ffcc00",
                        marginBottom: "20px",
                    }}
                >
                    Bienvenue aux tournois de jeux vidéo
                </Typography>
                <Typography variant="h5" style={{ color: "#ffffffb3", marginBottom: "30px" }}>
                    Rejoignez des compétitions épiques et montrez vos talents !
                </Typography>
                <Link to="/create-event" style={{ textDecoration: "none", marginRight: "10px" }}>
                    <Button variant="contained" style={{ backgroundColor: "#ff0000", color: "#fff" }} size="large">
                        Créer un évenement
                    </Button>
                </Link>
                <Link to="/join-event" style={{ textDecoration: "none" }}>
                    <Button variant="contained" style={{ backgroundColor: "#ff0000", color: "#fff" }} size="large">
                        Rejoindre un évenement
                    </Button>
                </Link>
            </div>

            <Container style={{ flexGrow: 1 }}>
                <Typography variant="h3" style={{ fontWeight: "bold", fontFamily: "Arial Black, Gadget, sans-serif", color: "#ffcc00", textAlign: "center", marginBottom: "30px" }}>
                    Tournois disponibles
                </Typography>
                <Grid container spacing={3}>
                    {tournaments.map((tournament) => (
                        <Grid item xs={12} md={4} key={tournament.id}>
                            <Card style={{ backgroundColor: "#1a1a1a", color: "#fff" }}>
                                <CardContent>
                                    <Typography
                                        variant="h5"
                                        component="div"
                                        style={{ fontWeight: "bold", fontFamily: "Arial Black, Gadget, sans-serif", color: "#ffcc00" }}
                                    >
                                        {tournament.name}
                                    </Typography>
                                    <Typography color="text.secondary" gutterBottom style={{ color: "#ffffffb3" }}>
                                        Date : {tournament.date}
                                    </Typography>
                                    <Typography variant="body2" style={{ color: "#fff" }}>
                                        Récompense : {tournament.prize}
                                    </Typography>
                                    <Link to="/ticket-office" state={tournament}>
                                        <Button variant="contained" style={{ backgroundColor: "#ff0000", color: "#fff" }}>
                                            Réserver
                                        </Button>
                                    </Link>
                                </CardContent>
                            </Card>
                        </Grid>
                    ))}
                </Grid>
            </Container>

            <footer
                className="footer"
                style={{
                    marginTop: "40px",
                    padding: "20px 0",
                    backgroundColor: "#1a1a1a",
                    textAlign: "center",
                }}
            >
                <Typography variant="body2" style={{ color: "#ffffffb3" }}>
                    © 2025 Tournois de Jeux Vidéo. Tous droits réservés.
                </Typography>
                <nav className="footer-nav">
                    <Link to="#" style={{ textDecoration: "none", color: "#ffcc00", margin: "0 10px" }}>
                        Contact
                    </Link>
                    <Link to="#" style={{ textDecoration: "none", color: "#ffcc00", margin: "0 10px" }}>
                        Conditions d'utilisation
                    </Link>
                    <Link to="#" style={{ textDecoration: "none", color: "#ffcc00", margin: "0 10px" }}>
                        Politique de confidentialité
                    </Link>
                </nav>
            </footer>
        </div>
    );
}

export default HomePage;
