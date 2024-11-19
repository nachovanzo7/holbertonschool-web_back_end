export default function createReportObject(employeesList) {
    return {allEmployees: employeesList, //Propiedad
      getNumberOfDepartments(employees) //Metodo
      {
        return Object.keys(employees).length; //Obtener array
      },
    };
  }
  