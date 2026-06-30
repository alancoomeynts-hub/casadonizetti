document.addEventListener( "DOMContentLoaded", function() {
    const confirm_profile_page = document.getElementById("profile-details");
    if (confirm_profile_page) {
        const deleteModal = document.getElementById('cancelReservationModal');
        const cancelConfirm = document.getElementById("cancelConfirm");
        const reservationText = document.getElementById("reservationModalText");

        if(deleteModal && cancelConfirm && reservationText) {
            deleteModal.addEventListener('show.bs.modal', function (event) {
                const button = event.relatedTarget;
                if (!button) return;

                const reservationDate = button.getAttribute('data-reservation-date');
                const reservationId = button.getAttribute('data-reservation-id');
                const cancelUrl = button.getAttribute('data-cancel-url');
                reservationText.textContent = reservationDate;
                cancelConfirm.action = cancelUrl


            });
        }

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
                editForm.action = editUrl

            });
        }
    }
});