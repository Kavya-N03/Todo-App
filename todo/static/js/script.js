// Toggle theme
function toggleTheme(){
  const body = document.getElementById('page-body');
  const toggleBtn = document.getElementById('toggle-btn');
  const isDark = body.classList.toggle('dark')

  toggleBtn.textContent = isDark?'🌙Dark Mode':'☀️Light Mode';
  localStorage.setItem('theme',isDark?'dark':'light');
}

//Previously saved theme
function applysavedTheme(){
  const body = document.getElementById('page-body');
  const toggleBtn = document.getElementById('toggle-btn');
  const savedTheme = localStorage.getItem('theme');

  if(savedTheme === 'dark'){
    body.classList.add('dark');
    toggleBtn.textContent = "🌙Dark Mode";
  }else{
    body.classList.remove('dark');
    toggleBtn.textContent = "☀️Light Mode";
  }
}

window.onload = function(){
  applysavedTheme();
  document.getElementById('toggle-btn').addEventListener('click',toggleTheme);
}