import unittest
from oop import Materia, Profesor, Alumno

class TestMateria(unittest.TestCase):
    def test_materia(self):
        nombre = "Computación"
        profesores = "Daniel"
        alumno1 = Alumno("Victoria", "62340", "20", "mvb.torres")
        alumno2 = Alumno("Celina", "62146", "20", "celi.gd")
        alumnos = [alumno1,alumno2]
        materia = Materia(nombre, profesores,alumnos)
        self.assertEqual(materia.__nombre__, nombre)
        self.assertEqual(materia.__profesores__, profesores)
        self.assertEqual(materia.__alumnos__, alumnos)

    def test_obtener(self):
        profesores = "Daniel"
        alumno1 = Alumno("Victoria", "62340", "20", "mvb.torres")
        alumno2 = Alumno("Celina", "62146", "20", "celi.gd")
        alumnos = [alumno1,alumno2]
        materia = Materia("Computación", profesores,alumnos)

        self.assertEqual(materia.obtener_profesores(), profesores)

    def test_cambiar(self):
        nombre = "Computación"
        alumno1 = Alumno("Victoria", "62340", "20", "mvb.torres")
        alumno2 = Alumno("Celina", "62146", "20", "celi.gd")
        alumnos = [alumno1,alumno2]
        materia = Materia(nombre, "Daniel",alumnos)
        materia.cambiar_nombre("Programación")

        self.assertEqual(materia.__nombre__, "Programación")

    def test_obtener_alumnos(self):
        alumno2 = Alumno("Celina", "62146", "20", "celi.gd")
        alumno3 = Alumno('Victoria','62725','20','mvb.torres')
        alumno1 = Alumno("Valentina", "62080", "20", "mv.artola")
        alumnos = [alumno1,alumno2,alumno3]
        
        materia = Materia('Computacion','Daniel',alumnos)
        self.assertEqual(materia.obtener_alumnos(),alumnos)

class TestProfesor(unittest.TestCase):
    def test_profesor(self):
        profesores = Profesor("Darío", "JTP", "3423")
        self.assertEqual(profesores.__nombre__, "Darío")
        self.assertEqual(profesores.__cargo__, "JTP")
        self.assertEqual(profesores.__legajo__, "3423")

    def test_obtener_nomnbre(self):
        profesores = Profesor("Darío", "JTP", "3423")
        self.assertEqual(profesores.obtener_nombre(), "Darío")

    def test_obtener_cargo(self):
        profesores = Profesor("Darío", "JTP", "3423")
        self.assertEqual(profesores.obtener_cargo(), "JTP")

    def test_obtener_legajo(self):
        profesores = Profesor("Darío", "JTP", "3423")
        self.assertEqual(profesores.obtener_legajo(), "3423")

class TestAlumno(unittest.TestCase):
    def test_alumno(self):
        alumno = Alumno("Victoria", "62980", "20", "mvb.torres")
        self.assertEqual(alumno.__nombre__, "Victoria")
        self.assertEqual(alumno.__legajo__, "62980")
        self.assertEqual(alumno.__edad__, "20")
        self.assertEqual(alumno.__mail__, "mvb.torres") 

    def test_obtener_nombre(self):
        alumno = Alumno("Victoria", "62080", "20", "mvb.torres")
        self.assertEqual(alumno.obtener_nombre(), "Victoria")

    def test_cambiar_mail(self):
        mail = "mvb.torres"
        alumno = Alumno("Victoria", "62080", "20", mail)
        alumno.cambiar_mail("vicky.torres")
        self.assertEqual(alumno.__mail__, "vicky.torres")


if __name__ == '__main__':
    unittest.main()