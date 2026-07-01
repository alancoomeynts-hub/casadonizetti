document.addEventListener( "DOMContentLoaded", function() {
    const confirm_profile_page = document.getElementById("profile-details");
    const confirm_contact_us_page = document.getElementById("contact-us-form");
    if (confirm_profile_page) {
        setupEditModal();
        setupCancelModal();
    }

    if(confirm_contact_us_page){

        togglePrivateDiningFields();
    }

});
/**
 * Set up the edit reservation modal.
 * Populates the form fields and updates the form action URL
 * when the Bootstrap edit modal is opened.
 */
function setupEditModal(){
        const editModal = document.getElementById('editReservationModal');
        const editForm = document.getElementById("editReservationForm");
        const partySizeInput = document.getElementById("id_party_size");
        const dateInput = document.getElementById("id_reservation_date");
        const timeInput = document.getElementById("id_reservation_time");

        if(editModal && editForm && partySizeInput && dateInput && timeInput) {
            editModal.addEventListener('show.bs.modal', function (event) {
                const button = event.relatedTarget;
                if (!button) return;


                const reservationDate = button.getAttribute('data-reservation-date');
                const reservationTime = button.getAttribute('data-reservation-time');
                const reservationPartySize = button.getAttribute('data-reservation-party-size');
                const editUrl = button.getAttribute('data-edit-url');

                dateInput.value = reservationDate;
                timeInput.value = reservationTime;
                partySizeInput.value = reservationPartySize;
                editForm.action = editUrl;

            });
        }

}
/**
 * Set up the cancel reservation modal.
 * Updates the confirmation text and sets the cancel form action URL
 * when the Bootstrap cancel modal is opened.
 */
function setupCancelModal() {
    const deleteModal = document.getElementById('cancelReservationModal');
    const cancelConfirm = document.getElementById("cancelConfirm");
    const reservationText = document.getElementById("reservationModalText");

    if (deleteModal && cancelConfirm && reservationText) {
        deleteModal.addEventListener('show.bs.modal', function (event) {
                const button = event.relatedTarget;
                if (!button) return;

                const reservationDate = button.getAttribute('data-reservation-date');
                const reservationTable = button.getAttribute('data-reservation-table');
                const cancelUrl = button.getAttribute('data-cancel-url');
                reservationText.textContent = reservationDate + " at " + reservationTable;
                cancelConfirm.action = cancelUrl;


        });

    }
}
/**
 * Toggles the visibility of party size and reservation for fields based on the selected request type in the contact us form.
 */
function togglePrivateDiningFields(){
    const requestType = document.getElementById("id_request_type");
    const partySize=document.getElementById("div_id_party_size");
    const partySizeInput=document.getElementById("id_party_size");
    const reservationFor=document.getElementById("div_id_reservation_for");
    const reservationForInput=document.getElementById("id_reservation_for");

    function togglePrivateDiningFields() {
        if (requestType.value === "private_dining") {
            partySize.style.display = "block";
            partySizeInput.required = true;
            reservationFor.style.display = "block";
            reservationForInput.required = true;
        } else {
            partySize.style.display = "none";
            partySizeInput.required = false;
            reservationFor.style.display = "none";
            reservationForInput.required = false;
        }
    }
    requestType.addEventListener("change", togglePrivateDiningFields);
    togglePrivateDiningFields();

}


