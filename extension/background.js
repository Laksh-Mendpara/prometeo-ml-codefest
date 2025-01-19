chrome.runtime.onInstalled.addListener(() => {
  console.log('Extension Installed');
});

// Example function to communicate with the backend
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === 'sendToBackend') {
    console.log("Backend Hai Hi Nahin Maa chudalo")
    // fetch('http://localhost:3000/data', {
    //   method: 'POST',
    //   headers: { 'Content-Type': 'application/json' },
    //   body: JSON.stringify({ message: message.payload }),
    // })
    //   .then((response) => response.json())
    //   .then((data) => sendResponse(data))
    //   .catch((error) => console.error(error));
    return true; // Keep the message channel open for async response
  }
});
