export function taskFirst() {
    const task = 'I prefer const when I can.';
    return task;
  }
  
  export function getLast() {
    return ' is okay';
  }
  
  export function taskNext() {
    // Usamos let porque 'combination' cambia su valor con "+="
    let combination = 'But sometimes let';
    combination += getLast();
  
    return combination;
  }
  