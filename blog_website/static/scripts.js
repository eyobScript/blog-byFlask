// Flash message handling
document.querySelectorAll('.flash-message').forEach(function(message) {
    setTimeout(function() {
        message.classList.add('hidden');
        setTimeout(() => message.style.display = 'none', 300);
    }, 3000);
    const closeBtn = message.querySelector('.close-btn');
    if (closeBtn) {
        closeBtn.addEventListener('click', function() {
            message.classList.add('hidden');
            setTimeout(() => message.style.display = 'none', 300);
        });
    }
});

// Comment area toggle
document.querySelectorAll('.comment-span').forEach(span => {
    span.addEventListener('click', () => {
        const commentArea = span.closest('.post-preview').querySelector('.comment-area');
        if (commentArea.style.display === 'none' || commentArea.style.display === '') {
            commentArea.style.display = 'block';
        } else {
            commentArea.style.display = 'none';
        }
    });
});

//
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.cancel-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const checkbox = this.closest('.comment-content').querySelector('.edit-toggle');
            if (checkbox) {
                checkbox.checked = false; // Unchecks the checkbox, hiding the form
            }
        });
    });
});