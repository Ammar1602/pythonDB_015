import tkinter as tk
from tkinter import messagebox
import sqlite3

def submit_nilai():
    # Ambil data
    nama_siswa = entry.nama.get()
    nilai_biologi = int(entry.biologi.get())
    nilai_fisika = int(entry.fisika.get())
    nilai_inggris = int(entry.inggris.get())

    # Hitung nilai tertinggi
    nilai_tertinggi = max(nilai_biologi, nilai_fisika, nilai_inggris)
    prediksi = ""
    if nilai_tertinggi == nilai_biologi:
        prediksiprodi = "Kedokteran"
    elif nilai_tertinggi == nilai_fisika:
        prediksiprodi = "Teknik"
    elif nilai_tertinggi == nilai_inggris:
        prediksiprodi = "Bahasa"
    

    # Tampilkan hasil 
    messagebox.showinfo("Hasil Prediksi", f"Prediksi Prodi: {prediksiprodi}")