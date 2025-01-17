import React, { useState } from "react";
import {Link} from "react-router-dom";

export function CreateEventPage() {
    const [players, setPlayers] = useState([]); // Liste des participants
    const [add, setAdd] = useState(''); // Champ d'ajout de participant
    const [editingPlayer, setEditingPlayer] = useState(null); // Participant en cours de modification
    const [newPseudo, setNewPseudo] = useState(''); // Nouveau pseudo proposé

    // Fonction pour ajouter un participant
    const handleAddParticipant = () => {
        if (add.trim() === '') {
            alert("Veuillez entrer un pseudo avant d'ajouter un participant !");
            return;
        }
        setPlayers([...players, { participant: add, code: generateCode() }]);
        setAdd('');
    };

    // Fonction pour supprimer un participant
    const handleDeleteParticipant = (code) => {
        setPlayers((prev) => prev.filter((player) => player.code !== code));
    };

    // Fonction pour générer un code aléatoire avec un #
    const generateCode = () => {
        const characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        let code = "#";
        for (let i = 0; i < 6; i++) {
            code += characters.charAt(Math.floor(Math.random() * characters.length));
        }
        return code;
    };

    // Ouvrir la fenêtre de modification
    const openEditWindow = (player) => {
        setEditingPlayer(player);
        setNewPseudo(player.participant);
    };

    // Appliquer la modification du pseudo
    const handleEditParticipant = () => {
        setPlayers((prev) =>
            prev.map((p) =>
                p.code === editingPlayer.code
                    ? { ...p, participant: newPseudo }
                    : p
            )
        );
        setEditingPlayer(null);
        setNewPseudo('');
    };

    // Annuler la modification
    const closeEditWindow = () => {
        setEditingPlayer(null);
        setNewPseudo('');
    };

    return (
        <div style={styles.page}>
            <Menu />
            <div style={styles.container}>
                <Add
                    add={add}
                    onAddChange={setAdd}
                    onAddParticipant={handleAddParticipant}
                />
                <PlayersData
                    players={players}
                    onEdit={openEditWindow}
                    onDelete={handleDeleteParticipant}
                />
                <button
                    style={styles.validateButton}
                    onClick={() => alert("Validation effectuée !")}
                >
                    Valider
                </button>
            </div>

            {/* Mini-fenêtre de modification */}
            {editingPlayer && (
                <div style={styles.modalBackdrop}>
                    <div style={styles.modal}>
                        <h3 style={{ color: "#ff0000" }}>Modifier le pseudo</h3>
                        <input
                            type="text"
                            value={newPseudo}
                            onChange={(e) => setNewPseudo(e.target.value)}
                            style={styles.input}
                        />
                        <div style={styles.modalActions}>
                            <button style={styles.addButton} onClick={handleEditParticipant}>
                                Valider
                            </button>
                            <button style={styles.resetButton} onClick={closeEditWindow}>
                                Annuler
                            </button>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
}

// Menu en haut de la page
function Menu() {
    return (
        <div style={styles.menu}>
            <Link to="/">
                <button
                    style={styles.menuButton}
                    /*onClick={() => alert("Retour à la page précédente !")}*/
                >
                    Retour
                </button>
            </Link>

        </div>
    );
}

// Composant d'ajout de participant
function Add({add, onAddChange, onAddParticipant}) {
    return (
        <div style={styles.addContainer}>
            <input
                type="text"
                style={styles.input}
                value={add}
                placeholder="Ajouter un participant"
                onChange={(e) => onAddChange(e.target.value)}
            />
            <button style={styles.addButton} onClick={onAddParticipant}>
                Ajouter
            </button>
        </div>
    );
}

// Affichage des participants
function PlayersData({ players, onEdit, onDelete }) {
    return (
        <table style={styles.table}>
            <thead>
            <tr>
                <th style={styles.header}>Participant</th>
                <th style={styles.header}>Code</th>
                <th style={styles.header}></th>
            </tr>
            </thead>
            <tbody>
            {players.map((player, index) => (
                <PlayerRow
                    key={index}
                    player={player}
                    onEdit={onEdit}
                    onDelete={onDelete}
                />
            ))}
            </tbody>
        </table>
    );
}

// Ligne d'un participant
function PlayerRow({ player, onEdit, onDelete }) {
    return (
        <tr style={styles.row}>
            <td style={styles.cell}>{player.participant}</td>
            <td style={styles.cell}>{player.code}</td>
            <td style={styles.cell}>
                <button
                    style={styles.deleteButton}
                    onClick={() => onDelete(player.code)}
                >
                    X
                </button>
            </td>
        </tr>
    );
}

// Styles
const styles = {
    page: {
        backgroundColor: "#1e1e1e",
        color: "#fff",
        fontFamily: '"Orbitron", sans-serif',
        padding: "20px",
        minHeight: "100vh",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        gap: "20px",
    },
    menu: {
        width: "100%",
        backgroundColor: "#2c2c2c",
        padding: "10px",
        marginBottom: "20px",
        display: "flex",
        justifyContent: "flex-start",
    },
    menuButton: {
        backgroundColor: "#ff0000",
        color: "#fff",
        border: "none",
        borderRadius: "5px",
        padding: "10px 15px",
        cursor: "pointer",
        fontSize: "16px",
        fontWeight: "bold",
        fontFamily: '"Orbitron", sans-serif',
    },
    container: {
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        gap: "20px",
        width: "100%",
        maxWidth: "600px",
    },
    table: {
        width: "100%",
        borderCollapse: "collapse",
        backgroundColor: "#2c2c2c",
        color: "#fff",
    },
    header: {
        textAlign: "left",
        fontWeight: "bold",
        padding: "10px",
        borderBottom: "2px solid #ff0000",
        color: "#ff0000",
    },
    row: {
        borderBottom: "1px solid #444",
        transition: "background 0.3s",
    },
    cell: {
        padding: "10px",
        textAlign: "left",
    },
    addContainer: {
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        gap: "10px",
        width: "100%",
    },
    addButton: {
        backgroundColor: "#ff0000",
        color: "#fff",
        border: "none",
        borderRadius: "5px",
        padding: "10px 15px",
        cursor: "pointer",
        fontSize: "16px",
        fontWeight: "bold",
    },
    validateButton: {
        backgroundColor: "#ff0000",
        color: "#fff",
        border: "none",
        borderRadius: "5px",
        padding: "10px 15px",
        fontSize: "16px",
        fontWeight: "bold",
        cursor: "pointer",
        textTransform: "uppercase",
    },
    deleteButton: {
        backgroundColor: "#ff0000",
        color: "#fff",
        border: "none",
        borderRadius: "5px",
        padding: "5px 10px",
        cursor: "pointer",
        fontWeight: "bold",
    },
    input: {
        width: "100%",
        padding: "10px",
        fontSize: "16px",
        border: "1px solid #444",
        borderRadius: "5px",
        backgroundColor: "#2c2c2c",
        color: "#fff",
    },
};

export default CreateEventPage
// Log to console
console.log('Ça marche');