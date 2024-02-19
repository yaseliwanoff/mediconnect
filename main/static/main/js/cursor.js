document.addEventListener('DOMContentLoaded', () => {
  const cursor = document.createElement('div');
  cursor.classList.add('custom-cursor');
  document.body.appendChild(cursor);

  function moveCursor(x, y) {
    cursor.style.left = x + 'px';
    cursor.style.top = y + 'px';
  }

  document.addEventListener('mousemove', (e) => {
    moveCursor(e.clientX, e.clientY);
  });

  document.addEventListener('mousedown', () => {
    cursor.classList.add('pressed');
  });

  document.addEventListener('mouseup', () => {
    cursor.classList.remove('pressed');
  });
})