// Show/hide password onClick of button using Javascript only


function show(element_id) {
	var input_element = element_id.replace("-icon", "").replace("-", "_");
	var input_element = document.getElementsByName(input_element)[0];
	var input_icon = document.getElementById(element_id);

	input_icon.setAttribute("class", "bi bi-eye");
	input_element.setAttribute("type", "text");
}


function hide(element_id) {
	var input_element = element_id.replace("-icon", "").replace("-", "_");
	var input_element = document.getElementsByName(input_element)[0];
	var input_icon = document.getElementById(element_id);

	input_icon.setAttribute("class", "bi bi-eye-fill");
	input_element.setAttribute("type", "password");
}


var pwShown = 0;
eye_element = document.querySelectorAll("#password-icon, #confirm-password-icon")

eye_element.forEach(
	item => {
  	item.addEventListener('click', event => {
			current_element_id = event.target.id			
			if (pwShown == 0) {
				pwShown = 1;
				show(current_element_id);
			} 
			else {
				pwShown = 0;
				hide(current_element_id);
			}
  })
})

