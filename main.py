class Node:
    def __init__ (self, data = None, next = None):
        self.data = data #Se crea un atributo para guardar el dato
        self.next = next #Se crea un atributo para guardar el nodo siguiente



class LinkedList:
    def __init__ (self):
        self.head = None #Se crea una cabeza vacia


    #Metodo para agregar un nodo al inicio de la lista
    def add_to_front (self, data):
        self.head = Node(data = data, next = self.head) #Se crea un nodo y se asigna a la cabeza`


    #Metodo para agregar un nodo al final de la lista
    def add_at_end (self, data):
        if not self.head: #Si la cabeza no tiene asignado un nodo
            self.head = Node(data = data) #Se crea un nodo y se asigna a la cabeza
            return #Se termina la ejecucion del metodo
        curr = self.head #Se crea un nodo temporal que apunta a la cabeza
        while curr.next: #Mientras el nodo temporal tenga un nodo siguiente
            curr = curr.next #Se asigna el nodo siguiente al nodo temporal
        curr.next = Node(data = data) #Se crea un nodo y se asigna al nodo siguiente del nodo temporal


    #Metodo para saber si la lista esta vacia
    def is_empy (self):
        return not self.head == None #Se retorna si la cabeza no tiene asignado un nodo


    #Metodo para obtener el dato del nodo al final de la lista
    def get_last_node(self):
        temp = self.head
        while (temp.next is not None):
            temp = temp.next
        return temp.data


    #Metodo para eliminar un elemento de la lista
    def delete_node(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None


