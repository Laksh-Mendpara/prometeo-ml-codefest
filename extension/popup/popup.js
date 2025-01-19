document.getElementById('sendMessage').addEventListener('click', () => {
    const inputMessage = document.getElementById('inputMessage').value;
  
    chrome.runtime.sendMessage(
      { type: 'sendToBackend', payload: inputMessage },
      (response) => {
        document.getElementById('response').textContent = response.reply;
      }
    );
  });
  