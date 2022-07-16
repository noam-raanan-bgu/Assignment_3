console.log("Im inside of JS");

function getUsers(){
    const value = document.getElementById('input_number').value;
    fetch(`https://reqres.in/api/users/${value}`).then(
        response => response.json()
    ).then(
        response_obj => users_in_html(response_obj.data)
    ).catch(
        err => console.log(err)
    )
}


function users_in_html(response_obj_data) {
    // console.log(response_obj_data);

    const curr_main = document.querySelector("main");
        const section = document.createElement('section');
        section.innerHTML = `
        <p>
        <img src="${response_obj_data.avatar}" alt="Profile Picture"/>
        <div>
            <span>${response_obj_data.first_name} ${response_obj_data.last_name}</span>
            <br>
            <a href="mailto:${response_obj_data.email}">Send an email</a>
        </div>
        </p>
        `;
        curr_main.innerHTML = section.innerHTML;




}