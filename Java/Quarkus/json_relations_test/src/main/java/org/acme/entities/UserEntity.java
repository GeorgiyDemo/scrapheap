package org.acme.entities;

import com.fasterxml.jackson.annotation.JsonBackReference;
import io.quarkus.hibernate.orm.panache.PanacheEntity;
import lombok.Data;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.OneToMany;
import javax.persistence.Table;
import javax.validation.constraints.NotNull;
import java.util.List;


@Data
@Entity
@Table(name = "users")
public class UserEntity extends PanacheEntity {

    @NotNull
    @Column(nullable = false)
    private String name;

    @JsonBackReference(value = "userTasks")
    @OneToMany(mappedBy = "user")
    private List<TaskEntity> tasks;

    @Override
    public String toString() {
        return "UserEntity{" +
                "name='" + name + '\'' +
                ", tasks=" + tasks +
                ", id=" + id +
                '}';
    }
}