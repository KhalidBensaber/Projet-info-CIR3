import React, { useState } from "react";
import { Button, Container, Typography, TextField, Box, Alert, MenuItem, Select, InputLabel, FormControl } from "@mui/material";
import { Link } from "react-router-dom";
import { getCSRFToken } from "@/utils/csrf";


function SignUpPage() {
    const [formData, setFormData] = useState({
        first_name: "",
        last_name: "",
        username: "",
        email: "",
        password1: "",
        password2: "",
        status: "spectator", // Valeur par défaut
    });
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
        const response = await fetch("/api/register/", {
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
            setError(
                data.errors
                    ? Object.values(data.errors).flat().join(", ")
                    : data.message
            );
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
                    Créer un compte
                </Typography>

                <form onSubmit={handleSubmit}>
                    <TextField
                        label="Prénom"
                        name="first_name"
                        fullWidth
                        value={formData.first_name}
                        onChange={handleChange}
                        required
                        style={{ marginBottom: "15px", backgroundColor: "#1a1a1a" }}
                        inputProps={{ style: { color: "#fff" } }}
                        InputLabelProps={{ style: { color: "#fff" } }}
                    />
                    <TextField
                        label="Nom"
                        name="last_name"
                        fullWidth
                        value={formData.last_name}
                        onChange={handleChange}
                        required
                        style={{ marginBottom: "15px", backgroundColor: "#1a1a1a" }}
                        inputProps={{ style: { color: "#fff" } }}
                        InputLabelProps={{ style: { color: "#fff" } }}
                    />
                    <TextField
                        label="Nom d'utilisateur"
                        name="username"
                        fullWidth
                        value={formData.username}
                        onChange={handleChange}
                        required
                        style={{ marginBottom: "15px", backgroundColor: "#1a1a1a" }}
                        inputProps={{ style: { color: "#fff" } }}
                        InputLabelProps={{ style: { color: "#fff" } }}
                    />
                    <TextField
                        label="Email"
                        name="email"
                        type="email"
                        fullWidth
                        value={formData.email}
                        onChange={handleChange}
                        required
                        style={{ marginBottom: "15px", backgroundColor: "#1a1a1a" }}
                        inputProps={{ style: { color: "#fff" } }}
                        InputLabelProps={{ style: { color: "#fff" } }}
                    />

                    <FormControl fullWidth style={{ marginBottom: "15px" }}>
                        <InputLabel style={{ color: "#fff" }}>Statut</InputLabel>
                        <Select
                            name="status"
                            value={formData.status}
                            onChange={handleChange}
                            style={{
                                color: "#fff",
                                backgroundColor: "#1a1a1a",
                            }}
                        >
                            <MenuItem value="spectator">Spectator</MenuItem>
                            <MenuItem value="player">Player</MenuItem>
                            <MenuItem value="special-status">Special Status</MenuItem>
                        </Select>
                    </FormControl>

                    <TextField
                        label="Mot de passe"
                        name="password1"
                        type="password"
                        fullWidth
                        value={formData.password1}
                        onChange={handleChange}
                        required
                        style={{ marginBottom: "15px", backgroundColor: "#1a1a1a" }}
                        inputProps={{ style: { color: "#fff" } }}
                        InputLabelProps={{ style: { color: "#fff" } }}
                    />
                    <TextField
                        label="Confirmer le mot de passe"
                        name="password2"
                        type="password"
                        fullWidth
                        value={formData.password2}
                        onChange={handleChange}
                        required
                        style={{ marginBottom: "15px", backgroundColor: "#1a1a1a" }}
                        inputProps={{ style: { color: "#fff" } }}
                        InputLabelProps={{ style: { color: "#fff" } }}
                    />
                    <Button
                        type="submit"
                        variant="contained"
                        fullWidth
                        style={{
                            backgroundColor: "#ffcc00",
                            color: "#fff",
                            marginBottom: "20px",
                            fontWeight: "bold",
                            fontFamily: "Arial Black, Gadget, sans-serif",
                        }}
                    >
                        S'inscrire
                    </Button>
                </form>
                {error && <Alert severity="error" style={{ marginTop: "20px" }}>{error}</Alert>}
                {success && <Alert severity="success" style={{ marginTop: "20px" }}>Compte créé avec succès !</Alert>}
                <Link to="/login-account" style={{ textDecoration: "none" }}>
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
                        Retour à la connexion
                    </Button>
                </Link>

                <Link to="/" style={{ textDecoration: "none" }}>
                    <Button variant="outlined" fullWidth style={{ color: "#fff", borderColor: "#ffcc00", fontFamily: 'Arial Black, Gadget, sans-serif' }}>
                        Retour Menu
                    </Button>
                </Link>
            </Box>
        </Container>
    );
}

export default SignUpPage;
