
      function showLoading() {
        const loadingOverlay = document.getElementById('loading-overlay');
        loadingOverlay.classList.remove('hidden');
        loadingOverlay.classList.add('flex');
      }
    
      // Add click event to all internal links
      document.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', function(event) {
          if (this.hostname === window.location.hostname && this.href) {
            event.preventDefault();
            showLoading();
            setTimeout(() => {
              window.location.href = this.href;
            }, 500);
          }
        });
      });
