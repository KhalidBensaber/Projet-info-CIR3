import React from "react";
import {Link} from "react-router-dom";

function ShowEventPage() {

    return (
        <div>
            <p>Show Event page</p>
            <Link to="/">
                <button>Retour Menu</button>
            </Link>
        </div>
    );
}

export default ShowEventPage;