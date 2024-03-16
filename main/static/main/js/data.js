const getCurrentDateAsString = () => {
    const today = new Date();
    return `${today.getFullYear()}-${String(today.getMonth() + 1).padStart(2, '0')}-${String(today.getDate()).padStart(2, '0')}`;
   };
   
   document.addEventListener("DOMContentLoaded", () => {
    document.querySelector('input[name="date"]').value = getCurrentDateAsString();
   });
