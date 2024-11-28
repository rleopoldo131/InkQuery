
function fetchData(word, dictType = 'intermediate') {

    const dictCodes = {
        "intermediate": "sd3", "elementary": "sd2", "collegiate": "collegiate", "spanish": "spanish"
    };

    const dictKeys = {
        "intermediate": "a19c9426-51cf-4c68-af55-de3b8229f559",
        "elementary": "e59d86cd-4e68-4ffc-a389-9945b19a1f32",
        "collegiate": "95da4924-31ba-4752-b070-f434ec41a1ba",
        "spanish": "a29aabe7-82a8-4c85-8e27-3b0bb0d722d8"
    };

    const url = `https://dictionaryapi.com/api/v3/references/${dictCodes[dictType]}/json/${word}?key=${dictKeys[dictType]}`;

    return fetch(url)
    .then(response => {
        if (!response.ok) {
            console.error("Response not ok");
            throw new Error(response.status);
        }
        return response.json()
    })
    .catch(error => {
        console.error("Error fetching")
        console.error(error);
        throw error;
    });
}

export default function wm_getDef(word, dictType = 'intermediate') {
    return fetchData(word, dictType)
    .then(data => {
        return data[0].shortdef[0];
    })
    .catch(error => console.error(error));
}


// fetch(url)
//     .then(response => {
//         if (!response.ok) {
//             throw new Error(response.statusText);
//         }
//         return response.json()
//     })
//     .then(data => console.log(data))
//     .catch(error => console.error(error))

// async function fetchData(){
//
//     try{
//         const response = await fetch(url);
//         if (!response.ok) {
//             throw new Error(response.statusText);
//         }
//
//         const data = await response.json();
//         console.log(data);
//     }
//     catch(error){
//         console.error(error);
//     }
//
// }
