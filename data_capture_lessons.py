import configparser
import os
import sqlite3
from pathlib import Path
from tkinter import messagebox

file_root = os.path.abspath(os.path.join(os.getcwd(),".."))
db = file_root+os.path.sep+"MagicRoom.db"

def get_Lessons():
    print (db)
    connection = sqlite3.connect(db)
    cur = connection.cursor()
    sql = "select Lesson_ID, Lesson_Title, Factual_Term1, Factual_Term2,Factual_Term3, Application_Step_Description_1,Application_Steps_Number from Magic_Science_Lessons"
    cur.execute(sql)
    rows = cur.fetchall()
    list_lessons = []
    for element in rows:
        list_lessons.append(element)
    connection.commit()
    connection.close()
    return list_lessons
