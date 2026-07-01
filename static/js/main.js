document.addEventListener( "DOMContentLoaded", function() {
    const confirm_profile_page = document.getElementById("profile-details");
    if (!confirm_profile_page) return;

    setupEditModal();
    setupCancelModal();

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