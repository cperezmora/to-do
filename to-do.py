import tkinter as tk
from tkinter import messagebox

class AppToDo:
    def __init__(self, raiz):
        # Ventana principal
        self.raiz = raiz
        self.raiz.title('Lista de Tareas')

        # Lista para almacenar las tareas
        self.tareas = []

        # Listbox para mostrar las tareas
        self.lista_tareas = tk.Listbox(raiz, width=50, height=20, font=('Arial', 12))
        self.lista_tareas.pack(pady=20)

        # Entrada de texto para nuevas tareas
        self.entrada_tarea = tk.Entry(raiz, font=('Arial', 14))
        self.entrada_tarea.pack(pady=20)

        # Frame para botones
        self.frame_botones = tk.Frame(raiz)
        self.frame_botones.pack(pady=20)

        # Botón para agregar tarea
        self.btn_agregar = tk.Button(self.frame_botones, text='Agregar', width=15, command=self.agregar_tarea)
        self.btn_agregar.grid(row=0, column=0, padx=10)

        # Botón para eliminar tarea
        self.btn_eliminar = tk.Button(self.frame_botones, text='Eliminar', width=15, command=self.eliminar_tarea)
        self.btn_eliminar.grid(row=0, column=1, padx=10)

    def agregar_tarea(self):
        """Agrega una tarea a la lista."""
        tarea = self.entrada_tarea.get()
        if tarea != "":
            self.tareas.append(tarea)
            self.actualizar_lista_tareas()
            self.entrada_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, introduce una tarea.")

    def eliminar_tarea(self):
        """Elimina una tarea seleccionada de la lista."""
        try:
            indice_tarea = self.lista_tareas.curselection()[0]
            del self.tareas[indice_tarea]
            self.actualizar_lista_tareas()
        except:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")

    def actualizar_lista_tareas(self):
        """Actualiza el Listbox con las tareas actuales."""
        self.lista_tareas.delete(0, tk.END)
        for tarea in self.tareas:
            self.lista_tareas.insert(tk.END, tarea)

if __name__ == "__main__":
    raiz = tk.Tk()
    app_todo = AppToDo(raiz)
    raiz.mainloop()