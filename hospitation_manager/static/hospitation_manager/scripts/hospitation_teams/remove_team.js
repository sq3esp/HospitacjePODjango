const csrftoken = getCookie('csrftoken');

function removeTeam(id) {
    removeRequest(id)
        .then(() => {
            window.location.replace('/hospitation_teams/')
        })
}

async function removeRequest(id) {
    await fetch('/hospitation_teams/delete/' + id, {
        method: 'DELETE',
        mode: 'cors',
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            'X-CSRFToken': csrftoken
        }
    })
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}