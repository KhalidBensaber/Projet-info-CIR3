// utils/csrf.js

export async function getCSRFToken() {
    let csrfToken = null;

    // Check if the token exists in cookies
    if (document.cookie && document.cookie !== '') {
        document.cookie.split(';').forEach(cookie => {
            const trimmedCookie = cookie.trim();
            if (trimmedCookie.startsWith('csrftoken=')) {
                csrfToken = trimmedCookie.substring('csrftoken='.length);
            }
        });
    }

    // If no token found, fetch it from the server
    if (!csrfToken) {
        try {
            const response = await fetch('api/login/get-csrf-token/');
            if (response.ok) {
                const data = await response.json();
                csrfToken = data.csrfToken;
                // Set the token in the cookies for future use
                document.cookie = `csrftoken=${csrfToken}; path=/;`;
            } else {
                console.error('Failed to fetch CSRF token');
            }
        } catch (error) {
            console.error('Error fetching CSRF token:', error);
        }
    }

    return csrfToken;
}
