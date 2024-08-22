document.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById('add-competition-form');
  
  form.addEventListener('submit', function(e) {
      e.preventDefault();

      // Collect form data
      const type = document.querySelector('.select-menu:nth-child(2) .sBtn-text').innerText;
      const field = document.querySelector('.select-menu:nth-child(3) .sBtn-text').innerText;
      const deadline = document.getElementById('deadline').value;

      // Validate form data
      if (type === 'Type' || field === 'Filière' || !deadline) {
          alert('Please fill in all fields');
          return;
      }

      // Create FormData object
      const formData = new FormData();
      formData.append('type', type);
      formData.append('field', field);
      formData.append('deadline', deadline);

      // Send data to server
      fetch('/api/add-competition/', {
          method: 'POST',
          body: formData,
          headers: {
              'X-CSRFToken': getCookie('csrftoken'),
          },
          credentials: 'same-origin'
      })
      .then(response => {
          if (!response.ok) {
              throw new Error('Network response was not ok');
          }
          return response.json();
      })
      .then(data => {
          if (data.success) {
              alert('Competition launched successfully!');
              // Clear the form
              form.reset();
              // Reset select menus
              document.querySelectorAll('.select-menu .sBtn-text').forEach(span => {
                  span.innerText = span.closest('.select-menu').querySelector('.option-text').innerText;
              });
          } else {
              alert('Error launching competition: ' + (data.error || 'Unknown error'));
          }
      })
      .catch(error => {
          console.error('Error:', error);
          alert('An error occurred while launching the competition: ' + error.message);
      });
  });
});

// Function to get CSRF token
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}