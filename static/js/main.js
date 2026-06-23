document.addEventListener( "DOMContentLoaded", function() {
    const create_account_checkbox=document.getElementById("id_create_account");
    const password_wrapper=document.getElementById("div_id_password");


    if(create_account_checkbox&&password_wrapper){

        create_account_checkbox.addEventListener("change", function () {
            toggle_password_visibility(create_account_checkbox,password_wrapper);
        });
        toggle_password_visibility(create_account_checkbox,password_wrapper);
    }


});

function toggle_password_visibility(create_account_checkbox,password_wrapper){
    password_wrapper.style.display = create_account_checkbox.checked? "block" : "none";
}