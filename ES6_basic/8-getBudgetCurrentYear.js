function getCurrentYear() {
    const date = new Date();
    return date.getFullYear();
  }
  
  export default function getBudgetForCurrentYear(income, gdp, capita) {
    const currentYear = getCurrentYear(); // Calculamos el año una vez para evitar múltiples llamadas.
  
    const budget = {
      [`income-${currentYear}`]: income,
      [`gdp-${currentYear}`]: gdp,
      [`capita-${currentYear}`]: capita,
    };
  
    return budget;
  }
  