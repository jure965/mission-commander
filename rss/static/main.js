window.addEventListener("load", function () {
    flatpickr(".flatpickr", {
        enableTime: true,
        dateFormat: "Y-m-d H:i:S",
        time_24hr: true,
    });
}, false);
