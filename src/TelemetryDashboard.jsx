import React, { useEffect, useState } from "react";

function TelemetryDashboard() {
    const [data, setData] = useState(null);

    useEffect(() => {
        fetch("/api/telemetry/")
            .then((response) => response.json())
            .then((data) => setData(data))
            .catch((error) => console.error("Erreur lors du chargement des données :", error));
    }, []);

    if (!data) return <p>Chargement...</p>;

    return (
        <div>
            <h1>Tableau de bord Télémétrie</h1>
            <p>Total des requêtes : {data.total_requests}</p>
            <p>Temps de réponse moyen : {data.avg_response_time} secondes</p>
            <h2>Statistiques des codes de statut</h2>
            <ul>
                {data.status_counts.map((status) => (
                    <li key={status.status_code}>
                        {status.status_code} : {status.count} requêtes
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default TelemetryDashboard;
