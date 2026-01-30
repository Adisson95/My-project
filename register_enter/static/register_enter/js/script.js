
const dateInput = document.getElementById('BirthDate');
const today = new Date().toISOString().split('T')[0];
dateInput.setAttribute('max', today);

function checkForm() {
    let fn = document.getElementById("name").value;
    let ln = document.getElementById("lastname").value;
    let em = document.getElementById("email").value;
    let pn = document.getElementById("number").value;
    let ps = document.getElementById("BirthDate").value;
    



    const patterns = {
        firsname: /^[А-Я][а-я]/,
        lastname: /^[А-Я][а-я]/,
        email: /^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/,
        number: /^\+7\(\d{3}\)\d{3}-\d{2}-\d{2}$/,
        BirthDate: /\d/
    }
    
    if (!patterns.name.test(fn)) {
        alert('You have the wrong name.')
        return false
    }    
    if (!patterns.lastname.test(ln)) {
        alert('lastname')
        return false
    }
    if (!patterns.email.test(em)) {
        alert('email')
        return false
    }
    if (!patterns.number.test(pn)) {
        alert('number')
        return false
    }
    if (!patterns.BirthDate.test(ps)) {
        alert('BirthDate')
        return false
    }
    
    return true;
}

function validateField(input, pattern) {
    const isValid = pattern.test(input.value);
    
    if (isValid) {
        input.style.borderColor = "green";
    } else {
        input.style.borderColor = "red";
    }
    
    return isValid;
}

document.addEventListener('DOMContentLoaded', function() {
    const patterns = {
        firsname: /^[А-Я][а-я]/,
        lastname: /^[А-Я][а-я]/,
        email: /^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/,
        number: /^\+7\(\d{3}\)\d{3}-\d{2}-\d{2}$/,
        password: /^(?=.*[A-Z])(?=.*[0-9]).{8,}$/
    };

    const firsnameInput = document.getElementById("firsname");
    const lastnameInput = document.getElementById("lastname");
    const emailInput = document.getElementById("email");
    const numberInput = document.getElementById("number");
    const passwordInput = document.getElementById("Password");

    firsnameInput.addEventListener('input', () => validateField(firsnameInput, patterns.firsname));
    lastnameInput.addEventListener('input', () => validateField(lastnameInput, patterns.lastname));
    emailInput.addEventListener('input', () => validateField(emailInput, patterns.email));
    numberInput.addEventListener('input', () => validateField(numberInput, patterns.number));
    passwordInput.addEventListener('input', () => validateField(passwordInput, patterns.password));
});