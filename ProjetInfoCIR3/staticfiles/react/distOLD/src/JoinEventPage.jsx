import React from "react";
import {Link} from "react-router-dom";

function JoinEventPage() {

    return (
        <div>
            <p>Join Event page</p>
            <div>
                <label>Code Event</label>
                <input
                    type="text"
                    id="code"
                    name="code"
                />
                <Link to="/show-event">
                    <button>Confirm</button>
                </Link>
            </div>
            <Link to="/">
                <button>Retour Menu</button>
            </Link>
        </div>
    );
}

export default JoinEventPage;