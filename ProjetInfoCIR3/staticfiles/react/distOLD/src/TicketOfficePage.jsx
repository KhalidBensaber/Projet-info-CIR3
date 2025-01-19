import React from "react";
import {Link} from "react-router-dom";

function TicketOfficePage() {

    return (
        <div>
            <p>Ticket Office page</p>
            <Link to="/">
                <button>Retour Menu</button>
            </Link>
        </div>
    );
}

export default TicketOfficePage;