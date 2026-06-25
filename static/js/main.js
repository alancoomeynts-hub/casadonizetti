document.addEventListener( "DOMContentLoaded", function() {

    const deleteModal=document.getElementById('cancelReservationModal');
    const cancelConfirm = document.getElementById("cancelConfirm");
    const reservationText = document.getElementById("reservationModalText");

    deleteModal.addEventListener('show.bs.modal', function (event) {
        const button = event.relatedTarget;
        const reservationDate = button.getAttribute('data-reservation-date');
        const reservationId = button.getAttribute('data-reservation-id');
        const cancelUrl = button.getAttribute('data-cancel-url');
        reservationText.textContent=reservationDate;
        cancelConfirm.action=cancelUrl




});

});