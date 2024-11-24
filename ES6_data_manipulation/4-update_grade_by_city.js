export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((student) => student.location === city)
    .map((student) => {

      const vargrade = newGrades.find((grade) => grade.studentId === student.id);

      return {
        ...student,
        grade: vargrade ? vargrade.grade : 'N/A',
      };
    });
}
