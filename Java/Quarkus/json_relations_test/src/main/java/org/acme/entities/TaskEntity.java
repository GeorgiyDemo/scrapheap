package org.acme.entities;


import com.fasterxml.jackson.annotation.JsonManagedReference;
import com.vladmihalcea.hibernate.type.json.JsonBinaryType;
import io.quarkus.hibernate.orm.panache.PanacheEntity;
import lombok.Data;
import org.acme.models.WayPointModel;
import org.hibernate.annotations.Type;
import org.hibernate.annotations.TypeDef;

import javax.persistence.*;
import javax.validation.constraints.NotNull;
import java.util.List;

@Data
@Entity
@Table(name = "tasks")
@TypeDef(name = "json", typeClass = JsonBinaryType.class)
public class TaskEntity extends PanacheEntity {

    @NotNull
    private String name;

    @Type(type = "json")
    @Column(columnDefinition = "json")
    @NotNull
    private List<WayPointModel> wayPoints;

    @JsonManagedReference(value = "userTasks")
    @ManyToOne
    @JoinColumn(name = "user_id", nullable = false)
    private UserEntity user;

    @Override
    public String toString() {
        return "TaskEntity{" +
                "name='" + name + '\'' +
                ", wayPoints=" + wayPoints +
                ", user=" + user +
                ", id=" + id +
                '}';
    }
}
