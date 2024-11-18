export default function taskBlock(trueOrFalse) {
    const task = false; 
    const task2 = true;
  
    if (trueOrFalse) { //No cambia el valor fuera del if
      let task = true;
      let task2 = false;
    }
  
    return [task, task2];
  }
  