const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

// shows sign up form
signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

// shows login 
signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});