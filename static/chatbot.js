// chatbot.js

// Function to beautify and position the chatbot window
function beautifyChatbotWindow() {
    var chatContainer = document.getElementById("chat-container");
    chatContainer.style.position = "fixed";
    chatContainer.style.bottom = "20px";
    chatContainer.style.right = "20px";
    chatContainer.style.backgroundColor = "#f5f5f5";
    chatContainer.style.borderRadius = "5px";
    chatContainer.style.boxShadow = "0px 2px 5px rgba(0, 0, 0, 0.2)";
    chatContainer.style.padding = "10px";
    chatContainer.style.maxWidth = "400px";
    chatContainer.style.zIndex = "1000";
}

// Call the function when the window loads
window.onload = function () {
    beautifyChatbotWindow();
};
