package com.demka.roomtest.Room;

import androidx.room.Dao;
import androidx.room.Insert;
import androidx.room.Query;

import com.demka.roomtest.Room.Tables.Student;
import com.demka.roomtest.Room.Tables.StudentDetails;
import com.demka.roomtest.Room.Tables.StudentWithDetails;

import java.util.List;

@Dao
public interface DAO {

    @Insert
    public void studentInsertion(Student student);

    @Insert
    public void studentDetailInsertion(StudentDetails studentDetails);

    @Query("Select * from Student")
    public StudentWithDetails getData();

    @Query("Select * from Student")
    List<Student> getStudent();

    @Query("Update Student set stuFirstName = :stuName where stuId = :stuID")
    void updateStu(String stuName , int stuID);

    @Query("Delete from Student where stuId = :stuID")
    void deleteStu (int stuID);

}
