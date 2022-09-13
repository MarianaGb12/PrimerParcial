# PrimerParcial


# Library Management System
PROBLEMA: The user can do many things in the Library Management system. 
The user can borrow a book, return a book and display available books. The Librarian should be able 
to upload a list of books and modify such list if a book is lost or damaged. You should be able to 
browse all the available collections or find a book by searching (you only need to think in exact 
string matching, not approximate)

UML Diagram:

![image](https://user-images.githubusercontent.com/98919850/189922148-39958f36-1f49-4688-9e04-772aa785daf7.png)

UML explanation: 
Para crear el manejo del sistema de la librería creé dos clases. 
Una clase denominada Librarian, que tiene como atributos el nombre y la lista de libros.
Esta cuenta con dos métodos que permitirán actualizar la lista de libros (enfoque en
agregar un nuevo libro) y modificar la lista de los libros (libros que fueron dañados 
o perdidos). La otra clase creada es la de User que tiene como atributos nombre y id. 
Cuenta con tres métodos que permiten prestar un libro, regresar un libro y disponer de los 
libros disponibles. 
