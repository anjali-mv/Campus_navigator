console.log("JS loaded");

// Wait for DOM to fully load
document.addEventListener("DOMContentLoaded", () => {

    const chatArea = document.querySelector(".chat-area");
    const userInput = document.getElementById("userInput");
    const gpsBtn = document.getElementById("gpsBtn");
    const sendBtn = document.querySelector(".input-area button"); // first button is Send

    // 1️⃣ Function to add messages to chat
    function addMessage(text, sender) {
        const msg = document.createElement("div");
        msg.className = "chat " + sender;
        msg.innerText = text;
        chatArea.appendChild(msg);
        chatArea.scrollTop = chatArea.scrollHeight; // auto-scroll
    }

    // 2️⃣ Send message to backend
    function sendMessage() {
        const message = userInput.value.trim();
        if (message === "") return;

        addMessage(message, "user");
        userInput.value = "";

        fetch("http://127.0.0.1:5000/ask", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: message })
        })
        .then(res => res.json())
        .then(data => {
            addMessage(data.bot_reply, "bot");
        })
        .catch(() => {
            addMessage("❌ Backend not running", "bot");
        });
    }

    // 3️⃣ GPS / Location function
    function getLocation() {
        if (!navigator.geolocation) {
            addMessage("❌ GPS not supported by browser", "bot");
            return;
        }

        navigator.geolocation.getCurrentPosition(
            position => {
                const lat = position.coords.latitude;
                const lng = position.coords.longitude;

                addMessage(
                    `📍 Your Current Location:\nLatitude: ${lat}\nLongitude: ${lng}\n` +
                    `View on map: https://www.google.com/maps?q=${lat},${lng}`,
                    "bot"
                );
            },
            () => {
                addMessage("❌ Location permission denied", "bot");
            }
        );
    }

    // 4️⃣ Attach click events
    gpsBtn.addEventListener("click", getLocation);
    sendBtn.addEventListener("click", sendMessage);

    // 5️⃣ Optional: Send message on Enter key
    userInput.addEventListener("keypress", e => {
        if (e.key === "Enter") sendMessage();
    });

});