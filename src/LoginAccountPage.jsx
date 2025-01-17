import React, { useState } from "react";
import { Button, Container, Typography, TextField, Box, Alert } from "@mui/material";
import { Link } from "react-router-dom";
import { getCSRFToken } from "@/utils/csrf";


function LoginAccountPage() {
    const [formData, setFormData] = useState({ username: "", password: "" });
    const [error, setError] = useState("");
    const [success, setSuccess] = useState(false);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

   const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setSuccess(false);

    const csrfToken = getCSRFToken(); // Récupérez le CSRF Token

    if (!csrfToken) {
        setError("CSRF Token non trouvé. Veuillez réessayer.");
        return;
    }

    try {
        const response = await fetch("/api/login/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrfToken, // Ajoutez le CSRF Token ici
            },
            body: JSON.stringify(formData),
        });

        if (!response.ok) {
            const errorText = await response.text();
            console.error("Erreur HTTP :", response.status, errorText);
            setError("Une erreur est survenue : " + errorText);
            return;
        }

        const data = await response.json();
        if (data.success) {
            setSuccess(true);
            console.log(data.message);
        } else {
            setError(data.message);
        }
    } catch (error) {
        console.error("Erreur lors de la requête :", error);
        setError("Une erreur s'est produite. Veuillez réessayer.");
    }
};


    return (
        <Container
            style={{
                minHeight: "100vh",
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                backgroundColor: "#1a1a1a",
            }}
        >
            <Box
                style={{
                    backgroundColor: "#000",
                    color: "#fff",
                    padding: "40px 30px",
                    borderRadius: "10px",
                    boxShadow: "0px 0px 20px rgba(255, 255, 255, 0.2)",
                    maxWidth: "400px",
                    width: "100%",
                    textAlign: "center",
                }}
            >
                <Typography
                    variant="h4"
                    style={{
                        marginBottom: "20px",
                        color: "#ffcc00",
                        fontFamily: "Arial Black, Gadget, sans-serif",
                    }}
                >
                    Connexion
                </Typography>

                <form onSubmit={handleSubmit}>
                    <TextField
                        label="Nom d'utilisateur"
                        name="username"
                        variant="outlined"
                        fullWidth
                        value={formData.username}
                        onChange={handleChange}
                        style={{ marginBottom: "20px", backgroundColor: "#1a1a1a" }}
                        InputLabelProps={{ style: { color: "#fff" } }}
                        inputProps={{
                            style: { color: "#fff", fontFamily: "Arial Black, Gadget, sans-serif" },
                        }}
                        required
                    />

                    <TextField
                        label="Mot de passe"
                        name="password"
                        type="password"
                        variant="outlined"
                        fullWidth
                        value={formData.password}
                        onChange={handleChange}
                        style={{ marginBottom: "20px", backgroundColor: "#1a1a1a" }}
                        InputLabelProps={{ style: { color: "#fff" } }}
                        inputProps={{
                            style: { color: "#fff", fontFamily: "Arial Black, Gadget, sans-serif" },
                        }}
                        required
                    />

                    {error && (
                        <Alert severity="error" style={{ marginBottom: "20px" }}>
                            {error}
                        </Alert>
                    )}
                    {success && (
                        <Alert severity="success" style={{ marginBottom: "20px" }}>
                            Connexion réussie !
                        </Alert>
                    )}

                    <Button
                        type="submit"
                        variant="contained"
                        fullWidth
                        style={{
                            backgroundColor: "#ff0000",
                            color: "#fff",
                            marginBottom: "20px",
                            fontWeight: "bold",
                            fontFamily: "Arial Black, Gadget, sans-serif",
                        }}
                    >
                        Se connecter
                    </Button>

                    <Link to="/sign-up-account" style={{ textDecoration: "none" }}>
                        <Button
                            variant="outlined"
                            fullWidth
                            style={{
                                color: "#fff",
                                borderColor: "#ffcc00",
                                fontFamily: "Arial Black, Gadget, sans-serif",
                                marginBottom: "10px",
                            }}
                        >
                            Créer un compte
                        </Button>
                    </Link>

                    <Link to="/" style={{ textDecoration: "none" }}>
                        <Button
                            variant="outlined"
                            fullWidth
                            style={{
                                color: "#fff",
                                borderColor: "#ffcc00",
                                fontFamily: "Arial Black, Gadget, sans-serif",
                            }}
                        >
                            Retour au menu
                        </Button>
                    </Link>
                </form>
            </Box>
        </Container>
    );
}

export default LoginAccountPage;
