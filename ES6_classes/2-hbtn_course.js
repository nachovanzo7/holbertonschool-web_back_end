export default class HolbertonCourse
{
    constructor(name, length, students)
    {
        if (typeof name !== "string") 
            throw new TypeError("El nombre debe ser un string");
        
        if (typeof length !== "number") 
            throw new TypeError("Length debe ser un número");

        if (!Array.isArray(students)) 
            throw new TypeError("Students debe ser un array");

        this._name = name;
        this._length = length;
        this._students = students
    }

    get name()
    {
        return this._name;
    }

    set name(value){
        if (typeof value == "string")
            this._name = value;
        else
            console.error('El nombre debe ser un string');
    }

    get length(){
        return this._length;
    }

    set length(value){
        if (typeof length == "number")
            this._length = value;
        else
            console.error('Length debe ser un numero');
    }

    get students()
    {
        return this._students;
    }

    set students(value){
        if (Array.isArray(value))
            this._students = value;
        else
            console.error('Length debe ser un array');
    }
}
