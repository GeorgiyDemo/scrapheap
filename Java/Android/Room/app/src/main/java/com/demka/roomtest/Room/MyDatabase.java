package com.demka.roomtest.Room;

import androidx.room.Database;
import androidx.room.RoomDatabase;

import com.demka.roomtest.Room.Tables.Student;
import com.demka.roomtest.Room.Tables.StudentDetails;

@Database(entities =  {Student.class, StudentDetails.class} , version = 1 , exportSchema = false)
public abstract class MyDatabase extends RoomDatabase {
    public abstract DAO dao();
}
