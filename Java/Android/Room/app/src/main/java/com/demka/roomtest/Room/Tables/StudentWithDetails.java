package com.demka.roomtest.Room.Tables;

import androidx.room.Embedded;
import androidx.room.Relation;

import java.util.List;

public class StudentWithDetails {

    @Embedded
    Student student;

    @Relation(
            parentColumn = "stuId",
            entityColumn = "stuId",
            entity = StudentDetails.class)
    public List<StudentDetails> studentDetails;

    public Student getStudent() {
        return student;
    }

    public void setStudent(Student student) {
        this.student = student;
    }

    public List<StudentDetails> getStudentDetails() {
        return studentDetails;
    }

    public void setStudentDetails(List<StudentDetails> studentDetails) {
        this.studentDetails = studentDetails;
    }
}
