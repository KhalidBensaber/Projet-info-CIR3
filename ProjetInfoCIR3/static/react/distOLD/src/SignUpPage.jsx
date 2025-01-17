import React, { useState } from "react";
import { Link } from "react-router-dom";
import { Button, Container, Typography, TextField, Box, Alert } from "@mui/material";

function SignUpPage() {
    const [formData, setFormData] = useState({
        username: "",
        email: "",
        password: "",
        confirmPassword: "",
    });
    const [error, setError] = useState("");

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (formData.password !== formData.confirmPassword) {
            setError("Les mots de passe ne correspondent pas.");
            return;
        }
        setError("");
        console.log("Compte créé avec succès :", formData);
    };

    return (
        <Container style={{ minHeight: "100vh", display: "flex", justifyContent: "center", alignItems: "center", backgroundColor: "#1a1a1a" }}>
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
                <Typography variant="h4" style={{ marginBottom: "20px", color: "#ffcc00", fontFamily: 'Arial Black, Gadget, sans-serif' }}>
                    Créer un compte
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
                        inputProps={{ style: { color: "#fff", fontFamily: 'Arial Black, Gadget, sans-serif' } }}
                        required
                    />

                    <TextField
                        label="Adresse Email"
                        name="email"
                        type="email"
                        variant="outlined"
                        fullWidth
                        value={formData.email}
                        onChange={handleChange}
                        style={{ marginBottom: "20px", backgroundColor: "#1a1a1a" }}
                        InputLabelProps={{ style: { color: "#fff" } }}
                        inputProps={{ style: { color: "#fff", fontFamily: 'Arial Black, Gadget, sans-serif' } }}
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
                        inputProps={{ style: { color: "#fff", fontFamily: 'Arial Black, Gadget, sans-serif' } }}
                        required
                    />

                    <TextField
                        label="Confirmer le mot de passe"
                        name="confirmPassword"
                        type="password"
                        variant="outlined"
                        fullWidth
                        value={formData.confirmPassword}
                        onChange={handleChange}
                        style={{ marginBottom: "20px", backgroundColor: "#1a1a1a" }}
                        InputLabelProps={{ style: { color: "#fff" } }}
                        inputProps={{ style: { color: "#fff", fontFamily: 'Arial Black, Gadget, sans-serif' } }}
                        required
                    />

                    {error && (
                        <Alert severity="error" style={{ marginBottom: "20px" }}>
                            {error}
                        </Alert>
                    )}

                    <Button
                        type="submit"
                        variant="contained"
                        fullWidth
                        style={{ backgroundColor: "#ff0000", color: "#fff", marginBottom: "20px", fontWeight: "bold", fontFamily: 'Arial Black, Gadget, sans-serif' }}
                    >
                        Créer mon compte
                    </Button>

                    <Link to="/" style={{ textDecoration: "none" }}>
                        <Button variant="outlined" fullWidth style={{ color: "#fff", borderColor: "#ffcc00", fontFamily: 'Arial Black, Gadget, sans-serif' }}>
                            Retour Menu
                        </Button>
                    </Link>
                </form>
            </Box>
        </Container>
    );
}

export default SignUpPage;
