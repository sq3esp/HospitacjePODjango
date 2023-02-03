const UPDATE_URI = '/appeal_responses/edit/'
const id = JSON.parse(document.getElementById('appeal-data').textContent);
const csrftoken = getCookie('csrftoken');

const acceptButton = document.querySelector('#accept');
const declineButton = document.querySelector('#decline');


acceptButton.addEventListener('click', () => {
    sendUpdateRequest('accept')
        .then(() => {
            window.location.replace('/appeal_responses/')
        })
})

declineButton.addEventListener('click', () => {
    sendUpdateRequest('decline')
        .then(() => {
            window.location.replace('/appeal_responses/')
        })
})

// status = 'accept' | 'decline'
async function sendUpdateRequest(status) {
    const dean_response = document.querySelector('#dean_response').value;
    const data = {
        status,
        dean_response
    }

    await fetch(UPDATE_URI + id, {
        method: 'PUT',
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(data)
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
