export default class ClassRoom
{
    constructor(maxStudentsSize)
    {
        this._maxStudentsSize = maxStudentsSize;
    }

    initializeRooms() {
        const class1 = new ClassRoom(19);
        const class2 = new ClassRoom(20);
        const class3 = new ClassRoom(34);
        return [class1, class2, class3];
    }
}