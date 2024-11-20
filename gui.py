import os
import tkinter as tk
from tkinter import messagebox, ttk
from conexion import conectar
import pymysql
import pandas as pd
import matplotlib.pyplot as plt


# Funciones de manejo de encuestas (crear, actualizar, eliminar, ver)
def crear_encuesta(treeview, entrada_edad, entrada_sexo, entrada_bebidas_semana, entrada_cervezas_semana,
                   entrada_bebidas_fin_semana, entrada_bebidas_destiladas, entrada_vinos_semana,
                   entrada_perdidas_control, entrada_diversion_dependencia, entrada_problemas_digestivos,
                   entrada_tension_alta, entrada_dolor_cabeza):
    edad = entrada_edad.get()
    sexo = entrada_sexo.get()
    bebidas_semana = entrada_bebidas_semana.get()
    cervezas_semana = entrada_cervezas_semana.get()
    bebidas_fin_semana = entrada_bebidas_fin_semana.get()
    bebidas_destiladas = entrada_bebidas_destiladas.get()
    vinos_semana = entrada_vinos_semana.get()
    perdidas_control = entrada_perdidas_control.get()
    diversion_dependencia = entrada_diversion_dependencia.get()
    problemas_digestivos = entrada_problemas_digestivos.get()
    tension_alta = entrada_tension_alta.get()
    dolor_cabeza = entrada_dolor_cabeza.get()

    if not (edad and sexo and bebidas_semana and cervezas_semana and bebidas_fin_semana and
            bebidas_destiladas and vinos_semana and perdidas_control and diversion_dependencia and
            problemas_digestivos and tension_alta and dolor_cabeza):
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos necesarios.")
        return

    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("""
                INSERT INTO ENCUESTA (edad, sexo, BebidasSemana, CervezasSemana, BebidasFinSemana, 
                                      BebidasDestiladasSemana, VinosSemana, PerdidasControl, 
                                      DiversionDependenciaAlcohol, ProblemasDigestivos, TensionAlta, DolorCabeza)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                int(edad), sexo, int(bebidas_semana), int(cervezas_semana), int(bebidas_fin_semana),
                int(bebidas_destiladas), int(vinos_semana), int(perdidas_control), diversion_dependencia,
                problemas_digestivos, tension_alta, dolor_cabeza
            ))
            conexion.commit()
            messagebox.showinfo("Éxito", "Encuesta registrada exitosamente")
            ver_registros(treeview)  # Actualizar la tabla después de la inserción

        except pymysql.MySQLError as err:
            messagebox.showerror("Error de base de datos", f"Hubo un error al insertar el registro: {err}")
        finally:
            conexion.close()


def ver_registros(treeview, filtro=""):
    # Elimina registros actuales del treeview
    for row in treeview.get_children():
        treeview.delete(row)

    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()

            # Consulta SQL con filtro
            if filtro:
                query = f"""
                    SELECT * FROM ENCUESTA 
                    WHERE CONCAT_WS(' ', idEncuesta, edad, sexo, BebidasSemana, CervezasSemana, 
                                    BebidasFinSemana, BebidasDestiladasSemana, VinosSemana, 
                                    PerdidasControl, DiversionDependenciaAlcohol, ProblemasDigestivos, 
                                    TensionAlta, DolorCabeza) LIKE %s
                """
                cursor.execute(query, ('%' + filtro + '%',))
            else:
                query = "SELECT * FROM ENCUESTA"
                cursor.execute(query)

            registros = cursor.fetchall()

            # Agregar registros al treeview
            for registro in registros:
                treeview.insert("", "end", values=registro)

        except pymysql.MySQLError as err:
            messagebox.showerror("Error de base de datos", f"Hubo un error al recuperar los registros: {err}")
        finally:
            conexion.close()



def actualizar_registro(treeview, entrada_edad, entrada_sexo, entrada_bebidas_semana, entrada_cervezas_semana,
                        entrada_bebidas_fin_semana, entrada_bebidas_destiladas, entrada_vinos_semana,
                        entrada_perdidas_control, entrada_diversion_dependencia, entrada_problemas_digestivos,
                        entrada_tension_alta, entrada_dolor_cabeza):
    seleccionado = treeview.selection()
    if not seleccionado:
        messagebox.showwarning("Advertencia", "Por favor, selecciona un registro para actualizar.")
        return

    registro_id = treeview.item(seleccionado)['values'][0]
    edad = entrada_edad.get()
    sexo = entrada_sexo.get()
    bebidas_semana = entrada_bebidas_semana.get()
    cervezas_semana = entrada_cervezas_semana.get()
    bebidas_fin_semana = entrada_bebidas_fin_semana.get()
    bebidas_destiladas = entrada_bebidas_destiladas.get()
    vinos_semana = entrada_vinos_semana.get()
    perdidas_control = entrada_perdidas_control.get()
    diversion_dependencia = entrada_diversion_dependencia.get()
    problemas_digestivos = entrada_problemas_digestivos.get()
    tension_alta = entrada_tension_alta.get()
    dolor_cabeza = entrada_dolor_cabeza.get()

    if not (edad and sexo and bebidas_semana and cervezas_semana and bebidas_fin_semana and
            bebidas_destiladas and vinos_semana and perdidas_control and diversion_dependencia and
            problemas_digestivos and tension_alta and dolor_cabeza):
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos necesarios.")
        return

    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("""
                UPDATE ENCUESTA
                SET edad=%s, sexo=%s, BebidasSemana=%s, CervezasSemana=%s, BebidasFinSemana=%s, 
                    BebidasDestiladasSemana=%s, VinosSemana=%s, PerdidasControl=%s, DiversionDependenciaAlcohol=%s,
                    ProblemasDigestivos=%s, TensionAlta=%s, DolorCabeza=%s
                WHERE idEncuesta=%s
            """, (
                int(edad), sexo, int(bebidas_semana), int(cervezas_semana), int(bebidas_fin_semana),
                int(bebidas_destiladas), int(vinos_semana), int(perdidas_control), diversion_dependencia,
                problemas_digestivos, tension_alta, dolor_cabeza, registro_id
            ))
            conexion.commit()
            messagebox.showinfo("Éxito", "Encuesta actualizada exitosamente")
            ver_registros(treeview)  # Actualizar la tabla después de la actualización

        except pymysql.MySQLError as err:
            messagebox.showerror("Error de base de datos", f"Hubo un error al actualizar el registro: {err}")
        finally:
            conexion.close()


def eliminar_registro(treeview):
    seleccionado = treeview.selection()
    if not seleccionado:
        messagebox.showwarning("Advertencia", "Por favor, selecciona un registro para eliminar.")
        return

    registro_id = treeview.item(seleccionado)['values'][0]
    respuesta = messagebox.askyesno("Confirmar eliminación",
                                    f"¿Estás seguro de eliminar el registro con ID {registro_id}?")
    if respuesta:
        conexion = conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM ENCUESTA WHERE idEncuesta=%s", (registro_id,))
                conexion.commit()
                messagebox.showinfo("Éxito", f"Registro con ID {registro_id} eliminado exitosamente")
                ver_registros(treeview)  # Actualizar la tabla después de la eliminación

            except pymysql.MySQLError as err:
                messagebox.showerror("Error de base de datos", f"Hubo un error al eliminar el registro: {err}")
            finally:
                conexion.close()


def eliminar_encuesta():
    messagebox.showinfo("Eliminar Encuesta", "Función de eliminar encuesta aún no implementada.")


def actualizar_encuesta():
    messagebox.showinfo("Actualizar Encuesta", "Función de actualizar encuesta aún no implementada.")


def exportar_a_excel():
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM ENCUESTA")
            registros = cursor.fetchall()
            columnas = [desc[0] for desc in cursor.description]  # Obtener nombres de las columnas

            # Crear un DataFrame y exportar
            df = pd.DataFrame(registros, columns=columnas)

            # Nombre base del archivo
            base_filename = "encuestas_exportadas.xlsx"
            filename = base_filename

            # Verificar si el archivo ya existe
            counter = 1
            while os.path.exists(filename):
                filename = f"encuestas_exportadas_{counter}.xlsx"
                counter += 1

            # Guardar el archivo con el nuevo nombre
            df.to_excel(filename, index=False)
            messagebox.showinfo("Éxito", f"Datos exportados a {filename}")

        except pymysql.MySQLError as err:
            messagebox.showerror("Error de base de datos", f"Hubo un error al exportar los datos: {err}")
        finally:
            conexion.close()



def mostrar_grafico(treeview):
        conexion = conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM ENCUESTA")
                registros = cursor.fetchall()

                # Extraer los datos relevantes para el gráfico
                edades = [registro[1] for registro in registros]  # Edad (índice 1)
                bebidas_semana = [registro[3] for registro in registros]  # BebidasSemana (índice 3)

                # Crear el gráfico
                plt.figure(figsize=(10, 6))
                plt.bar(edades, bebidas_semana, color='skyblue')
                plt.title('Bebidas por Semana según Edad')
                plt.xlabel('Edad')
                plt.ylabel('Bebidas por Semana')
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()

            except pymysql.MySQLError as err:
                messagebox.showerror("Error de base de datos", f"Hubo un error al recuperar los registros: {err}")
            finally:
                conexion.close()


def crear_interfaz():
    root = tk.Tk()
    root.title("Gestión de Encuestas")

    # Configuración de diseño de la ventana
    root.geometry("1000x600")  # Se aumentó el ancho para ajustarse a más registros

    # Frame de entradas
    frame_entradas = tk.Frame(root)
    frame_entradas.pack(pady=10)

    frame_filtro = tk.Frame(root)
    frame_filtro.pack(pady=10)

    # Entradas de texto (por ejemplo, edad, sexo, etc.)
    tk.Label(frame_entradas, text="Edad:").grid(row=0, column=0)
    entrada_edad = tk.Entry(frame_entradas)
    entrada_edad.grid(row=0, column=1)

    tk.Label(frame_entradas, text="Sexo:").grid(row=1, column=0)
    entrada_sexo = tk.Entry(frame_entradas)
    entrada_sexo.grid(row=1, column=1)

    tk.Label(frame_entradas, text="Bebidas Semana:").grid(row=2, column=0)
    entrada_bebidas_semana = tk.Entry(frame_entradas)
    entrada_bebidas_semana.grid(row=2, column=1)

    tk.Label(frame_entradas, text="Cervezas Semana:").grid(row=3, column=0)
    entrada_cervezas_semana = tk.Entry(frame_entradas)
    entrada_cervezas_semana.grid(row=3, column=1)

    tk.Label(frame_entradas, text="Bebidas Fin Semana:").grid(row=4, column=0)
    entrada_bebidas_fin_semana = tk.Entry(frame_entradas)
    entrada_bebidas_fin_semana.grid(row=4, column=1)

    tk.Label(frame_entradas, text="Bebidas Destiladas Semana:").grid(row=5, column=0)
    entrada_bebidas_destiladas = tk.Entry(frame_entradas)
    entrada_bebidas_destiladas.grid(row=5, column=1)

    tk.Label(frame_entradas, text="Vinos Semana:").grid(row=6, column=0)
    entrada_vinos_semana = tk.Entry(frame_entradas)
    entrada_vinos_semana.grid(row=6, column=1)

    tk.Label(frame_entradas, text="Perdidas Control:").grid(row=7, column=0)
    entrada_perdidas_control = tk.Entry(frame_entradas)
    entrada_perdidas_control.grid(row=7, column=1)

    tk.Label(frame_entradas, text="Diversión Dependencia Alcohol:").grid(row=8, column=0)
    entrada_diversion_dependencia = tk.Entry(frame_entradas)
    entrada_diversion_dependencia.grid(row=8, column=1)

    tk.Label(frame_entradas, text="Problemas Digestivos:").grid(row=9, column=0)
    entrada_problemas_digestivos = tk.Entry(frame_entradas)
    entrada_problemas_digestivos.grid(row=9, column=1)

    tk.Label(frame_entradas, text="Tensión Alta:").grid(row=10, column=0)
    entrada_tension_alta = tk.Entry(frame_entradas)
    entrada_tension_alta.grid(row=10, column=1)

    tk.Label(frame_entradas, text="Dolor de Cabeza:").grid(row=11, column=0)
    entrada_dolor_cabeza = tk.Entry(frame_entradas)
    entrada_dolor_cabeza.grid(row=11, column=1)

    tk.Label(frame_filtro, text="Filtro:").pack(side=tk.LEFT, padx=5)
    entrada_filtro = tk.Entry(frame_filtro, width=30)
    entrada_filtro.pack(side=tk.LEFT, padx=5)

    # Treeview para mostrar los registros
    treeview = ttk.Treeview(root, columns=("ID", "Edad", "Sexo", "BebidasSemana", "CervezasSemana",
                                           "BebidasFinSemana", "BebidasDestiladasSemana", "VinosSemana",
                                           "PerdidasControl", "DiversionDependenciaAlcohol",
                                           "ProblemasDigestivos", "TensionAlta", "DolorCabeza"),
                            show="headings")  # Mostrar solo las cabeceras sin la columna vacía

    # Establecer el tamaño de las columnas
    for col in treeview["columns"]:
        treeview.column(col, width=80)  # Ajustar el ancho de las columnas para que se vean más juntas

    treeview.heading("#1", text="ID")
    treeview.heading("#2", text="Edad")
    treeview.heading("#3", text="Sexo")
    treeview.heading("#4", text="BebidasSemana")
    treeview.heading("#5", text="CervezasSemana")
    treeview.heading("#6", text="BebidasFinSemana")
    treeview.heading("#7", text="BebidasDestiladasSemana")
    treeview.heading("#8", text="VinosSemana")
    treeview.heading("#9", text="PerdidasControl")
    treeview.heading("#10", text="DiversionDependenciaAlcohol")
    treeview.heading("#11", text="ProblemasDigestivos")
    treeview.heading("#12", text="TensionAlta")
    treeview.heading("#13", text="DolorCabeza")

    treeview.pack(fill=tk.BOTH, expand=True)

    # Botones
    botones_frame = tk.Frame(root)
    botones_frame.pack(pady=10)

    tk.Button(botones_frame, text="Crear Encuesta", width=20,
              command=lambda: crear_encuesta(treeview, entrada_edad, entrada_sexo, entrada_bebidas_semana,
                                             entrada_cervezas_semana, entrada_bebidas_fin_semana,
                                             entrada_bebidas_destiladas, entrada_vinos_semana,
                                             entrada_perdidas_control, entrada_diversion_dependencia,
                                             entrada_problemas_digestivos, entrada_tension_alta,
                                             entrada_dolor_cabeza)).grid(row=0, column=0, padx=10)

    tk.Button(botones_frame, text="Actualizar Encuesta", width=20,
              command=actualizar_encuesta).grid(row=0, column=1, padx=10)

    tk.Button(botones_frame, text="Eliminar Encuesta", width=20,
              command=eliminar_encuesta).grid(row=0, column=2, padx=10)

    tk.Button(botones_frame, text="Ver Registros", width=20,
              command=lambda: ver_registros(treeview)).grid(row=1, column=0, padx=10)

    tk.Button(botones_frame, text="Actualizar Registro", width=20,
              command=lambda: actualizar_registro(treeview, entrada_edad, entrada_sexo, entrada_bebidas_semana,
                                                  entrada_cervezas_semana, entrada_bebidas_fin_semana,
                                                  entrada_bebidas_destiladas, entrada_vinos_semana,
                                                  entrada_perdidas_control, entrada_diversion_dependencia,
                                                  entrada_problemas_digestivos, entrada_tension_alta,
                                                  entrada_dolor_cabeza)).grid(row=1, column=1, padx=10)

    tk.Button(botones_frame, text="Eliminar Registro", width=20,
              command=lambda: eliminar_registro(treeview)).grid(row=1, column=2, padx=10)

    tk.Button(botones_frame, text="Exportar a Excel", width=20,
              command=exportar_a_excel).grid(row=2, column=0, padx=10)

    tk.Button(botones_frame, text="Mostrar Gráfico", width=20,
              command=lambda: mostrar_grafico(treeview)).grid(row=2, column=1, padx=10)

    tk.Button(frame_filtro, text="Aplicar Filtro", width=20,
              command=lambda: ver_registros(treeview, entrada_filtro.get())).pack(side=tk.LEFT, padx=5)

    root.mainloop()


# Ejecuta la interfaz
crear_interfaz()
